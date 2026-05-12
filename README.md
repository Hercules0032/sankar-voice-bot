# Sankar Group – Hindi + Telugu Voice Bot

## Tech Stack
- **Frontend**: HTML5 + CSS3 + Vanilla JS
- **STT**: Web Speech API (hi-IN + te-IN)
- **TTS**: Web SpeechSynthesis API (hi-IN + te-IN)
- **Logic**: Pattern-matching engine (Bilingual)
- **Backend**: Python Flask / Gunicorn
- **Hosting**: Render

## Setup
```bash
pip install -r requirements.txt
gunicorn server:app