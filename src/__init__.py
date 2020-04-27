from flask import Flask
from flask import jsonify
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
        return jsonify(oracle.get_next_movie_json())

    return app
