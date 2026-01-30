from flask import Blueprint
from controllers.webhook_controller import handle_webhook, get_events

webhook_bp = Blueprint("webhook", __name__)

webhook_bp.route("/webhook", methods=["POST"])(handle_webhook)
webhook_bp.route("/events", methods=["GET"])(get_events)
