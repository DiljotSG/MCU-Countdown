from flask import Flask
from flask import request
from flask import jsonify
from datetime import date
from flask_cors import CORS
from flask_cors import cross_origin

from src.oracle import Oracle


def create_app():
    oracle = Oracle()
    app = Flask(__name__)
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app)

    # Establish the root endpoint
    # Return HTML data at root
    @app.route("/", methods=["GET"])
    @cross_origin()
    def root():
        return oracle.get_next_movie_html()

    # Return JSON data at /api
    @app.route("/api", methods=["GET"])
    @cross_origin()
    def api():
        try:
            given_date = request.args.get("date", type=str)
            if given_date:
                desired_date = str(date.fromisoformat(given_date))
                return jsonify(oracle.get_next_movie_json(desired_date))
            else:
                return jsonify(oracle.get_next_movie_json())
        except ValueError:
            return jsonify(oracle.get_next_movie_json())

    return app
