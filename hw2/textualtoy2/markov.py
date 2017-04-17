import random, sys

def make_model(text, n):
    """
        Creates a Markov model for the text with memory n
    """
    model = dict()
    for i in range(len(text) - n):
        curr = text[i:i+n]
        nex = text[i+1:i+n+1]
        if text[i:i+n] not in model:
            model[curr] = dict()
        if nex not in model[curr]:
            model[curr][nex] = 1
        else:
            model[curr][nex] += 1
    #Normalize the model
    for ngram in model:
        normalization = sum(model[ngram].values())
        model[ngram] = {key : val/float(normalization)
                        for key, val in model[ngram].items()}
    return model

def get_next(model, curr):
    if curr not in model:
        raise Exception
    choices = model[curr]
    r_num = random.random()
    
    curr_sum = 0
    for choice in choices:
        curr_sum += choices[choice]
    if curr_sum > r_num:
        return choice


text = """Whose woods these are I think I know.  His house is in the village, though; He will not see me stopping here To watch his woods fill up with snow.  My little horse must think it queer To stop without a farmhouse near Between the woods and frozen lake The darkest evening of the year.  He gives his harness bells a shake To ask if there is some mistake.  The only other sounds the sweep Of easy wind and downy flake.  The woods are lovely, dark, and deep, But I have promises to keep, And miles to go before I sleep, And miles to go before I sleep.""".lower()

random.seed()

model = make_model(text, 4)
curr = "wood"
sys.stdout.write(curr)
for i in range(1000):
    nex = get_next(model, curr)
    sys.stdout.write(nex[-1])
    curr = nex

