# Sankar Group – Hindi + Telugu Voice Bot

## Tech Stack
- **Frontend**: HTML5 + CSS3 + Vanilla JS (single file)
- **STT**: Web Speech API (browser-native, supports hi-IN + te-IN)
- **TTS**: Browser SpeechSynthesis API (hi-IN + te-IN voices)
- **Response Logic**: AI-based via Anthropic Claude API (+ rule-based fallback)
- **Backend**: Python Flask (for serving + conversation log persistence)
- **Hosting**: ngrok

## Features
- 🎤 Mic button with live recording animation
- 📝 Live transcript bar
- 💬 Chat conversation view (user + bot bubbles)
- 🔊 Auto-play bot voice response (+ manual replay button)
- 🌐 Language switcher: Hindi / Telugu / Mix
- ⌨ Text input fallback (for unsupported browsers)
- 📋 Conversation logs (download as .txt or .json)
- 📱 Mobile + desktop responsive

## Supported Conversations
| User Says | Bot Replies |
|-----------|-------------|
| Namaste / Hello | Greeting in Hindi+Telugu |
| Naa peru / Mera naam [name] | Personalised response |
| Demo chahiye / demo kavali | Demo scheduling |
| Price / cost | Pricing info |
| Contact / phone | Contact details |
| Time / hours | Working hours |
| Bye / alvida | Farewell |

## Setup & Run

### Option 1 – Open directly (no backend needed)
Just open `voicebot.html` in Chrome or Edge.
> Note: Firefox has limited Speech API support. Use Chrome for best experience.

### Option 2 – With Flask backend (for persistent logs + ngrok)
```bash
pip install flask flask-cors
python server.py
```
Then in another terminal:
```bash
ngrok http 5000
```
Copy the ngrok HTTPS URL and share it.

## Submission
- **Candidate Name**: [Your Name]
- **Tech Stack**: HTML/CSS/JS + Web Speech API + Python Flask
- **Ngrok URL**: [paste after running ngrok]
- **GitHub Repo**: [paste if applicable]

## Notes
- Microphone permission required (browser will prompt)
- Best results in Google Chrome / Microsoft Edge
- Hindi voices available on most OS; Telugu voice availability varies by device
