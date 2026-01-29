import os
import src

app = src.create_flask_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(
        host="0.0.0.0",
        port=port,
        debug=debug,
        use_reloader=debug
    )