#!/usr/bin/python
from flask import Flask, render_template, request
import json
import re
import sys
import os
import CFG.cfg as parseCFG

app = Flask(__name__)

@app.route("/")
def homepage():
    """Render the homepage"""
    return render_template("index.html")

@app.route("/cfg")
def cfg():
    """Return the markov story page"""
    return render_template("cfg.html")

@app.route("/new_cfg")
def new_cfg():
    text = request.args.get("cfg")
    cfg = parseCFG.text_to_cfg(text)
    return parseCFG.cfg_to_string(cfg)

if __name__ == "__main__":
    app.run(debug=True)
