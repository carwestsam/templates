from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "hello world!"

# pip install Flask
# FLASK_APP=simple.py flask run --host=0.0.0.0