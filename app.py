from flask import Flask, Response
import requests
import os

app = Flask(__name__)

SOURCE_URL = os.environ.get("SOURCE_URL")


@app.route("/")
def home():
    return "API is running"


@app.route("/api/getCode")
def get_code():
    if not SOURCE_URL:
        return {
            "status": "error",
            "message": "SOURCE_URL is not configured"
        }, 500

    try:
        response = requests.get(
            SOURCE_URL,
            timeout=15
        )

        return Response(
            response.content,
            status=response.status_code,
            content_type=response.headers.get(
                "Content-Type",
                "application/json"
            )
        )

    except requests.RequestException:
        return {
            "status": "error",
            "message": "Source API request failed"
        }, 502


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
