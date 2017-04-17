#!/usr/bin/python
from flask import Flask, render_template, request
import json
import re

app = Flask(__name__)

with open("state_related/states.txt") as g:
    states=[line.strip() for line in g]
with open("state_related/most_sig.js") as g:
    most_sig = json.loads(g.read())
with open("state_related/stem2tokens.js") as g:
    stem2tokens = json.loads(g.read())


@app.route("/")
def homepage():
    #Return the index page
    return render_template("index.html")

@app.route("/responder")
def response():
    #Get the message from the client
    message = str(request.args.get("message"))
    #If the client sends over a state,
    #Respond with the right message
    for state in states:
        if state.lower() == message.lower():
            #Right now, we just return whatever the second most
            #important word on that state's page is
            return stem2tokens[most_sig[state][1]][0]
    return message

if __name__ == "__main__":
    app.run(debug=True)
