# Chatbot with Google Gemini API

This project integrates Google Gemini API to create a chatbot in Python.

## 🚀 Setup Instructions

### **1️⃣ Clone the Repository**


### Create a Virtual Environment


python3 -m venv gemini_env
source gemini_env/bin/activate 

On Windows use: gemini_env\Scripts\activate

# install packages
pip install google-genai
pip install dotenv

# Set Up the Environment File

Create a .env file inside the project directory.

Add your API key:

GEMINI_API_KEY="your-api-key-here"

# Run the Chatbot

python3 gemini_chat.py

# Deactivate the Virtual Environment (Optional)

deactivate