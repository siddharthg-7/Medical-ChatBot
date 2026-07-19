<div align="center">
  
# AI Medical Assistant (Medical-ChatBot)

An intelligent, multimodal AI medical consultation platform. Users can describe their symptoms via voice, upload medical images (like X-rays or rashes), or provide videos to receive immediate, professional guidance from an AI doctor, complete with a spoken voice response.

**[Report Bug](#feedback)** • **[Request Feature](#feedback)**

</div>

---

##  Features

-  **Voice Interaction** - Speak directly to the AI doctor using Deepgram Speech-to-Text.
-  **Multimodal Vision** - Upload medical images or videos for the AI to analyze using Groq's LLaMA Vision models.
-  **AI Medical Guidance** - Receive empathetic, professional, and rapid general medical advice.
-  **Voice Responses** - The AI doctor speaks back to you using ultra-realistic Deepgram Text-to-Speech.
-  **Modern UI** - Beautiful, responsive glassmorphism interface built with Gradio.
-  **Lightning Fast** - Powered by Groq's LPU inference engine for near-instant responses.

---

##  Tech Stack

### Core Application
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Gradio](https://img.shields.io/badge/Gradio-FF7C00?style=for-the-badge&logo=gradio&logoColor=white) ![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white)

### AI Models & APIs
![Groq](https://img.shields.io/badge/Groq-f55036?style=for-the-badge&logo=groq&logoColor=white) ![Deepgram](https://img.shields.io/badge/Deepgram-130F25?style=for-the-badge&logo=deepgram&logoColor=white) ![LLaMA Vision](https://img.shields.io/badge/LLaMA_3.2_Vision-0452C8?style=for-the-badge&logo=meta&logoColor=white)

### Package Management
![uv](https://img.shields.io/badge/uv-2B2B2B?style=for-the-badge&logo=rust&logoColor=white)

---

##  Installation & Local Setup

### 1. Clone Repository
```bash
git clone https://github.com/siddharthg-7/Medical-ChatBot.git
cd Medical-ChatBot
```

### 2. Install Dependencies
This project uses `uv` for lightning-fast Python package management. 

```bash
# Install dependencies using uv
uv sync

# Or using standard pip
pip install -r requirements.txt
```

*Note: You must have [FFmpeg](https://ffmpeg.org/download.html) installed on your system for audio and video processing to work.*

### 3. Environment Variables
Create a `.env` file in the root directory and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
DEEPGRAM_API_KEY=your_deepgram_api_key_here
GROQ_MODEL=llama-3.2-11b-vision-preview
```

### 4. Start the Application
```bash
# Run the application
uv run main.py
```
The application will launch on your local host (usually `http://127.0.0.1:7860`).

---

##  Deployment

To deploy this project to **Hugging Face Spaces** (Recommended for Gradio apps):

1. Create a new Gradio Space on Hugging Face.
2. Upload all project files (`main.py`, `brain_of_doctor.py`, `requirements.txt`, etc.).
3. Ensure `packages.txt` is present (it contains `ffmpeg` which the cloud server needs).
4. Go to your Space **Settings** and add your `GROQ_API_KEY` and `DEEPGRAM_API_KEY` to the **Variables and secrets** section.
5. Watch it build and go live!

---

##  Usage Workflow

###  Patient Workflow
1. Click the microphone icon to **Describe Your Symptoms** via voice.
2. (Optional) **Upload a Medical Image** (e.g., an X-ray, rash, or wound).
3. (Optional) **Upload a Video** for further context.
4. Click **Analyze Medical Condition**.
5. Read the generated transcript and listen to the AI Doctor's voice response.

---

##  Roadmap

- [x] Speech-to-Text Integration
- [x] LLaMA Vision Multimodal Setup
- [x] Text-to-Speech Integration
- [x] Beautiful Glassmorphism UI
- [x] Generalize from Skin to all Medical queries
- [ ] Add chat history / conversation memory
- [ ] PDF Upload for Lab Results
- [ ] Multi-language voice support

---

## **Optimizations**

-  Dynamically handling OS-specific FFmpeg paths to prevent deployment crashes on Linux servers.
-   Used **Groq** to drastically reduce LLM inference latency.
-   Optimized media processing using lightweight `ffmpeg` sub-process extraction for video frames.
-   Modularized code into `brain_of_doctor`, `voice_of_doctor`, and `voice_of_patient`.
-   Designed a completely custom **responsive UI** overriding default Gradio themes with CSS variables and custom SVGs.

---

##  Author

**@sidharthg-7**

---

##  Feedback & Support

- **Feedback:** If you have any feedback, suggestions, or feature requests, feel free to open an issue or reach out through GitHub.
- **Support:** If you found this project useful, consider giving it a **STAR** on GitHub!
