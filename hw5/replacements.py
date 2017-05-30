import nltk
import random
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn

#Produces an synonym for the given word
def synonym(word):
    wrd = wn.synsets(word)
    candidates = list(filter(lambda x: x.name().split('.')[0] != word.lower(), wn.synsets(word)))
    if candidates:
        return random.choice(candidates).name().split('.')[0]
    return word

#Produces an antonym for the given word
def antonym(word):
    for s in wn.synsets(word):
        for l in s.lemmas():
            for a in l.antonyms():
                return a.name().split('.')[0]
    return word

#Produces an hyponym for the given word
def hyponym(word):
    for s in wn.synsets(word):
        for l in s.lemmas():
            for a in l.hypernyms():
                return a.name().split('.')[0]
    return word

#Produces an hypernym for the given word
def hypernym(word):
    for s in wn.synsets(word):
        for l in s.lemmas():
            for a in l.hyponyms():
                return a.name().split('.')[0]
    return word

def get_neg_paragraph(pos_tagged_text):
    def change_wrd(tagged_wrd):
        # only change adjectives or nouns
        new_wrd = tagged_wrd[0]
        if tagged_wrd[1] == 'NN' or tagged_wrd[1] == 'NNS':
            new_wrd = antonym(tagged_wrd[0])
        elif tagged_wrd[1] == 'JJ':
            new_wrd = antonym(tagged_wrd[0])
        return new_wrd

    return list(map(change_wrd, pos_tagged_text))


def get_pos_paragraph(pos_tagged_text):
    def change_wrd(tagged_wrd):
        # only change adjectives or nouns
        new_wrd = tagged_wrd[0]
        if tagged_wrd[1] == 'NN' or tagged_wrd[1] == 'NNS':
            new_wrd = synonym(tagged_wrd[0])
        elif tagged_wrd[1] == 'JJ':
            new_wrd = synonym(tagged_wrd[0])
        return new_wrd

    return list(map(change_wrd, pos_tagged_text))

def produce(parag):
    '''
    Takes in a paragraph of text (as a string), returns list of two paragraphs, one positive,
    one negative.
    '''
    text = nltk.word_tokenize(parag)
    text = nltk.pos_tag(text)
    pos_para = get_pos_paragraph(text)
    neg_para = get_neg_paragraph(text)
    # now we have a pos_tagged_text to concatentate back to a paragraph
    pos_string = ' '.join(pos_para).replace(' ,', ',').replace(' .', '.').replace(" '", "'").replace(" !", "!").replace(" ;", ";")
    neg_string = ' '.join(neg_para).replace(' ,', ',').replace(' .', '.').replace(" '", "'").replace(" !", "!").replace(" ;", ";")
    return [pos_string, neg_string]


with open("anna.txt") as file:
    og = file.read().replace('\n', ' ')
    print('Original text:\n', og)
    new_text = produce(og)
    print('Positive text:\n', new_text[0])
    print('Negative text:\n', new_text[1])

























