from deepgram import DeepgramClient, SpeakOptions
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DOCTOR_AUDIO = BASE_DIR / "doctor_response.mp3"

def convert_text_to_doctor_audio(text, output_filepath=DEFAULT_DOCTOR_AUDIO):
    deepgram_api_key = os.environ.get("DEEPGRAM_API_KEY")
    deepgram = DeepgramClient(api_key=deepgram_api_key)
    
    options = SpeakOptions(
        model=os.environ.get("DEEPGRAM_TTS_MODEL", "aura-asteria-en"),
        encoding="mp3",
    )
    
    deepgram.speak.rest.v1.save(str(output_filepath), {"text": text}, options)
    return Path(output_filepath)

import subprocess
import platform
def play_audio(audio_filepath):
    audio_filepath = str(audio_filepath)

    if platform.system() == "Darwin":
        subprocess.run(["afplay", audio_filepath], check=False)
    elif platform.system() == "Windows":
        os.startfile(audio_filepath)
    else:
        subprocess.run(["xdg-open", audio_filepath], check=False)

