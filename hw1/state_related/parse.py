import re
import json
import nltk
porter = nltk.PorterStemmer()
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

def clean_text(text, stem2tokens):
    """Cleans (tokenizes and stems) text"""
    #Remove all non alpha-numeric characters
    content = re.sub("[^a-zA-Z0-9 ]+", " ", text)
    #Tokenize
    tokens = nltk.word_tokenize(content)
    #Stem all of the words
    tokens = [stem(t, stem2tokens) for t in tokens]
    return ' '.join(tokens)

