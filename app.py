import os
from flask import Flask, request

try:
    from google import genai
except Exception:
    genai = None

app = Flask(__name__)

# ===== CHANGE ONLY THIS =====
STUDENT_NAME = "MD Najmul Islam"
STUDENT_ID = "2026512841"
# ============================

def page(question="", answer=""):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>AI Study Assistant</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{
            font-family: Arial, sans-serif;
            background:#eef2ff;
            margin:0;
            padding:40px 15px;
        }}
        .box {{
            max-width:700px;
            margin:auto;
            background:white;
            padding:30px;
            border-radius:18px;
            box-shadow:0 5px 20px #bbb;
        }}
        h1 {{ color:#2563eb; }}
        .student {{
            background:#f1f5f9;
            padding:15px;
            border-radius:10px;
            line-height:1.7;
        }}
        textarea {{
            width:100%;
            height:120px;
            padding:12px;
            box-sizing:border-box;
            border:1px solid #ccc;
            border-radius:10px;
            font-size:16px;
        }}
        button {{
            margin-top:12px;
            padding:12px 25px;
            background:#2563eb;
            color:white;
            border:0;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        }}
        .answer {{
            margin-top:25px;
            background:#eff6ff;
            padding:20px;
            border-radius:10px;
            white-space:pre-wrap;
        }}
    </style>
</head>
<body>
<div class="box">
    <h1>🤖 AI Study Assistant</h1>

    <div class="student">
        <b>Student Name:</b> {STUDENT_NAME}<br>
        <b>Student ID:</b> {STUDENT_ID}
    </div>

    <h3>Ask AI</h3>

    <form method="POST">
        <textarea name="question"
        placeholder="Example: Explain cloud computing in simple words."
        required>{question}</textarea>
        <br>
        <button type="submit">Ask AI</button>
    </form>

    {f'<div class="answer"><b>AI Answer:</b><br><br>{answer}</div>' if answer else ''}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    question = ""
    answer = ""

    if request.method == "POST":
        question = request.form.get("question", "").strip()
        key = os.environ.get("GEMINI_API_KEY")

        if not key:
            answer = "Gemini API key is missing. Add GEMINI_API_KEY in Render Environment Variables."

        elif genai is None:
            answer = "Google Gemini package is not installed. Check requirements.txt."

        else:
            try:
                client = genai.Client(api_key=key)
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=question
                )
                answer = response.text or "No answer returned."
            except Exception as e:
                answer = "AI connection error. Please check your Gemini API key."

    return page(question, answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
