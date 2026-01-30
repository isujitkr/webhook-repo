from flask import request, jsonify
from datetime import datetime
from db import events_collection

def handle_webhook():
    github_event = request.headers.get("X-GitHub-Event")
    payload = request.json
    event_data = None

    if github_event == "push":
        event_data = {
            "request_id": payload.get("after"),
            "author": payload.get("pusher", {}).get("name"),
            "action": "PUSH",
            "from_branch": None,
            "to_branch": payload.get("ref").replace("refs/heads/", ""),
            "timestamp": datetime.fromisoformat(
                payload["head_commit"]["timestamp"].replace("Z", "+00:00")
            )
        }

    elif github_event == "pull_request":
        pr = payload.get("pull_request")

        if pr.get("merged"):
            event_data = {
                "request_id": pr.get("merge_commit_sha"),
                "author": pr.get("merged_by").get("login"),
                "action": "MERGE",
                "from_branch": pr.get("head").get("ref"),
                "to_branch": pr.get("base").get("ref"),
                "timestamp": datetime.fromisoformat(
                    pr["merged_at"].replace("Z", "+00:00")
                )
            }
        else:
            event_data = {
                "request_id": pr.get("head").get("sha"),
                "author": pr.get("user").get("login"),
                "action": "PULL_REQUEST",
                "from_branch": pr.get("head").get("ref"),
                "to_branch": pr.get("base").get("ref"),
                "timestamp": datetime.fromisoformat(
                    pr["created_at"].replace("Z", "+00:00")
                )
            }

    if not event_data:
        return jsonify({"message": "Event ignored"}), 200

    events_collection.insert_one(event_data)
    return jsonify({"message": "Event stored"}), 201

def get_events():
    events = list(
        events_collection.find({})
        .sort("timestamp", -1)
        .limit(20)
    )

    for e in events:
        e["_id"] = str(e["_id"])
        e["timestamp"] = e["timestamp"].isoformat()

    return jsonify(events), 200
