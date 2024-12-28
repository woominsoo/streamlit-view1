from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML 템플릿
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>글자 띄우기</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <h1>웹사이트에 글자를 띄우기</h1>
    <form method="post">
        <input type="text" name="user_input" placeholder="글자를 입력하세요">
        <button type="submit">제출</button>
    </form>
    {% if user_input %}
    <h2>입력한 내용:</h2>
    <div style="font-size: 24px; color: blue;">{{ user_input }}</div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    user_input = None
    if request.method == "POST":
        user_input = request.form.get("user_input")
    return render_template_string(html_template, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
