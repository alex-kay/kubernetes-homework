from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    return subprocess.getoutput("/usr/games/fortune")