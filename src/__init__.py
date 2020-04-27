from flask import Flask
from flask import request
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
    @app.route("/", methods=["GET"])
    @cross_origin()
    def root():
        try:
            output = request.args.get("json", type=str)
            if output:
                return jsonify(oracle.get_next_movie_json())
            else:
                return oracle.get_next_movie_html()
        except ValueError:
            return oracle.get_next_movie_html()

    return app
