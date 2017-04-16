from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/responder")
def response():
    return str(request.args.get("message"))

if __name__ == "__main__":
    app.run()
