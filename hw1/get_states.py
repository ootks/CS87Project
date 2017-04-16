import re
import wikipedia
import html2text
from bs4 import BeautifulSoup
import nltk

states=[line.strip() for line in open("states.txt")]

h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True
h.ignore_emphasis = True
h.body_width = 0

# for state in states:
#Stemmer for getting stems
porter = nltk.PorterStemmer()
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
        tokens = [porter.stem(t) for t in tokens]
        #Make all of the words lower case
        tokens = [t.lower() for t in tokens]
        print("Got page for " + page.title)
        g.write(' '.join(tokens))
