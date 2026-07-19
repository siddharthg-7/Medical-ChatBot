import os
import subprocess
import sys
import traceback

os.environ["PATH"] += os.pathsep + r"C:\Users\Siddharth\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Essentials_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-essentials_build\bin"

sys.path.append(r"c:\project-self-1\ai-medical-chatbot")

from brain_of_doctor import brain_of_the_doctor

try:
    video_path = "dummy_video.mp4"
    if not os.path.exists(video_path):
        subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "color=c=blue:s=320x240:d=2", video_path], check=True)

    res = brain_of_the_doctor("Hello doctor", image_filepath=None, video_filepath=video_path)
    print("Success:", res)
except Exception as e:
    traceback.print_exc()
