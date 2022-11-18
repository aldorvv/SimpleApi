from http import HTTPStatus

from flask import Flask
from flask import make_response, Response, request

from pokeclient import PokeClient
from stats import Stats


app = Flask(__name__)
client = PokeClient()
DEFAULT_MAX = 64


@app.route("/allBerryStats", methods=["GET"])
def root() -> Response:
    client.limit = int(request.args.get("limit", DEFAULT_MAX))
    stats = Stats(client.times)
    return make_response(
        stats.all() | {"berries_names": client.berries},
        HTTPStatus.OK
    )
