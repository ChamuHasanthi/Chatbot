import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

print(os.getenv("GEMINI_API_KEY"))
# Configure the API key from the environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

# Get user input in a loop
while True:
    prompt = input("You: ")
    if prompt.lower() in ['exit', 'quit', 'bye']:
        print("Gemini: Goodbye!")
        break

    try:
        # Generate the response
        response = model.generate_content(prompt)
        print("Gemini:", response.text)
    except Exception as e:
        print(f"Gemini: An error occurred: {e}")