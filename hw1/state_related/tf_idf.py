#Implements tf-idf algorithm
#Writes all of the tf-idf data to state_tf_idfs.js
import re, math, json

def text2bag(text):
    """
    Converts text to a bag of words (dictionary: words -> counts)
    """
    words = re.split(" +", text)
    words_table = dict()
    for word in words:
        if word == "":
            continue
        #Increment count of each word
        if word not in words_table:
            words_table[word] = 1
        else:
            words_table[word] = words_table[word] + 1
    return words_table

def word_idf(bags, word):
    """
    Gets the idf for word with respect to the corpus (bags)
    """
    #Return Log(#bags containing word / #number of bags)
    return math.log(sum([word in bag for bag in bags.values()])/float(len(bags)))

def bags2idfs(bags):
    """
    Gets the idfs for all of the words in bags
    where bags is a dictionary, whose values 
    are bags
    """
    idf = dict()
    for bag in bags.values():
        for word in bag:
            if word not in idf:
                idf[word] = word_idf(bags, word)
    return idf

def bag2tfidfs(bag, idfs):
    """
    Gets the tf_idfs for the specified bag
    """
    tfidf = dict()
    for word in bag:
        tfidf[word] = idfs[word] * bag[word]
    return tfidf

def bags2tfidfs(bags):
    idfs = bags2idfs(bags)
    return {key: bag2tfidfs(val, idfs) for key, val in bags.items()}

if __name__ == '__main__':
    states=[line.strip() for line in open("states.txt")]

    state_bags = dict()

    #Turn all of the state data into bags
    for state in states:
        with open('states/' + re.sub(" ", "_", state).lower() + ".txt") as g:
            state_bags[state] = text2bag(g.read())

    idfs = bags2idfs(state_bags)
    tf_idfs = dict()

    for state in states:
        tf_idfs[state] = bag2tfidfs(state_bags[state], idfs)

    with open("state_tf_idfs.js", 'w') as g:
        g.write(json.dumps(tf_idfs, indent = 4, separators = (',', ': ')))
