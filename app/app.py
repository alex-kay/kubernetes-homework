from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    return subprocess.getoutput("/usr/games/fortune")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='80')