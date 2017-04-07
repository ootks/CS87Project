from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    with open("index.html") as f:
        return f.read()

if __name__ == "__main__":
    app.run()
