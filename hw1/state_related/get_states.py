import re
import wikipedia
import html2text
import nltk
import json

states=[line.strip() for line in open("states.txt")]

h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True
h.ignore_emphasis = True
h.body_width = 0

def stem(token, stem_list):
    """
        Takes in a token, and a dictionary mapping stems to possible tokens
        and returns the stemmed version of the token, after adding the token 
        to the stem_list
    """
    stem = porter.stem(token)
    stem = stem.lower()
    if stem not in stem_list:
        stem_list[stem] = set()
    stem_list[stem].add(token)
    return stem
    

#Stemmer for getting stems
stem2tokens = dict()
for state in states:
    with open('states_wiki/' + re.sub(" ", "_", state).lower() + ".txt", 'w') as g:
        print("Getting article for " + state)
        # Only use disambiguation if needed
        try:
            page = wikipedia.page(state)
        except Exception as e:
            #If there is a keyboard interrupt, stop
            if type(e) == KeyboardInterrupt:
                exit()
            page = wikipedia.page(state + " (U.S. state)")
        g.write(page.content)
