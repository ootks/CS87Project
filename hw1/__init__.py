#!/usr/bin/python
from flask import Flask, render_template, request
import json
import re
from state_related import tf_idf
from state_related import cosine_similarity
from state_related import parse
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/textualtoy1')
from textualtoy1 import textualtoy

app = Flask(__name__)

with open("state_related/states.txt") as g:
    states=[line.strip() for line in g]
with open("state_related/most_sig.js") as g:
    most_sig = json.loads(g.read())
with open("state_related/stem2tokens.js") as g:
    stem2tokens = json.loads(g.read())

states=[line.strip() for line in open("state_related/states.txt")]

bags = dict()

#Turn all of the state data into bags
for state in states:
    with open('state_related/states/' + re.sub(" ", "_", state).lower() + ".txt") as g:
        bags[state] = tf_idf.text2bag(g.read())

@app.route("/")
def homepage():
    return render_template("index.html")
@app.route("/chatbot")
def chatbot():
    #Return the index page
    return render_template("chatbot.html")

@app.route("/state_responder")
def state_response():
    #Get the message from the client
    message = str(request.args.get("message"))
    #If the client sends over a state,
    #Respond with the right message
    mentioned_states = get_mentioned_states(message)
    if mentioned_states:
        return ' '.join([get_response(state) for state in mentioned_states])
    
    return get_response(most_similar_state(message))

def get_mentioned_states(message):
    """Gets all of the states mentioned in message"""
    found_states = []
    lower_message = message.lower()
    for state in states:
        if lower_message.find(state.lower()) != -1:
            found_states.append(state)
    return found_states

def most_similar_state(message):
    """Finds the state most similar to the message"""
    message = parse.clean_text(message, dict())
    bags["message"] = tf_idf.text2bag(message)
    tf_idfs = tf_idf.bags2tfidfs(bags)

    max_cos = cosine_similarity.cos_sim(bags["message"], bags["Michigan"])
    candidate = "Michigan"
    for state in bags:
        if state != "message":
            cos = cosine_similarity.cos_sim(bags["message"], bags[state])
            if cos > max_cos:
                candidate = state
                max_cos = cos
    return candidate



def get_response(state):
    return "{} is all about {}, {}, and {}.".format(
            state,
            stem2tokens[most_sig[state][1]][0],
            stem2tokens[most_sig[state][2]][0],
            stem2tokens[most_sig[state][3]][0]
            )
    
@app.route("/tt1")
def tt1():
    #Get the message from the client
    return render_template("textualtoy1.html")

@app.route("/tt1_responder")
def tt1_response():
    #Get the message from the client
    message = str(request.args.get("message"))
    lines = [line for line in message.split("\n") if line != '']
    response = textualtoy.get_poem(lines)
    return re.sub("\n", "<br>", response)


if __name__ == "__main__":
    app.run(debug=True)
