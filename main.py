from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "index page"

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    app.run(host=host, port=port, debug=True)
