from datetime import date, timedelta

from flask import Blueprint, jsonify, make_response, render_template, request
from flask_cors import CORS, cross_origin
from werkzeug.exceptions import NotFound

from src.consts import NAMED_LISTS
from src.services.oracle import Oracle

mod = Blueprint("root", __name__)
cors = CORS(mod)
oracle = Oracle()


def add_cache_headers(response, max_age=3600):
    response.headers["Cache-Control"] = f"public, max-age={max_age}"
    response.headers["Vary"] = "Accept-Encoding"
    return response


def render_page(data: dict, list_id: int = None):
    if data is None or len(data) < 1:
        raise NotFound()

    release_date = data.get("release_date", None)
    next_url = None
    if release_date:
        next_day = date.fromisoformat(release_date) + timedelta(days=1)
        if list_id:
            next_url = "/?date={}&list_id={}".format(date.isoformat(next_day), list_id)
        else:
            next_url = "/?date={}".format(date.isoformat(next_day))
    return render_template(
        "page.html",
        title=data.get("title", ""),
        days=data.get("days_until", 0),
        poster_url=data.get("poster_url", ""),
        release_date=data.get("release_date", ""),
        overview=data.get("overview", ""),
        type=data.get("type", ""),
        upcoming_title=data.get("following_production", {}).get("title", None),
        next_url=next_url,
        is_custom_list=(list_id is not None),
    )


def handle_countdown_request(list_id: int = None, list_name: str = None):
    given_date = request.args.get("date", type=str)

    try:
        desired_date = date.fromisoformat(given_date) if given_date else None
    except (ValueError, TypeError):
        desired_date = None

    data = oracle.get_next_mcu_production(
        desired_date=desired_date, tmdb_list_id=list_id
    )
    response = make_response(render_page(data, list_id=list_id))
    return add_cache_headers(response)


@mod.route("/", methods=["GET"])
@cross_origin()
def root():
    list_id = request.args.get("list_id", type=int)
    return handle_countdown_request(list_id=list_id)


@mod.route("/<string:list_name>", methods=["GET"])
@cross_origin()
def named_list(list_name: str):
    if list_name not in NAMED_LISTS:
        raise NotFound()

    list_config = NAMED_LISTS[list_name]
    list_id = list_config["list_id"]

    return handle_countdown_request(list_id=list_id, list_name=list_config["name"])


@mod.route("/api", methods=["GET"])
@cross_origin()
def api():
    given_date = request.args.get("date", type=str)
    list_id = request.args.get("list_id", type=int)

    try:
        desired_date = date.fromisoformat(given_date) if given_date else None
    except (ValueError, TypeError):
        desired_date = None

    data = oracle.get_next_mcu_production(
        desired_date=desired_date, tmdb_list_id=list_id
    )
    response = make_response(jsonify(data))
    return add_cache_headers(response)
