from flask import Flask, request, jsonify
import os

app = Flask(__name__)

SOURCES = {
    "account1": os.environ.get("SOURCE_ACCOUNT1"),
    "account2": os.environ.get("SOURCE_ACCOUNT2"),
    "account3": os.environ.get("SOURCE_ACCOUNT3"),
    "account4": os.environ.get("SOURCE_ACCOUNT4"),
}


@app.route("/")
def home():
    return "API is running"


@app.route("/api/getCode")
def get_code():
    account_id = request.args.get("id")

    if not account_id:
        return jsonify({
            "status": "error",
            "message": "id is required"
        }), 400

    if account_id not in SOURCES:
        return jsonify({
            "status": "error",
            "message": "Unknown ID"
        }), 404

    if not SOURCES[account_id]:
        return jsonify({
            "status": "error",
            "message": "Source not configured"
        }), 500

    return jsonify({
        "status": "success",
        "id": account_id,
        "source_configured": True
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
