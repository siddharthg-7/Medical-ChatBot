from pathlib import Path
import os
import platform

# Only add local FFmpeg path if running on Windows locally
if platform.system() == "Windows":
    os.environ["PATH"] += os.pathsep + r"C:\Users\Siddharth\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Essentials_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-essentials_build\bin"

import gradio as gr

from brain_of_doctor import brain_of_the_doctor
from voice_of_doctor import convert_text_to_doctor_audio
from voice_of_patient import transcribe_patient_voice

APP_TITLE = "AI Medical Assistant"

# -----------------
# CUSTOM THEME & CSS
# -----------------
custom_theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="indigo",
    neutral_hue="slate",
    spacing_size="lg",
    radius_size="lg",
    font=[gr.themes.GoogleFont('Outfit'), 'ui-sans-serif', 'system-ui', 'sans-serif'],
).set(
    body_background_fill="#f6f8fd",
    block_background_fill="#ffffff",
    block_border_width="0px",
    block_shadow="0 4px 15px rgba(0, 0, 0, 0.03)",
    button_primary_background_fill="#2563EB",
    button_primary_background_fill_hover="#1d4ed8",
    button_primary_text_color="#ffffff",
)

CUSTOM_CSS = """
/* Force Light Mode Aesthetics & Increase Font Sizes globally */
:root, .dark {
    --body-text-color: #0f172a !important;
    --body-text-color-subdued: #475569 !important;
    --background-fill-primary: #f0f4fd !important;
    --background-fill-secondary: #ffffff !important;
    --border-color-primary: #e2e8f0 !important;
    --block-background-fill: rgba(255, 255, 255, 0.9) !important;
    --block-label-text-color: #334155 !important;
    --input-background-fill: rgba(255, 255, 255, 0.9) !important;
    --input-background-fill-hover: #ffffff !important;
    --text-sm: 15px !important;
    --text-md: 17px !important;
    --text-lg: 19px !important;
    --text-xl: 24px !important;
}

/* Global Styles */
body, .gradio-container {
    background: linear-gradient(135deg, #f0f4fd 0%, #e0e8f8 100%) !important;
    font-family: 'Outfit', system-ui, -apple-system, sans-serif !important;
    min-height: 100vh;
    color: #0f172a !important;
}

/* Centered container with max width */
.main-container {
    max-width: 1400px !important;
    margin: 0 auto !important;
    padding: 40px 24px !important;
}

/* Header Styling */
.header-card {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(226, 232, 240, 0.8);
    border-radius: 24px;
    padding: 32px 48px;
    margin-bottom: 40px;
    box-shadow: 0 10px 40px rgba(37, 99, 235, 0.08);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.header-title h1 {
    font-size: 44px !important;
    font-weight: 700 !important;
    background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    line-height: 1.2;
}

.header-title p {
    font-size: 19px !important;
    color: #475569 !important;
    margin: 10px 0 0 0;
    font-weight: 500 !important;
}

.privacy-shield {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #059669 !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    background: rgba(209, 250, 229, 0.9);
    padding: 12px 24px;
    border-radius: 999px;
    border: 1px solid rgba(167, 243, 208, 0.8);
}

/* Card Wrappers */
.panel-card {
    background: rgba(255, 255, 255, 0.85) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 1px solid rgba(226, 232, 240, 0.8) !important;
    border-radius: 24px !important;
    padding: 36px !important;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.05) !important;
    height: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 20px !important;
}

.section-title {
    font-size: 26px !important;
    font-weight: 700 !important;
    color: #0f172a !important;
    display: flex;
    align-items: center;
    gap: 14px;
    padding-bottom: 20px;
    border-bottom: 2px solid rgba(226, 232, 240, 0.8);
}

/* Gradient Icons in titles */
.section-title svg {
    stroke: url(#blue-gradient);
    filter: drop-shadow(0 2px 4px rgba(37,99,235,0.2));
}

/* Input Wrappers */
.input-wrapper {
    background: white;
    border-radius: 16px;
    padding: 20px;
    border: 1px solid #cbd5e1;
    box-shadow: 0 2px 10px rgba(0,0,0,0.02);
}
.input-label {
    font-size: 18px !important;
    font-weight: 700 !important;
    color: #1e293b !important;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* Info Box */
.info-box {
    background: linear-gradient(135deg, rgba(239, 246, 255, 0.95), rgba(224, 231, 255, 0.95));
    border: 1px solid rgba(191, 219, 254, 0.8);
    border-radius: 16px;
    padding: 24px;
    display: flex;
    gap: 16px;
    color: #1e40af !important;
    font-size: 17px !important;
    font-weight: 500 !important;
    line-height: 1.6;
    margin-top: auto;
}
.info-box .icon {
    font-size: 26px;
}

/* Analyze Button Override */
.analyze-btn {
    font-size: 20px !important;
    font-weight: 700 !important;
    height: 68px !important;
    margin-top: 16px !important;
    border-radius: 16px !important;
    background: linear-gradient(135deg, #2563EB 0%, #4F46E5 100%) !important;
    border: none !important;
    color: white !important;
    box-shadow: 0 10px 30px rgba(37, 99, 235, 0.3) !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}

.analyze-btn:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 15px 40px rgba(37, 99, 235, 0.4) !important;
}

.analyze-btn:active {
    transform: translateY(1px) !important;
}

/* Footer */
.footer-disclaimer {
    text-align: center;
    color: #475569 !important;
    font-size: 16px !important;
    margin-top: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 30px;
    border-top: 1px solid rgba(226, 232, 240, 0.8);
}

/* Transcript and Markdown */
.markdown-output {
    font-size: 18px !important;
    line-height: 1.8 !important;
    color: #0f172a !important;
    background: #ffffff !important;
    padding: 30px !important;
    border-radius: 20px !important;
    border: 1px solid #cbd5e1 !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.03) !important;
}

.markdown-output h1, .markdown-output h2, .markdown-output h3 {
    color: #0f172a !important;
    font-weight: 700 !important;
    margin-top: 1.5em !important;
    margin-bottom: 0.8em !important;
}

/* Clean up Gradio default borders inside panel */
.panel-card .gradio-container, .panel-card .gr-block {
    border: none !important;
    background: transparent !important;
    box-shadow: none !important;
}

/* Animated Spinner for Loading */
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
.loader-spin {
    animation: spin 1s linear infinite;
}

/* Glassmorphism for inputs */
.gr-input, .gr-box {
    background: rgba(255,255,255,0.95) !important;
    color: #0f172a !important;
    font-size: 17px !important;
}

.gr-form {
    background: transparent !important;
}

.gr-padded {
    padding: 16px !important;
}

/* Responsive Design */
@media (max-width: 768px) {
    .header-card {
        flex-direction: column !important;
        text-align: center !important;
        gap: 20px !important;
        padding: 24px !important;
    }
    .header-title h1 {
        font-size: 32px !important;
    }
    .main-container {
        padding: 16px 12px !important;
    }
    .panel-card {
        padding: 24px !important;
    }
}
"""

