from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/responder")
def response():
    return "asdasdas"

if __name__ == "__main__":
    app.run()
