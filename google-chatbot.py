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
    print("Ai - Type ExitChat if you want to exit")

    while True:
        user_input = input("You: ")

        if user_input.strip() == "ExitChat":
            print("see you another time")
            break
        if user_input.strip():
            reply = ask_gemini(user_input)
            print(f"AI: {reply}\n")
        else:
            print("please enter a message. \n")