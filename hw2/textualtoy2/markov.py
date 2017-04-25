import random, sys

def make_model(text, n):
    """
        Creates a Markov model for the text with memory n
    """
    #Model is a dictionary mapping ngrams
    #to dictionaries, represent the counts of the 
    #following ngram.
    model = dict()
    for i in range(len(text) - n + 1):
        #Current ngram
        curr = text[i:i+n]
        #Next ngram
        nex = text[i+1:i+n+1]
        if curr not in model:
            model[curr] = dict()
        if nex not in model[curr]:
            model[curr][nex] = 1
        else:
            model[curr][nex] += 1
    if text[-n:] not in model:
        model[text[-n:]] = dict()
    if text[:n] not in model[curr]:
        model[text[-n:]][text[:n]] = 1
    else:
        model[text[-n:]][text[:n]] += 1
    #Normalize the model
    for ngram in model:
        normalization = sum(model[ngram].values())
        model[ngram] = {key : val/float(normalization)
                        for key, val in model[ngram].items()}
    return model

def next_ngram(model, curr):
    """
        Generates a new ngram, given a model and a current ngram
    """
    if curr not in model:
        raise Exception
    choices = model[curr]
    r_num = random.random()
    
    curr_sum = 0
    for choice in choices:
        curr_sum += choices[choice]
        if curr_sum > r_num:
            return choice
    return choices[0]

def next_sentence(model, curr):
    """
        Get an entire sentence from the current model
    """
    sentence = list(curr)

    curr = next_ngram(model, curr)
    while curr[-1] != '.':
        sentence.append(curr[-1])
        curr = next_ngram(model, curr)

    return ''.join(sentence)

def random_seed(text, n):
    """Get a random seed of length n from text"""
    index = random.randint(0, len(text)-3)
    return text[index: index+3]

#Test script, only runs if called as main
if __name__ == '__main__':
    text = """Whose woods these are I think I know.  His house is in the village, though; He will not see me stopping here To watch his woods fill up with snow.  My little horse must think it queer To stop without a farmhouse near Between the woods and frozen lake The darkest evening of the year.  He gives his harness bells a shake To ask if there is some mistake.  The only other sounds the sweep Of easy wind and downy flake.  The woods are lovely, dark, and deep, But I have promises to keep, And miles to go before I sleep, And miles to go before I sleep.""".lower()

    random.seed()

    model = make_model(text, 3)
    for i in range(5):
        curr = random_seed(text, 3)
        nex = next_sentence(model, curr)
        print(nex + ".")
