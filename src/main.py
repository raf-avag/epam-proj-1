from flask import redirect, url_for, session, request, Flask, flash
from .app import views

app = Flask(__name__)


@app.route("/api/v1/post/<post_id>", methods=["POST"])
def post(post_id):
    content = request.json
    views.APIView(content)
    flash("Message posted to %s: %s" % (post_id, content), "info")


if __name__ == "__main__":
    app.run(host="0.0.0.5000", debug=True)
