from datetime import date, timedelta

from flask import Blueprint, jsonify, render_template, request
from flask_cors import CORS, cross_origin

from src.common import is_valid_date
from src.consts import NOT_FOUND
from src.services.oracle import Oracle

mod = Blueprint('root', __name__)
cors = CORS(mod)
oracle = Oracle()


def render_page(data: dict):
    if data is None or len(data) < 1:
        return render_template("404.html"), NOT_FOUND

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


@mod.route("/", methods=["GET"])
@cross_origin()
def root():
    given_date = request.args.get("date", type=str)

    if not given_date:
        return render_page(oracle.get_next_mcu_production())

    if not is_valid_date(given_date):
        return render_page(oracle.get_next_mcu_production())

    desired_date = str(date.fromisoformat(given_date))
    return render_page(oracle.get_next_mcu_production(desired_date))


@mod.route("/api", methods=["GET"])
@cross_origin()
def api():
    given_date = request.args.get("date", type=str)

    if not given_date:
        return jsonify(oracle.get_next_mcu_production())

    if not is_valid_date(given_date):
        return jsonify(oracle.get_next_mcu_production())

    desired_date = str(date.fromisoformat(given_date))
    return jsonify(oracle.get_next_mcu_production(desired_date))
