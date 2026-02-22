import time
from functools import lru_cache
from pathlib import Path

import gradio as gr
import soundfile as sf
from kittentts import KittenTTS

SAMPLE_RATE = 24000
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MODELS = {
    "Nano Int8 (25MB) - KittenML/kitten-tts-nano-0.8-int8": "KittenML/kitten-tts-nano-0.8-int8",
    "Nano (56MB) - KittenML/kitten-tts-nano-0.8": "KittenML/kitten-tts-nano-0.8",
    "Micro (41MB) - KittenML/kitten-tts-micro-0.8": "KittenML/kitten-tts-micro-0.8",
    "Mini (80MB) - KittenML/kitten-tts-mini-0.8": "KittenML/kitten-tts-mini-0.8",
}

VOICES = ["Bella", "Jasper", "Luna", "Bruno", "Rosie", "Hugo", "Kiki", "Leo"]


@lru_cache(maxsize=4)
def load_model(model_id: str) -> KittenTTS:
    return KittenTTS(model_id)


def synthesize(text: str, model_label: str, voice: str, speed: float):
    text = (text or "").strip()
    if not text:
        raise gr.Error("Enter some text first.")

    model_id = MODELS[model_label]
    model = load_model(model_id)

    kwargs = {"voice": voice, "speed": float(speed)}
    try:
        audio = model.generate(text, **kwargs)
    except TypeError:
        kwargs.pop("speed", None)
        audio = model.generate(text, **kwargs)

    out_path = OUTPUT_DIR / f"kittentts_{int(time.time() * 1000)}.wav"
    sf.write(out_path, audio, SAMPLE_RATE)
    return str(out_path), f"Saved: {out_path}"


with gr.Blocks(title="KittenTTS UI") as demo:
    gr.Markdown("# KittenTTS UI")
    gr.Markdown("Local web UI for KittenML/KittenTTS. First run downloads the selected model from Hugging Face.")

    with gr.Row():
        with gr.Column(scale=2):
            text = gr.Textbox(
                label="Text",
                lines=8,
                placeholder="Type text to synthesize...",
                value="Hello from KittenTTS running locally.",
            )
            model_label = gr.Dropdown(
                label="Model",
                choices=list(MODELS.keys()),
                value="Nano Int8 (25MB) - KittenML/kitten-tts-nano-0.8-int8",
            )
            voice = gr.Dropdown(label="Voice", choices=VOICES, value="Bella")
            speed = gr.Slider(label="Speed", minimum=0.5, maximum=1.8, step=0.05, value=1.0)
            run_btn = gr.Button("Generate", variant="primary")
        with gr.Column(scale=1):
            audio_out = gr.Audio(label="Output", type="filepath")
            status = gr.Textbox(label="Status", interactive=False)

    run_btn.click(
        fn=synthesize,
        inputs=[text, model_label, voice, speed],
        outputs=[audio_out, status],
    )


if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, inbrowser=True)
