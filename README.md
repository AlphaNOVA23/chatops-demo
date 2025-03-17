# ChatOps with Slack and GitHub Actions

## Overview

This project integrates Slack with GitHub Actions to create a seamless **ChatOps workflow**. It allows triggering tests, deployments, and receiving notifications directly within Slack.

## Features

- **Trigger GitHub Actions via Slack** (`/deploy`, `/test` commands)
- **Run Selenium-based automated tests** from Slack
- **Receive Slack notifications for repository events** (pushes, pull requests, workflow status)
- **Automated deployment workflow** using GitHub Actions

## Setup Guide

### 1. Slack App Setup

- Create a Slack App and enable **Incoming Webhooks**.
- Obtain a **Slack Webhook URL** to send notifications.
- Register a **Slash Command** (e.g., `/deploy`, `/test`) to interact with GitHub Actions.

### 2. GitHub Repository Setup

- Store **GitHub Personal Access Token (PAT)** securely in repository secrets.
- Configure GitHub Actions workflows to handle deployments and test execution.
- Add a GitHub Webhook to notify Slack of repository events.

### 3. Running Selenium Tests from Slack

- Slack `/test` command triggers an automated Selenium test.
- Test execution is handled via a Python script using the Selenium WebDriver.
- Results are posted back to Slack.

### 4. Handling GitHub Events

- GitHub Webhooks notify Slack on repository activities.
- Slack receives notifications for:
  - **Pushes** (new commits)
  - **Pull Requests** (opened, merged)
  - **Workflow Runs** (success/failure)
- GitHub Actions workflow is set up to send Slack messages upon deployment success or failure.

### 5. Testing the Integration

- Run `/deploy` in Slack to trigger a deployment.
- Run `/test` to initiate Selenium tests.
- Push commits, create PRs, and observe Slack notifications.

## Notes

- All API tokens and secrets should be securely stored in **environment variables** or GitHub **repository secrets**.
- Ensure that required dependencies (Selenium, Flask, Requests) are installed before execution.

## Future Enhancements

- Extend support for additional Slack commands.
- Implement role-based access control for Slack commands.
- Automate rollback in case of deployment failure.
