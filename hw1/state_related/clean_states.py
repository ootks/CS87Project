import re, json
import parse

states=[line.strip() for line in open("states.txt")]

stem2tokens = dict()

for state in states:
    with open('states/' + re.sub(" ", "_", state).lower() + ".txt", 'w') as f, open('states_wiki/' + re.sub(" ", "_", state).lower() + ".txt") as g:
        f.write(parse.clean_text(g.read(), stem2tokens))

#Write the list of stems to a file
stem2tokens = {key : list(value) for key, value in stem2tokens.items()}
with open("stem2tokens.js", 'w') as f:
    f.write(json.dumps(stem2tokens, indent = 4, separators = (',', ': ')))

