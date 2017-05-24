import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn

#Produces an synonym for the given word
def synonym(word):
    wrd = wn.synsets(word)
    new_wrd = wrd.synonyms()[1]
    return new_wrd.name().split('.')[0]

#Produces an antonym for the given word
def antonym(word):
    wrd = wn.synset(word).lemmas()[0] # for antonyms only
    new_wrd = wrd.antonyms()[0]
    return new_wrd.name().split('.')[0]

#Produces an hyponym for the given word
def hyponym(word):
    wrd = wn.synset(word)
    new_wrd = wrd.hyponyms()[0]
    return new_wrd.name().split('.')[0]

#Produces an hypernym for the given word
def hyponym(word):
    wrd = wn.synset(word)
    new_wrd = wrd.hypernyms()[0]
    return new_wrd.name().split('.')[0]

def get_neg_paragraph(pos_tagged_text):
    for tagged_wrd in pos_tagged_text:
        # only change adjectives or nouns 
        if tagged_wrd[1] == 'NN' or tagged_wrd[1] == 'NNS':

        elif tagged_wrd[1] == 'JJ':
            new_wrd = synonym()
    pass

def get_pos_paragraph(pos_tagged_text):
    pass

def produce(parag):
    '''
    Takes in a paragraph of text (as a string), returns list of two paragraphs, one positive,
    one negative.
    '''
    text = nltk.word_tokenize(parag)
    text = nltk.pos_tag(text)
    print(text)
    return [get_pos_paragraph(text), get_neg_paragraph(text)]


with open("anna.txt") as file:
    og = file.read().replace('\n', ' ')
    print(og)
    print(produce(og))

