def process_inputs(audio_filepath, image_filepath, video_filepath):
    if not audio_filepath and not image_filepath and not video_filepath:
        raise gr.Error("Please provide some input (voice description, medical image, or video) before analysis.")

    patient_text = transcribe_patient_voice(audio_filepath)
    doctor_text = brain_of_the_doctor(
        patient_text=patient_text,
        image_filepath=image_filepath,
        video_filepath=video_filepath,
    )
    doctor_audio = convert_text_to_doctor_audio(doctor_text)

    # Return results and hide the loading HTML block
    return patient_text, doctor_text, str(Path(doctor_audio)), gr.update(visible=False)

with gr.Blocks(title=APP_TITLE) as iface:
    # Add SVG Gradient Definition
    gr.HTML("""
    <svg style="width:0;height:0;position:absolute;" aria-hidden="true" focusable="false">
      <linearGradient id="blue-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#2563EB" />
        <stop offset="100%" stop-color="#4F46E5" />
      </linearGradient>
    </svg>
    """)
    
    with gr.Column(elem_classes="main-container"):
        
        # Header
        gr.HTML("""
        <div class="header-card">
            <div class="header-title">
                <h1>AI Medical Assistant</h1>
                <p>Intelligent general medical consultation powered by multimodal AI.</p>
            </div>
            <div class="privacy-shield">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                HIPAA Compliant
            </div>
        </div>
        """)
        
        with gr.Row(equal_height=True):
            # Left Panel - Patient Input (35%)
            with gr.Column(scale=35, min_width=320, elem_classes="panel-card"):
                gr.HTML("""
                <div class="section-title">
                    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><polyline points="16 11 18 13 22 9"></polyline></svg>
                    Patient Input
                </div>
                """)
                
                with gr.Group(elem_classes="input-wrapper"):
                    gr.HTML('<div class="input-label"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg> Describe Your Symptoms or Concern</div>')
                    audio_input = gr.Audio(
                        sources=["microphone", "upload"], 
                        type="filepath",
                        show_label=False
                    )
                
                with gr.Group(elem_classes="input-wrapper"):
                    gr.HTML('<div class="input-label"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg> Upload Medical Image (Optional)</div>')
                    image_input = gr.Image(
                        type="filepath",
                        show_label=False
                    )
                
                with gr.Group(elem_classes="input-wrapper"):
                    gr.HTML('<div class="input-label"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"></polygon><rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect></svg> Upload Medical Video (Optional)</div>')
                    video_input = gr.Video(
                        show_label=False
                    )
                
                analyze_button = gr.Button("Analyze Medical Condition", elem_classes="analyze-btn")
                
                gr.HTML("""
                <div class="info-box">
                    <div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg></div>
                    <div>For best results, upload clear images under good lighting. Adding a short video improves AI assessment accuracy significantly.</div>
                </div>
                """)
                
            # Right Panel - Doctor Response (65%)
            with gr.Column(scale=65, min_width=320, elem_classes="panel-card"):
                gr.HTML("""
                <div class="section-title">
                    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"></path><path d="M12 5 9.04 7.96a2.1 2.1 0 0 0 0 2.97l.46.46a2.1 2.1 0 0 0 2.97 0l2.97-2.97"></path></svg>
                    AI Doctor Response
                </div>
                """)
                
                loading_status = gr.HTML("""
                <div style="text-align: center; padding: 80px 0; color: #64748b; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;">
                    <div style="background: #f1f5f9; padding: 24px; border-radius: 50%; margin-bottom: 24px;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v4"></path><path d="M12 18v4"></path><path d="M4.93 4.93l2.83 2.83"></path><path d="M16.24 16.24l2.83 2.83"></path><path d="M2 12h4"></path><path d="M18 12h4"></path><path d="M4.93 19.07l2.83-2.83"></path><path d="M16.24 7.76l2.83-2.83"></path></svg>
                    </div>
                    <div style="font-size: 24px; font-weight: 600; color: #334155; margin-bottom: 8px;">Ready for Analysis</div>
                    <div style="font-size: 16px;">Provide your inputs on the left and click Analyze.</div>
                </div>
                """)
                
                with gr.Group():
                    transcript_output = gr.Textbox(
                        label="Patient Transcript",
                        interactive=False,
                        lines=3
                    )
                
                with gr.Group():
                    gr.HTML('<div class="input-label" style="margin-top: 16px;"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg> Doctor Guidance</div>')
                    response_output = gr.Markdown(
                        elem_classes="markdown-output"
                    )
                
                with gr.Group():
                    gr.HTML('<div class="input-label" style="margin-top: 16px;"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg> Doctor Voice Response</div>')
                    audio_output = gr.Audio(
                        type="filepath",
                        autoplay=True,
                        show_label=False
                    )
                    
        # Footer
        gr.HTML("""
        <div class="footer-disclaimer">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
            AI guidance is informational only and should not replace consultation with a licensed medical professional.
        </div>
        """)

    # When analyze button is clicked, first show a loading HTML, then process the inputs.
    analyze_button.click(
        fn=lambda: gr.update(value='<div style="text-align: center; padding: 80px 0; color: #2563EB; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;"><div class="loader-spin" style="width:48px; height:48px; border:4px solid #e0e7ff; border-top-color:#2563EB; border-radius:50%; margin-bottom:24px;"></div><div style="font-size: 20px; font-weight: 600;">Analyzing Medical Data...</div><div style="font-size: 15px; color: #64748b; margin-top: 8px;">Please wait while the AI Doctor evaluates your inputs.</div></div>', visible=True),
        outputs=[loading_status]
    ).then(
        fn=process_inputs,
        inputs=[audio_input, image_input, video_input],
        outputs=[transcript_output, response_output, audio_output, loading_status],
    )

if __name__ == "__main__":
    iface.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860)),
        theme=custom_theme,
        css=CUSTOM_CSS,
        debug=True, 
        head='<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>'
    )