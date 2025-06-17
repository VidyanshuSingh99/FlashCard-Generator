import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
TITLE = os.getenv("TITLE", "Flashcard Generator")

def generate_flashcards(content, subject=None, difficulty=None):
    base_instruction = "Generate 10–15 question-answer flashcards from the following educational content.\n"

    if subject:
        base_instruction += f"The content is related to {subject}.\n"
    if difficulty:
        base_instruction += f"Generate the flashcards at a {difficulty} level.\n"

    full_prompt = f"{base_instruction}\nContent:\n{content}"

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "X-Title": TITLE,
        },
        json={
            "model": "deepseek/deepseek-r1:free",
            "messages": [{"role": "user", "content": full_prompt}]
        }
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"API Error: {response.status_code}, {response.text}")
