from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this code is updated locally and updated on Azure DevOps Repo!"

