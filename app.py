from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>tmdh-business</title>
    </head>
    <body>
        <h1>설명</h1>
        <p>이 사이트는 간단한 설명을 위한 예제입니다.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
