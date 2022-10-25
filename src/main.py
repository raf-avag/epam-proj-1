from flask import redirect, url_for, session, request, Flask, flash
from .app import views
from .infrastructure.config import CONFIG


def create_app(config_class=CONFIG):
    app = Flask(__name__)
    app.config.from_object(config_class)
    return app


app = create_app()


@app.route("/api/v1/post/<post_id>", methods=["POST"])
def post(post_id):
    content = request.json
    views.APIView(content).post()
    return "Message posted to %s: %s" % (post_id, content), "info"
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.5000")
