import os
import pickle
import random
import nltk
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

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),'dict.pkl')
if os.path.isfile(filename):
    with open(filename, 'rb') as f:
        state_words = pickle.load(f)
else:
    state_words = generate_dictionary()
    with open(filename, 'wb') as f:
        pickle.dump(state_words, f)

def generate_poem():
    poem = []
    for sent in states:
        line = ' '.join([random.choice(state_words[state]) for state in sent])
        line = line[0].upper() + line[1:]
        poem.append(line)
    return '\n'.join(poem)
