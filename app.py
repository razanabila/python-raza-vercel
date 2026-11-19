from flask import Flask

app = Flask(__main__)
@app.route("/")
def home():
  return "<h1>Hello world!</h1>"

app.run()
