# Virtual Try-On System
An AI-powered virtual try-on application that allows users to visualize how clothing items would look on them using advanced diffusion models.

## 🌟 Features

- **AI-Powered Try-On**: Uses Stable Diffusion and Dreambooth models to generate realistic clothing overlays
- **Web Application**: User-friendly Next.js interface for uploading selfies and outfit images
- **Chrome Extension**: Browser extension to capture clothing images from e-commerce websites
- **Email Notifications**: Receive results via email after processing
- **Image Processing Pipeline**: Automated image captioning, cropping, and augmentation
- **RESTful API**: Django-based backend with API endpoints for seamless integration

## 🏗️ Architecture

The project consists of four main components:

```
virtual-try-on-team/
├── frontend/           # Next.js web application
├── backend/            # Django REST API
├── chrome-plugin/      # Chrome extension
├── diffusion/          # Diffusion model training scripts
├── diffusion_improved/ # Enhanced diffusion implementation
└── diffusion_optimization/ # Performance optimization techniques
```

## 🛠️ Technology Stack

### Frontend
- **Framework**: Next.js 14
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **HTTP Client**: Axios
- **UI**: React 18

### Backend
- **Framework**: Django 4.1
- **API**: Django Ninja
- **Database**: SQLite (development)
- **Storage**: Local file storage (configurable for AWS S3)
- **CORS**: django-cors-headers

### AI/ML
- **Model**: Stable Diffusion with Dreambooth fine-tuning
- **Image Processing**: BLIP captioning
- **Framework**: PyTorch
- **Optimization**: Mixed precision training, gradient checkpointing

### Chrome Extension
- **Manifest Version**: 3
- **Permissions**: Storage, Active Tab, Scripting

## 📋 Prerequisites

- **Node.js** (v18 or higher)
- **Python** (v3.8 or higher)
- **pip** and **virtualenv**
- **Chrome Browser** (for extension testing)
- **CUDA-capable GPU** (recommended for diffusion model training)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/jeesunikim/virtual-try-on-team.git
cd virtual-try-on-team
```

### 2. Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env.local  # Configure environment variables
npm run dev
```

The frontend will be available at `http://localhost:3000`

### 3. Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Create .env file with required variables
cat > .env << EOF
SECRET_KEY=your-secret-key-here
DEBUG=True
EOF

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

The backend API will be available at `http://127.0.0.1:8000`

### 4. Chrome Extension Setup

1. Open Chrome and navigate to `chrome://extensions/`
2. Enable "Developer mode" in the top right
3. Click "Load unpacked"
4. Select the `chrome-plugin` directory from the project
5. The GetDressed extension will now appear in your browser

### 5. Diffusion Model Setup

```bash
cd diffusion

# Install dependencies
pip install diffusers transformers accelerate torch torchvision

# Run training scripts (adjust paths as needed)
bash identity_run.sh    # Train identity model
bash clothes_run.sh     # Train clothing overlay model
bash transforms.sh      # Process and augment images
```

## 📖 Usage

### Web Application

1. Navigate to `http://localhost:3000`
2. Upload a body image (clear photo of yourself)
3. Upload an outfit/clothing item image
4. Enter your email address
5. Submit and wait for processing
6. Receive results via email or in the interface

### API Endpoints

#### Try-On Endpoint
```bash
POST /api/try_on_outfit/{email}
Content-Type: multipart/form-data

Parameters:
- email: User's email address
- selfie: Image file (user's photo)
- outfit: Image file (clothing item)

Response:
{
  "message": "This is what it looks like"
}
```

## 🔬 How It Works

### Diffusion Model Pipeline

1. **User Input**: Upload 12 pictures of yourself for personalized model training
2. **Dreambooth Training**: Fine-tune a Stable Diffusion model on your images
3. **Mask Generation**: Create or generate masks defining where clothing appears
4. **Inpainting**: Apply clothing overlay using the trained diffusion model
5. **Refinement**: Iteratively improve output through the denoising process

### Key Parameters
- Training steps: 1000
- Learning rate: 5e-6
- Sampling: DDIM (fewer steps, faster inference)
- Precision: Mixed FP16/FP32 for optimal performance

### Image Processing
- **BLIP Captioning**: Automatic image description generation
- **Crop & Augment**: Preprocessing for consistent input dimensions
- **Mask Application**: Guide model for realistic clothing placement

## 🎯 Performance Optimization

The project implements several optimization techniques:

- **Mixed Precision Training**: Using PyTorch AMP for faster computation
- **Gradient Checkpointing**: Reduced memory usage for larger batches
- **Efficient Sampling**: DDIM and PFGM for fewer diffusion steps
- **Flash Attention**: Memory-efficient attention mechanisms
- **Dynamic Batching**: Minimized GPU idle time

## 📁 Project Structure

```
virtual-try-on-team/
├── frontend/
│   ├── app/                 # Next.js app directory
│   ├── src/
│   │   ├── components/      # React components
│   │   └── helpers/         # Utility functions
│   ├── public/              # Static assets
│   └── package.json
├── backend/
│   ├── django_project/      # Django settings
│   ├── try_on/              # Main app
│   │   ├── api.py          # API endpoints
│   │   ├── models.py       # Database models
│   │   └── schemas.py      # Request/response schemas
│   ├── emails/              # Email functionality
│   ├── media/               # Uploaded files
│   └── manage.py
├── chrome-plugin/
│   ├── manifest.json        # Extension configuration
│   ├── popup/               # Extension UI
│   ├── content-script.js    # Page interaction
│   └── background.js        # Background processes
├── diffusion/
│   ├── captioning/          # BLIP image captioning
│   ├── transforms/          # Image preprocessing
│   ├── clothes_run.sh       # Clothing model training
│   └── identity_run.sh      # Identity model training
├── diffusion_improved/      # Enhanced model implementation
└── diffusion_optimization/  # Performance improvements
```

## 🗄️ Database Models

### User Model
- Email (unique identifier)
- Extended from Django's AbstractUser

### Try Model
- User (foreign key)
- Selfie image
- Outfit image
- Timestamps

## 🔐 Environment Variables

### Backend (.env)
```env
SECRET_KEY=your-django-secret-key
DEBUG=True
# Optional AWS S3 configuration
# AWS_ACCESS_KEY_ID=your-aws-access-key
# AWS_SECRET_ACCESS_KEY=your-aws-secret-key
# AWS_STORAGE_BUCKET_NAME=your-bucket-name
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

## 📚 References

- [Stable Diffusion Inpainting](https://github.com/huggingface/diffusers/tree/main/examples/research_projects/dreambooth_inpaint)
- [Cloth Virtual Try-On](https://github.com/belider/cloth-virtual-try-on-using-stable-diffusion)
- [Diffusers with TorchAO](https://github.com/sayakpaul/diffusers-torchao)
- [Next.js Documentation](https://nextjs.org/docs)
- [Django Ninja Documentation](https://django-ninja.rest-framework.com/)

## 🐛 Known Issues

- ML model integration is partially implemented (placeholder functions)
- Email notification system needs configuration
- AWS S3 storage is commented out (local storage used by default)
- Training requires significant computational resources
