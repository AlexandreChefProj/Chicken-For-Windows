import os
import requests
from dotenv import load_dotenv

load_dotenv()

def feed_ai(question):
    with open("personnality.txt", "r") as file:
        prompt = file.read()
    with open("pref.txt", "r") as file:
        pref = file.read()
    # Get the API key from the environment
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set GEMINI_API_KEY in your .env file.")

    # Define the API endpoint
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    # Define the headers and payload
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{"text": f"{prompt}{pref}\nEnd of the preferences, here is the user question:\n\n{question}"}]
        }]
    }
    print(f"{prompt}{pref}\nEnd of the preferences, here is the user question:\n\n{question}")
    try:
        # Send the POST request
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            # Extract the AI's response text
            candidates = data.get("candidates", [])
            if candidates:
                ai_response = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                return ai_response.strip()
            else:
                return "error"
        else:
            return f"Error: Received status code {response.status_code} with message: {response.text}"
    
    except requests.exceptions.RequestException as e:
        return f"An error occurred while communicating with the API: {e}"


if __name__ == "__main__":
    q = "Hey can you start steam for me real quick?"
    print(feed_ai(q))