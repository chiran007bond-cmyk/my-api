from flask import Flask, request, Response
import requests

app = Flask(__name__)

SOURCE_URL = "https://pingosms.com/api/getCodefv3"


@app.route("/")
def home():
    return "API is running"


@app.route("/api/getCode")
def get_code():
    id_value = request.args.get("id")

    if not id_value:
        return {
            "status": "error",
            "message": "id is required"
        }, 400

    try:
        response = requests.get(
            SOURCE_URL,
            params={"id": id_value},
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
