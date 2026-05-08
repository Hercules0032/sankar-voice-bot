import os
import shutil
import uuid
import json
import ssl

# GLOBAL SSL BYPASS: Required for downloading Whisper models and API calls on macOS
ssl._create_default_https_context = ssl._create_unverified_context

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import whisper
import edge_tts
from brain import VoiceBotBrain

app = FastAPI()
brain = VoiceBotBrain()

# Setup necessary directories [cite: 31, 38]
os.makedirs("uploads", exist_ok=True)
os.makedirs("static/audio", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load Whisper STT Model [cite: 15, 59]
# The 'base' model is the best balance of speed and multilingual accuracy for your Mac
model = whisper.load_model("base")

@app.post("/chat")
async def chat_endpoint(file: UploadFile = File(...)):
    # 1. Save the incoming audio file locally
    temp_filename = f"uploads/{uuid.uuid4()}.wav"
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 2. Speech-to-Text (STT): Handles Hindi + Telugu mix [cite: 8, 17]
    try:
        result = model.transcribe(temp_filename)
        user_text = result['text']
    except Exception as e:
        print(f"STT Error: {e}")
        user_text = "Audio processing failed."

    # 3. Logic: Get mixed-language response from Gemini [cite: 18, 65]
    bot_text = brain.get_response(user_text)

    # 4. Text-to-Speech (TTS): Generate response audio [cite: 21, 59]
    # We use a neural Indian voice (Madhur) for a natural Hindi-Telugu blend
    audio_output_filename = f"audio/{uuid.uuid4()}.mp3"
    audio_full_path = f"static/{audio_output_filename}"
    
    communicate = edge_tts.Communicate(bot_text, "hi-IN-MadhurNeural")
    await communicate.save(audio_full_path)

    # 5. Conversation Logs: Store history in JSON format [cite: 38, 45]
    log_entry = {
        "id": str(uuid.uuid4()),
        "user": user_text,
        "bot": bot_text,
        "audio_path": audio_output_filename
    }
    
    with open("logs.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    # Return data to frontend UI [cite: 33, 34, 35]
    return {
        "user_text": user_text,
        "bot_text": bot_text,
        "audio_url": f"/static/{audio_output_filename}"
    }

@app.get("/")
async def read_index():
    # Serves the frontend UI [cite: 30]
    return FileResponse('static/index.html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)