from flask import Flask, request, abort

def create_app(config=None):
    app = Flask(__name__)


@app.route("/")
def index():
    return "ok"


if __name__ == "__main__":
    app.create_app()
    app.run(debug=True)
