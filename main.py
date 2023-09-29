from flask import Flask, request, abort, jsonify, Response
import random
import datetime
import concurrent.futures

import services
from models.horse import Horse

app = Flask(__name__)  # Create a flask app


@app.route("/")
def base_route():
    """Default route, return the list of available routes"""
    rank = "0.25"
    rank_float = float(rank)
    print(rank_float)

    date = datetime.datetime.now()
    print(date.strftime("%Y-%m-%d %H:%M:%S.%f"))

    return Response(
        {
            "routes_available": [
                {
                    "route": "/horse/<horseId>?category=",
                    "verb": "GET",
                    "description": "Return the horse results for 2023",
                }
            ]
        },
        mimetype="application/json",
    )
    return


@app.route("/horse/<horseId>")
def get_horse_results(horseId):
    """Returns the horse data.

    UriParam:
      horseId: the Horde id to filter

    QueryParam:
      category : optional category to filter on

    Returns: the Horse object

    """
    args = request.args
    print(f"Category:{args.get('category', default=None, type=str)}")

    # To be implemented

    abort(404, description="Resource not found")


# Set the correct methods for this route
@app.route("/horse/export-podium", methods=[""])
def export_podium():
    """Return the podium per categories for 3 best horses.

    Args:
      The list of horses

    Returns: the podium
    """

    return jsonify({})


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=random.randint(2000, 9000))
