# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

GITHUB_PAT = os.getenv("GITHUB_PAT")  # Store GitHub Token in ENV variable
REPO_OWNER = "YOUR_GITHUB_USERNAME"
REPO_NAME = "chatops-demo"

@app.route("/slack", methods=["POST"])
def slack_command():
    data = request.form
    if data.get("command") == "/deploy":
        trigger_github_action()
        return jsonify({"text": "🚀 Deployment triggered from Slack!"})
    else:
        return jsonify({"text": "❌ Unknown command!"})

def trigger_github_action():
    url = f"https://api.github.com/repos/{AlphaNOVA23}/{chatops-demo}/actions/workflows/deploy.yml/dispatches"
    headers = {"Authorization": f"token {GITHUB_PAT}", "Accept": "application/vnd.github.v3+json"}
    data = {"ref": "main"}
    requests.post(url, headers=headers, json=data)

if __name__ == "__main__":
    app.run(port=5000, debug=True)

