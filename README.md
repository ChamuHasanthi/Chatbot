# Gemini Chatbot Setup

This document outlines the steps to set up and run the Gemini chatbot application.

## Prerequisites

- Python 3.6 or higher
- Git (for cloning the repository)

## Installation

**Clone the Repository**

Clone this repository to your local machine:

## Create a Virtual Environment

Create a virtual environment to manage your project dependencies:

### For Linux/MacOS:

```
python3 -m venv gemini_env
source gemini_env/bin/activate
```

### For Windows:

```
python -m venv gemini_env
gemini_env\Scripts\activate
```

## Install Dependencies

Install the required Python packages using pip:

```
pip install google-genai
pip install dotenv
```

## Configure the Environment

Create a .env file in the root of your project directory to store your API key.

`touch .env`

Add your Google Gemini API key in the .env file to project root

Ini, TOML

GEMINI_API_KEY="your-api-key-here"

**Important**: Replace "your-api-key-here" with your actual Google Gemini API key.

## Run test

test.py created without using .env

- replace your API key directly to check wheter test environment

_from test.py_

```
2 |
3 | client = genai.Client(api_key="Add_your_API_Key")
4 |
```

## Run the Chatbot

Run the chatbot script to start the application:

```
python3 gemini_chat.py
```

## Deactivate the Virtual Environment (Optional)

Once you're done, you can deactivate the virtual environment:

```
deactivate
```
