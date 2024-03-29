from flask import Flask, render_template
from flask_cors import CORS

from src.consts import NOT_FOUND
from src.routes.root import mod as root_mod


# We want to be flexible with regards to trailing slashes
class RelaxedFlask(Flask):

    def add_url_rule(self, *args, **kwargs):
        if 'strict_slashes' not in kwargs:
            kwargs['strict_slashes'] = False
        super(RelaxedFlask, self).add_url_rule(*args, **kwargs)


def create_flask_app():
    app = RelaxedFlask(
        __name__,
        template_folder='../templates',
        static_folder='../static',
        static_url_path=''
    )
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app)

    app.register_blueprint(root_mod, url_prefix="/")

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), NOT_FOUND

    return app
