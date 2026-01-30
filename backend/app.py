from flask import Flask
from flask_cors import CORS
from config import setup_logging
from routes.webhook_routes import webhook_bp

def create_app():
    setup_logging()

    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(webhook_bp, url_prefix="/api")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
