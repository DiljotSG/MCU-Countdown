from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

from datetime import date
from datetime import timedelta
from flask_cors import CORS
from flask_cors import cross_origin

from src.constants.values import NOT_FOUND
from src.services.oracle import Oracle


def create_app():  # noqa: C901
    oracle = Oracle()
    app = Flask(__name__, static_folder='static', static_url_path='')
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app)

    # Establish the root endpoint
    # Return HTML data at root
    @app.route("/", methods=["GET"])
    @cross_origin()
    def root():
        def render_page(data: dict):
            if len(data) > 1:
                release_date = data.get("release_date", None)
                next_url = None
                if release_date:
                    next_day = date.fromisoformat(release_date) + timedelta(days=1)
                    next_url = "/?date={}".format(date.isoformat(next_day))
                return render_template(
                    'page.html',
                    title=data.get("title", ""),
                    days=data.get("days_until", 0),
                    poster_url=data.get("poster_url", ""),
                    release_date=data.get("release_date", ""),
                    overview=data.get("overview", ""),
                    type=data.get("type", ""),
                    upcoming_title=data.get("following_production", {}).get("title", None),
                    next_url=next_url
                )
            return render_template("404.html"), NOT_FOUND
        try:
            given_date = request.args.get("date", type=str)

            # If they give us a date, try to parse it in ISO format
            if given_date:
                desired_date = str(date.fromisoformat(given_date))
                return render_page(oracle.get_next_mcu_production(desired_date))
            else:
                return render_page(oracle.get_next_mcu_production())

        except ValueError:
            return render_page(oracle.get_next_mcu_production())

    # Return JSON data at /api
    @app.route("/api", methods=["GET"])
    @cross_origin()
    def api():
        try:
            given_date = request.args.get("date", type=str)

            # If they give us a date, try to parse it in ISO format
            if given_date:
                desired_date = str(date.fromisoformat(given_date))
                return jsonify(oracle.get_next_mcu_production(desired_date))
            else:
                return jsonify(oracle.get_next_mcu_production())

        except ValueError:
            return jsonify(oracle.get_next_mcu_production())

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), NOT_FOUND

    return app
