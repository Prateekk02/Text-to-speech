# Text-to-Speech API

A FastAPI-based text-to-speech service using the Bark model from Suno AI. This project provides a RESTful API endpoint to generate high-quality audio from text input with multiple voice presets.

## Features

- Text-to-speech generation using Suno's Bark model
- Multiple voice preset options
- RESTful API built with FastAPI
- Streaming audio response
- GPU acceleration support

## Project Structure
```
Text-to-speech/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── schemas.py
│   └── utils.py
├── main.py
├── requirements.txt
├── client.py
├── .gitignore
└── README.md
```

## Requirements

### System Requirements
- Python 3.10 or higher
- 4GB RAM minimum (8GB recommended)
- CUDA-compatible GPU (optional, for faster inference)

### Python Dependencies

#### Backend
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
torch==2.1.0
transformers==4.35.0
numpy==1.24.3
soundfile==0.12.1
pydantic==2.5.0
python-multipart==0.0.6
```

#### Frontend
```
streamlit==1.28.0
requests==2.31.0
```

## Installation

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/Prateekk02/Text-to-speech.git
cd Text-to-speech
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```


## Usage

### Running Locally

#### Start Backend Server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
The API will be available at `http://localhost:8000`

API documentation available at `http://localhost:8000/docs`

#### Start Frontend
```bash
streamlit run client.py
```
The Streamlit interface will be available at `http://localhost:8501`


### API Endpoints

#### Generate Audio
```
GET /generate/audio
```

**Parameters:**
- `prompt` (string, required): Text to convert to speech
- `preset` (string, optional): Voice preset (default: "v2/en_speaker_1")



**Example Request:**
```bash
curl "http://localhost:8000/generate/audio?prompt=Hello%20World&preset=v2/en_speaker_1" \
  --output audio.wav
```

**Python Example:**
```python
import requests

url = "http://localhost:8000/generate/audio"
params = {
    "prompt": "Hello, this is a test!",
    "preset": "v2/en_speaker_1"
}

response = requests.get(url, params=params)


## Development

### Code Formatting
```bash
# Install formatting tools
pip install black flake8 isort

# Format code
black .
isort .
flake8 .
```



## Performance Optimization

### CPU Optimization
- Use quantized models for faster inference
- Reduce the number of workers in production

### GPU Optimization
- Use mixed precision training (fp16)
- Batch multiple requests together
- Enable CUDA graphs for faster inference

### Memory Management
```python
import torch

# Clear cache periodically
torch.cuda.empty_cache()

# Use gradient checkpointing
model.gradient_checkpointing_enable()
```

## Model Information

This project uses the Bark model from Suno AI:
- Model: `suno/bark-small`
- Size: ~1GB
- Sample Rate: 24kHz
- License: MIT

For more information: https://github.com/suno-ai/bark


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Suno AI for the Bark model
- Hugging Face for the transformers library
- FastAPI team for the excellent web framework
- Streamlit team for the interactive frontend framework

## Contact

Prateek - GitHub: [@Prateekk02](https://github.com/Prateekk02)

Project Link: [https://github.com/Prateekk02/Text-to-speech](https://github.com/Prateekk02/Text-to-speech)


## References

- [Bark Documentation](https://github.com/suno-ai/bark)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Transformers Documentation](https://huggingface.co/docs/transformers/)
- [Streamlit Documentation](https://docs.streamlit.io/)