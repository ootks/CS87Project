# Implements tf-idf algorithm (term frequency–inverse document frequency)

import re, math

# Returns dictionary indicating number of occurences of each unique word.
def to_word_table(text):
    # Split the text by spaces
    words = re.split(" ", text)
    words_table = dict()
    # Count the occurence of each word
    for word in words:
        c = words_table.get(word, 0)
        words_table[word] = c + 1
    # Return the dictionary 
    return words_table


# Computes the relative importance of a word in a list of sentences,
# with a higher value indicating greater importance.
# 
# bags: the set of sentences
# word: the word (contained in bags) for which we desire to calculate
#        the importance
def word_idf(bags, word):
    return math.log(sum([word in bag for bag in bags])/float(len(bags)))

# Calculate the relative importance of each word in "bags", which is
# a list of sentences.
def idfs(bags):
    idf = dict()
    for bag in bags: 
        for word in bag.split(): # @Kevin: made a change to bag.split()
            if word not in idf:
                idf[word] = word_idf(bags, word)
    return idf
            
############################################################
# EXAMPLE USAGE:
############################################################

# # Prints {'world': 1, 'hello': 1} to indicate 1 "hello", 1 "world"
# print(to_word_table("hello world"))
# # Prints -0.6931471805599453
# print(word_idf(["hello world", "hello man"], "man"))
# # Prints 0.0; "hello" is more important than "man"
# print(word_idf(["hello world", "hello man"], "hello"))
# # Calculates importance of all words in the sentences.
# print(idfs(["hello world", "hello darkness my old friend", "hello friend"]))

