from google import genai
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")

clinet = genai.Client(api_key = API_KEY)

def ask_gemini(prompt: str) -> str:
    response = clinet.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text

if __name__ == "__main__":
    reply = ask_gemini("how good are you ?")
    print("AI: ",reply)