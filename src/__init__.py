from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

from datetime import date
from flask_cors import CORS
from flask_cors import cross_origin

from src.services.oracle import Oracle


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
        data = oracle.get_next_mcu_movie()
        return render_template(
            'page.html',
            title=data["title"],
            days=data["days_until"],
            poster_url=data["poster_url"]
        )

    # Return JSON data at /api
    @app.route("/api", methods=["GET"])
    @cross_origin()
    def api():
        try:
            given_date = request.args.get("date", type=str)

            # If they give us a date, try to parse it in ISO format
            if given_date:
                desired_date = str(date.fromisoformat(given_date))
                return jsonify(oracle.get_next_mcu_movie(desired_date))
            else:
                return jsonify(oracle.get_next_mcu_movie())

        except ValueError:
            return jsonify(oracle.get_next_mcu_movie())

    return app
