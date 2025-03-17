# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import requests
import os
import subprocess
import threading

app = Flask(__name__)

GITHUB_PAT = os.getenv("GITHUB_PAT")  # Store GitHub Token in ENV variable
REPO_OWNER = "AlphaNOVA23"
REPO_NAME = "chatops-demo"

@app.route("/", methods=["GET"])
def home():
    return "Slack Listener is Running!"

@app.route("/slack", methods=["POST"])
def slack_command():
    data = request.form
    if data.get("command") == "/deploy":
        trigger_github_action()
        return jsonify({"text": "Deployment triggered from Slack!"})
    
    elif data.get("command") == "/test":
        threading.Thread(target=run_selenium_test).start()
        return jsonify({"text": "Running test in the background. Results will be sent shortly!"})  # Instant response   
    
    else:
        return jsonify({"text": "Unknown command!"})

def trigger_github_action():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/deploy.yml/dispatches"
    headers = {"Authorization": f"token {GITHUB_PAT}", "Accept": "application/vnd.github.v3+json"}
    data = {"ref": "main"}
    requests.post(url, headers=headers, json=data)

def run_selenium_test():
    """ Runs the Selenium test script and returns the output """
    try:
        result = subprocess.run(["python", "selenium_test.py"], capture_output=True, text=True, encoding="utf-8")

        print(f"STDOUT: {result.stdout.strip()}")
        print(f"STDERR: {result.stderr.strip()}")

        if result.stdout.strip():
            send_slack_message(result.stdout.strip())  # Send results to Slack
        else:
            send_slack_message(f"No output received! STDERR: {result.stderr.strip()}")  # Debug stderr

    except Exception as e:
        send_slack_message(f"Error: {str(e)}")

def send_slack_message(message):
    SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")  # Store this in env variables
    if SLACK_WEBHOOK_URL:
        requests.post(SLACK_WEBHOOK_URL, json={"text": message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
