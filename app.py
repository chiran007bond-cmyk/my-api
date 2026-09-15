from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/getCode")
def get_code():
    account_id = request.args.get("id")

    if not account_id:
        return jsonify({
            "status": "error",
            "message": "id is required"
        }), 400

    # আপনার নিজস্ব অনুমোদিত backend logic এখানে থাকবে
    return jsonify({
        "status": "success",
        "id": account_id
    })

@app.route("/")
def home():
    return "API is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
