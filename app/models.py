import torch
from transformers import AutoProcessor, BarkModel, BarkProcessor
import numpy as np
from .schemas import VoicePresets

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_audio_model() -> tuple[BarkProcessor, BarkModel]: 
    """Load Bark text-to-speech model and processor."""
    try:
        processor = AutoProcessor.from_pretrained("suno/bark-small")
        model = BarkModel.from_pretrained("suno/bark-small")
        model = model.to(device) # type:ignore
        model.eval()  # ✅ Set to evaluation mode
        print(f"Model loaded successfully on {device}")
        return processor, model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise

def generate_audio(
    processor: BarkProcessor, 
    model: BarkModel,
    prompt: str,
    preset: VoicePresets
) -> tuple[np.ndarray, int]:
    """Generate audio from text using Bark model."""
    try:
        # Process input
        inputs = processor(
            text=prompt, 
            return_tensors="pt", 
            voice_preset=preset
        )
        
        # Move inputs to device
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        # Generate audio without gradient calculation
        with torch.no_grad():
            audio_array = model.generate(**inputs, do_sample=True)
        
        # Convert to numpy
        output = audio_array.cpu().numpy().squeeze()
        
        # Get sample rate from model config
        sample_rate = model.generation_config.sample_rate # type:ignore
        
        return output, sample_rate
    
    except Exception as e:
        print(f"Error generating audio: {e}")
        raise