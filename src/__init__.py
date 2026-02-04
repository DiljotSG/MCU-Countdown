from http import HTTPStatus

from flask import Flask, render_template
from flask_cors import CORS

from src.exceptions import ListNotFoundError, NoUpcomingProductionsError
from src.routes.root import mod as root_mod


class RelaxedFlask(Flask):
    def add_url_rule(self, *args, **kwargs):
        if "strict_slashes" not in kwargs:
            kwargs["strict_slashes"] = False
        super(RelaxedFlask, self).add_url_rule(*args, **kwargs)


def create_flask_app():
    app = RelaxedFlask(
        __name__,
        static_url_path='',
        template_folder="../templates",
        static_folder="../static",
    )
    app.config["CORS_HEADERS"] = "Content-Type"
    CORS(app)

    app.register_blueprint(root_mod, url_prefix="/")

    @app.errorhandler(HTTPStatus.NOT_FOUND)
    @app.errorhandler(ListNotFoundError)
    def handle_not_found(e):
        return render_template("404.html"), HTTPStatus.NOT_FOUND

    @app.errorhandler(NoUpcomingProductionsError)
    def handle_no_upcoming_productions(e):
        return render_template("no_upcoming.html"), HTTPStatus.NOT_FOUND

    return app
