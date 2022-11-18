from flask import Flask
from flask import Response


app = Flask(__name__)


@app.route("/", methods=["GET"])
def root() -> Response:
    return Response(b"OK")
