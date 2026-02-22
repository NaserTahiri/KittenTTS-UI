## Summary
I built and tested a local Gradio UI wrapper for KittenTTS and wanted to suggest it as a potential official UI option for users who want a simple, no-code interface.

## What This UI Provides
- Text input for synthesis
- Model selector (nano int8 / nano / micro / mini)
- Voice selector (Bella, Jasper, Luna, etc.)
- Speed control
- Audio playback and saved `.wav` output

## Why This Helps
- Many users install `kittentts` via `pip` but expect a visible app/folder UI.
- A small official UI can reduce onboarding friction.
- It can serve as a reference implementation for local desktop usage.

## Validation Completed
- UI launches at `http://127.0.0.1:7860`
- Local endpoint responds (`HTTP 200`)
- Real inference works and writes output `.wav` files end-to-end

## Repository
- Link: https://github.com/NaserTahiri/KittenTTS-UI

## Suggested Next Step For Maintainers
If useful, I can provide this as a clean PR with:
- `app.py`
- `requirements.txt`
- `README` quickstart
- optional Windows launcher (`run.bat`)
