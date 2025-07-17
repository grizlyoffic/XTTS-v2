import os
import torch
from TTS.api import TTS
from uuid import uuid4

# Load XTTSv2
MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"
tts = TTS(MODEL_NAME, gpu=torch.cuda.is_available())

# Path to your cloned voice sample
REFERENCE_AUDIO = "voice_sample/your_voice.wav"

# Output folder
os.makedirs("outputs", exist_ok=True)

def synthesize_text(text: str) -> str:
    output_path = f"outputs/{uuid4().hex}.wav"
    tts.tts_to_file(
        text=text,
        speaker_wav=REFERENCE_AUDIO,
        language="en",
        file_path=output_path
    )
    return output_path
