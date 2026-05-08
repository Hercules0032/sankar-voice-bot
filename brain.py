import requests
import json
import time

class VoiceBotBrain:
    def __init__(self):
        self.api_key = "AIzaSyDf5_8jHGkXknxenP3oQ1dCW9BaKOREGL4"
        # We use v1beta and the latest stable alias
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
        
        self.system_instruction = (
            "You are a helpful assistant for Sonkor Group. "
            "Speak in a natural mix of Hindi and Telugu. "
            "Respond in 15 words or less."
        )

    def get_response(self, user_text: str):
        payload = {
            "contents": [{"parts": [{"text": f"{self.system_instruction}\nUser: {user_text}"}]}]
        }
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.post(self.url, headers=headers, data=json.dumps(payload))
            res_json = response.json()
            
            # If we hit the rate limit shown in your screenshot (429 error)
            if response.status_code == 429:
                return "Namaste! System busy hai, please ek minute baad try karein."

            if 'candidates' in res_json:
                return res_json['candidates'][0]['content']['parts'][0]['text']
            
            # If the 404 returns, it means that specific model name is still locked
            return "Namaste! Main Sonkor AI Assistant hoon. Meeru ela unnaru?"
            
        except Exception as e:
            return "Connection error. Please check your internet."