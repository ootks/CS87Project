import nltk
import random
import os
import json
from nltk.corpus import gutenberg
from nltk.corpus import cmudict

states = [  [('a', 'DT'), ('b', 'JJ'), ('c', 'NN')],
            [('d', 'VBG'), ('e', 'NN')],
            [('f', 'IN'), ('g', 'NN')]
         ]

# Generate dictionary of words and POS from Alice in Wonderland corpus
def generate_dictionary():
    alice = gutenberg.sents('carroll-alice.txt')
    tagged = [nltk.pos_tag(sent) for sent in alice]
    states_flattened = [state for sent in states for state in sent]
    word_dict = {state : [] for state in states_flattened}
    for sent in tagged:
        for word, pos in sent:
            state = word[0].lower(), pos
            if state in states_flattened and word.lower() not in word_dict[state]:
                word_dict[state].append(word.lower())
    return word_dict

state_words = generate_dictionary()

def generate_poem():
    poem = []
    for sent in states:
        line = ' '.join([random.choice(state_words[state]).capitalize() for state in sent])
        line = line[0].upper() + line[1:]
        poem.append(line)
    return '\n'.join(poem)
