from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
client=genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(system_instruction="""You are Jarvis, a helpful and intelligent desktop assistant that supports a Python program.
- Answer all questions the user asks.
- Keep responses short, clear, and polite (2-3 sentences max).
- Do not execute code or commands, just provide text responses.
- If the user greets you, greet them back as Jarvis
- if something you can't do just say sorry or something like this.""",thinking_config=types.ThinkingConfig(thinking_budget=0)),
)

def ask_ai(query):
    response = chat.send_message(query)
    return response.text
    