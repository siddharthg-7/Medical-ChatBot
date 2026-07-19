import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def transcribe_patient_voice(audio_filepath):
    groq_api_key = os.environ.get("GROQ_API_KEY")

    client = Groq(api_key=groq_api_key)
    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model=os.environ.get("WHISPER_MODEL", "whisper-large-v3"),
        )

    return transcription.text

if __name__ == "__main__":
    audio_filepath="patient_voice_test.mp3"
    record_audio(audio_filepath, timeout=20, phrase_time_limit=10)
    
    print("Transcribing audio...")
    transcription = transcribe_patient_voice(audio_filepath)
    print(f"\nTranscription: {transcription}")