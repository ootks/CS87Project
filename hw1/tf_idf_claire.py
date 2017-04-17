# Implements tf-idf algorithm (term frequency–inverse document frequency)
import string
from math import log

###############################################################################################
# C A U T I O N - C A U T I O N - C A U T I O N - C A U T I O N - C A U T I O N - C A U T I O N 
# "corpus" = list of strings, each string is a sentence
# "sentence" = a string that is multiple words(such as "this is a line in a poem")
# "word" = a string that is one word only (use "term" when "word" is already in use)
# Finally, use the order "corpus -> sentence -> word" (biggest to smallest), whenever relevant.
###############################################################################################

def tf(sentence, word):
    '''
    tf = term-frequency
    Returns word-count of word in sentence. This is just one option for calculating tf. 
    '''
    # Double-check that white-space and punctuation have been stripped
    # from both word and sentence. 
    word = word.strip() 
    translator = str.maketrans('','', string.punctuation)
    word = word.translate(translator) 
    sentence = sentence.translate(translator) 

    return sentence.split().count(word)

def idf(corpus, word):
    '''
    idf = inverse document frequency
    idf(corpus, word) = log(number of sentences / 1 + number of sentences in which word occurs)
    '''
    s = sum(word in sentence for sentence in corpus)
    if s == 0:
        return -1
    return log(len(corpus) / s)

def tfidf(corpus, sentence, word):
    '''
    How important is word in sentence with respect to corpus?
    More positive -> more important
    '''
    return tf(sentence, word) * idf(corpus, word)

def get_tfidf_dict(corpus):
    '''
    Returns dictionary pointing (sentence, word) tuple to tfidf(corpus, sentence, word)
    NOTE: maps (sentence, word) -> importance, NOT sentence -> importance
    '''
    tfidf_dict = {}
    for sentence in corpus:
        for word in set(sentence.split()): # don't repeat words in the sentence
            tfidf_dict[sentence, word] = tfidf(corpus, sentence, word)

    return tfidf_dict

def get_sentence_tfidf_dict(corpus):
    '''
    Returns dictionary pointing sentences to sum over tfidf(corpus, sentence, word)
    for each word in the sentence. 
    NOTE: maps sentence -> importance, NOT (sentence, word) -> importance
    '''
    tfidf_dict = {}
    for sentence in corpus:
        sentence_importance = 0
        for word in set(sentence.split()): # don't repeat words in the sentence
            sentence_importance += tfidf(corpus, sentence, word)
        tfidf_dict[sentence] = sentence_importance

    return tfidf_dict


###############################################################################################
# EXAMPLE USAGE, DO NOT DELETE
###############################################################################################
# # prints 2
# print("tf:\t", tf("hello jello", "jello"), "\n") 
# # prints .693
# print("idf of jello:\t",idf(["hello hello world", "hello jello"], "jello"), "\n") 
# # prints 0 because 'hello' is in every sentence in the corpus
# print("idf of hello:\t",idf(["hello hello world", "hello jello"], "hello"), "\n") 
# # prints importance of 'hello' with respect to 'hello jello' with respect to corpus
# print("tfidf:\t", tfidf(["hello hello world", "hello jello"], "hello jello", "jello"), "\n")
# # prints dictionary mapping (sentence, word) -> importance
# print("tfidf dict:\t",get_tfidf_dict(["hello hello world", "hello jello", "let's go to tommy's"]), "\n")
# # prints dictionary mapping sentence -> importance
# print("tfidf dict by sentence:\t",get_sentence_tfidf_dict(["hello hello world", "hello jello", "let's go to tommy's"]))


