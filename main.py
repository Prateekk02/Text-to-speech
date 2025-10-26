from fastapi import FastAPI, status
from fastapi.responses import StreamingResponse
from app import load_audio_model, generate_audio, VoicePresets, audio_array_to_buffer

route = FastAPI()

@route.get(
    "/generate/audio",
    responses={status.HTTP_200_OK: {"content": {"audio/wav": {}}}},
    response_class=StreamingResponse,
)
def serve_text_to_audio_model_controller(
    prompt: str,
    preset: VoicePresets = 'v2/en_speaker_1',
):
    processor,model = load_audio_model()
    output, sample_rate = generate_audio(processor,model, prompt,preset)
    return StreamingResponse(
        audio_array_to_buffer(output, sample_rate), media_type="audio/wav"
    )
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000) 