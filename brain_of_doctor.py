import base64
import os
import re
from io import BytesIO

from dotenv import load_dotenv
from groq import Groq
from PIL import Image


load_dotenv()


def encode_image_for_groq(filepath):
    image = Image.open(filepath)
    image.thumbnail((1024, 1024))

    buffer = BytesIO()
    image.convert("RGB").save(buffer, format="JPEG", quality=75)
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


def brain_of_the_doctor(patient_text, image_filepath=None, video_filepath=None):
    groq_api_key = os.environ.get("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("Missing GROQ_API_KEY in .env or environment")

    prompt = (
        "You are a confident, natural, and highly knowledgeable general practitioner doctor. Speak with the reassurance, clarity, and authority of a real doctor. "
        "Limit your entire response to two or three sentences maximum. "
        "Do not use any special characters, symbols, asterisks, or markdown formatting in your response because it will be converted directly to audio.\n\n"
        f"Patient text: {patient_text}"
    )

    # If video is provided but no image, or even if both are provided, we can extract a frame from the video 
    # to serve as the visual input if needed.
    if video_filepath and not image_filepath:
        import subprocess
        import tempfile
        # Extract a frame from the video at 1 second mark (or the first frame if shorter)
        temp_image = tempfile.mktemp(suffix=".jpg")
        try:
            subprocess.run([
                "ffmpeg", "-y", "-i", video_filepath, 
                "-vframes", "1", "-ss", "00:00:00.500", 
                temp_image
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            image_filepath = temp_image
            prompt += "\n\nThe patient provided a video. I have extracted a representative frame from the video for you to analyze."
        except Exception as e:
            raise ValueError(f"Failed to extract frame from video: {str(e)}")
    elif video_filepath and image_filepath:
        prompt += "\n\nThe patient provided both an image and a video. Please analyze the provided image as the primary visual reference."

    client = Groq(api_key=groq_api_key)
    
    # Construct the user message depending on whether an image was provided
    user_content = [{"type": "text", "text": prompt}]
    if image_filepath:
        image_data = encode_image_for_groq(image_filepath)
        user_content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{image_data}",
            },
        })

    response = client.chat.completions.create(
        model=os.environ.get("GROQ_MODEL", "llama-3.2-11b-vision-preview"),
        max_completion_tokens=4096,
        messages=[
            {
                "role": "system",
                "content": "You are a careful medical assistant. Give general information, not a diagnosis. Be highly empathetic.",
            },
            {
                "role": "user",
                "content": user_content,
            },
        ],
    )

    content = response.choices[0].message.content
    
    # Qwen models output a <think> block. Let's cleanly remove it.
    # The (?:</think>|$) ensures we remove it even if the model runs out of tokens and cuts off before the closing tag.
    content = re.sub(r"<think>.*?(?:</think>|$)", "", content, flags=re.DOTALL).strip()
    return content


if __name__ == "__main__":
    response = brain_of_the_doctor("What do you see in this image?")
    print("Doctor's response:")
    print(response)
