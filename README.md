# KittenTTS UI

Simple local web UI for `KittenML/KittenTTS`.

## Why you could not find a folder
If you installed KittenTTS with `pip`, the package is placed in your Python environment `site-packages`, not inside `C:\AI`.

## Setup
1. Open PowerShell in `C:\AI\KittenTTS-UI`
2. (Optional) create a virtual env:
   `python -m venv .venv`
   `.\.venv\Scripts\Activate.ps1`
3. Install dependencies:
   `pip install -r requirements.txt`
4. Run:
   `python app.py`

The UI opens at `http://127.0.0.1:7860`.

## Notes
- First generation downloads the selected model from Hugging Face.
- Output wav files are saved in `C:\AI\KittenTTS-UI\outputs`.
- Model options and voices come from the official KittenTTS README.

## Share With KittenTTS Team
If you want to propose this as an official UI, open a new issue in this repo and choose:
- `KittenTTS Official UI Proposal`

That template includes a ready-to-send message for the KittenTTS maintainers.
