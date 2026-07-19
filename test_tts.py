import os
from deepgram import DeepgramClient
from dotenv import load_dotenv

load_dotenv()
deepgram_api_key = os.environ.get("DEEPGRAM_API_KEY")
deepgram = DeepgramClient(api_key=deepgram_api_key)

audio = deepgram.speak.v1.audio.generate(
    text="hello",
    model="aura-asteria-en",
    encoding="mp3",
)

with open("test_audio.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)
        
print("Bytes written:", os.path.getsize("test_audio.mp3"))
