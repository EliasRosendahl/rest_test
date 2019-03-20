from flask import Flask, request, abort, Blueprint


bp = Blueprint('frontend', __name__)


@bp.route("/")
def index():
    return "ok"


def create_app(config=None):
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app


if __name__ == "__main__":
    app.create_app()
    app.run(debug=True)
