#!/usr/bin/python
from flask import Flask, render_template, request
import json
import re
import sys
import os
import textualtoy2.markov as markov
import textualtoy3.hmm as hmm

app = Flask(__name__)

@app.route("/")
def homepage():
    """Render the homepage"""
    return render_template("index.html")
@app.route("/tt2")
def markov_story():
    """Return the markov story page"""
    return render_template("markovstory.html")
@app.route("/new_sentence")
def new_sentence():
    """Generates a new sentence for the markov story"""
    #Get the arguments from the get request
    seed = str(request.args.get("seed"))
    message = str(request.args.get("message"))
    try:
        size = int(request.args.get("n"))
    except ValueError:
        size = len(seed)

    #Generate the markov model
    model = markov.make_model(message, size)

    #Return a json dictionary, containing the next seed and sentence
    return json.dumps({"seed":markov.random_seed(message, size), "next_sentence":markov.next_sentence(model, seed)})

@app.route("/tt3")
def hmm_poem():
    """Return the markov story page"""
    return render_template("hmm_poem.html")
@app.route("/new_hmm_poem")
def new_hmm_poem():
    """Generates a new poem from the hmm"""
    #Return a json dictionary, containing the next seed and sentence
    return re.sub("\n", "<br>", hmm.generate_poem())

if __name__ == "__main__":
    app.run(debug=True)
