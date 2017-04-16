import re
import wikipedia
import html2text
from bs4 import BeautifulSoup
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
porter = nltk.PorterStemmer()
stem2tokens = dict()
for state in states:
    with open('states/' + re.sub(" ", "_", state).lower() + ".txt", 'w') as g:
        print("Getting article for " + state)
        # Only use disambiguation if needed
        try:
            page = wikipedia.page(state)
        except Exception as e:
            #If there is a keyboard interrupt, stop
            if type(e) == KeyboardInterrupt:
                exit()
            page = wikipedia.page(state + " (U.S. state)")
        #Remove all non alpha-numeric characters
        content = re.sub("[^a-zA-Z0-9 ]+", " ", page.content)
        #Tokenize
        tokens = nltk.word_tokenize(content)
        #Stem all of the words
        tokens = [stem(t, stem2tokens) for t in tokens]
        print("Got page for " + page.title)
        g.write(' '.join(tokens))

#Write the list of stems to a file
stem2tokens = {key : list(value) for key, value in stem2tokens.items()}
with open("stem2tokens.js", 'w') as f:
    f.write(json.dumps(stem2tokens, indent = 4, separators = (',', ': ')))
