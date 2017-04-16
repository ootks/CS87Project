import re
import json
from tf_idf import * 

states=[line.strip() for line in open("states.txt")]

state_bags = dict()

#Turn all of the state data into bags
for state in states:
    with open('states/' + re.sub(" ", "_", state).lower() + ".txt") as g:
        state_bags[state] = text2bag(g.read())

idfs = bags2idfs(state_bags)
tf_idfs = dict()

for state in states:
    tf_idfs[state] = bag2tfidfs(state_bags[state], idfs)

#For each state, we take the top 4 most significant words 
#according to their tf_idfs
most_sig = dict()
for state in states:
    curr = tf_idfs[state]
    most_sig[state] = sorted(curr.keys(), key=lambda x:curr[x])[:4]

#Write the most significant words to a json file
with open("most_sig.js", 'w') as f:
    f.write(json.dumps(most_sig, indent = 4, separators = (',', ': ')))
