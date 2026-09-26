# VERY EASY AI CLOUD PROJECT

This is a simple assignment project:
- Python + Flask
- Google Gemini AI API
- Render cloud deployment

## Change only one thing

Open `app.py` and change:

STUDENT_ID = "YOUR_STUDENT_ID"

to your real student ID.

You can also change STUDENT_NAME if needed.

## GitHub

Upload only:
- app.py
- requirements.txt
- README.md

## Render

Create a Web Service from the GitHub repository.

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn app:app

## Render Environment Variable

Key:
GEMINI_API_KEY

Value:
Your Gemini API key

Do NOT put the API key in app.py.

## Test

Open the Render URL and ask:

Explain cloud computing in simple words.

If an answer appears, the project works.
