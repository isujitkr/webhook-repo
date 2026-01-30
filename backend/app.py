import os
from flask import Flask, jsonify
from flask_cors import CORS
from config import setup_logging
from routes.webhook_routes import webhook_bp

def create_app():
    setup_logging()

    app = Flask(__name__)
    CORS(app)
    
    @app.route("/", methods=["GET"])
    def root():
        return "Api is working...", 200

    app.register_blueprint(webhook_bp, url_prefix="/api")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
    host="0.0.0.0",
    port=int(os.getenv("PORT", 4000)),
    debug=True,
)
