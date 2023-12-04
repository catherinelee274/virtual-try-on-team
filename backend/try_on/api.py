from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Query, UploadedFile, File, Router
from try_on.models import Try, User

from try_on.schemas import TryOnRequest

router = Router()


@router.post("/try_on_outfit/{email}")
def try_on_outfit(
    request: HttpRequest,
    email: str,
    selfie: UploadedFile = File(...),
    outfit: UploadedFile = File(...),
):
    # Find the user by email
    user = get_object_or_404(User, email=email)
    try_on = Try.objects.create(user=user)

    # TODO upload to s3
    try_on.selfie.save(selfie.name, selfie)
    try_on.outfit.save(outfit.name, outfit)

    # send images to mode
    _send_images_to_model()

    # send email to user
    _send_email_to_user()

    # Wait for training
    _poll_training_model()

    # Send response from ML model
    return {"message": "This is what it looks like"}


def _send_images_to_model():
    pass


def _send_email_to_user():
    pass


def _poll_training_model():
    pass
