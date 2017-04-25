# Functions as a "textual toy" for part 3 of homework 1.

import random # Used to randomize sentence-padding & sentence selection.
from textualtoy1.tf_idf_claire import *
from textualtoy1.cosine_similarity_claire import *
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) + '/'

###############################################################################################
# C A U T I O N - C A U T I O N - C A U T I O N - C A U T I O N - C A U T I O N - C A U T I O N 
# "corpus" = list of strings, each string is a sentence
# "sentence" = a string that is multiple words(such as "this is a line in a poem")
# "word" = a string that is one word only (use "term" when "word" is already in use)
# Finally, use the order "corpus -> sentence -> word" (biggest to smallest), whenever relevant.
###############################################################################################

def get_poem(user_corpus, min_length=20, max_rank=3):
    '''
    Input: A text made out of sentences, in the form of a list of strings.
    Output: A 3-line short story / poem.
    Techniques: Cosine Similarity, TF-IDF.
    
    MIN_LENGTH CONSTANT:
    This constant indicates the minimum number of sentences as input.
    If input is below this minimum, we pad with random Simon & Garfunkel lyrics
    in simon_and_garfunkel.txt

    MAX_RANK CONSTANT:
    We cannot randomly select a sentence ranked below this constant in importance.
    This number is used in *all* sentence selections, and so functions as a 
    general "entropy" constant.
    This number should NEVER be greater than 'min_length' variable
    Ex: If this constant is 5, we cannot select the 6th most important sentence.
    '''

    # Confirm that user has not failed to read comments
    if type(user_corpus) is not list:
        return -1
    if max_rank >= min_length:
        return -1

    # 'story' will contain the 3-line poem we are generating.
    story = ""

    # Pad with sentences from simon_and_garfunkel.txt if not 
    # 'user_corpus' does not have enough sentences
    deficit = min_length - len(user_corpus)
    if (deficit > 0):
        user_corpus.extend(get_padding(deficit))

    # Create a tfidf_dict that contains mappings for "dickinson.txt" as well as user_corpus
    dickinson_corpus = get_parsed_dickinson_list()
    combined_corpus = user_corpus + dickinson_corpus
    combined_tfidf_dict = get_tfidf_dict(combined_corpus)

    ###
    # 1. Randomly pick one of the most important sentences- output it.
    ###
    line1 = get_important_sentence(max_rank, user_corpus)
    story += line1

    ###
    # 2. Output the most similar sentence in dickinson_first_lines.txt (comparing to sentence 1)
    ###
    line2 = get_similar_sentence(max_rank, line1, dickinson_corpus, combined_tfidf_dict)
    story += line2

    ###
    # 3. Pick a similar sentence to the dickinson line from the user_corpus, output that.
    ###
    line3 = get_similar_sentence(max_rank, line2, user_corpus, combined_tfidf_dict)
    # Make sure you don't pick the same first & last sentence.
    while line3 == line1:
        line3 = get_similar_sentence(max_rank, line2, user_corpus, combined_tfidf_dict)
    story += line3

    return story

############################################################
# HELPER FUNCTIONS FOR get_poem():
############################################################

def get_padding(number_sentences, filename='simon_and_garfunkel.txt'):
    '''
    Returns "number_sentences"-length list of random sentences from 
    Simon & Garfunkel lyrics, found in "simon_and_garfunkel.txt".
    '''
    new_lines = []

    # No padding required. This shouldn't ever be tripped.
    if number_sentences <= 0:
        return []

    with open(dir_path + filename) as file:
        new_lines = random.sample(file.readlines(), number_sentences)

    return new_lines


def get_important_sentence(max_rank, source):
    '''
    Gets a sentence within the "rank"-most importance sentences.
    Source variable is a list of strings.
    '''
    sentence = ""

    # Returns dictionary pointing sentences to importance
    tfidf_dict = get_sentence_tfidf_dict(source)

    # Sort sentences in user input by importance rank
    ranked_sentence_list = sorted(tfidf_dict, key=tfidf_dict.get, reverse=True)

    # Return a sentence at random from the top-ranked, using rank variable.
    return random.choice(ranked_sentence_list[0:max_rank])

def get_similar_sentence(max_rank, prev_sentence, user_list, combined_tfidf_dict):
    '''
    Gets a sentence that was similar to the previous sentence, prev_sentence.
    '''
    # Sort sentences by similarity to prev_sentence
    ranked_user_list = sorted(user_list, key=lambda sent: cosine_similarity(combined_tfidf_dict, sent, prev_sentence), reverse=True)

    # Pick one of the top-ranked similar sentences.
    return random.choice(ranked_user_list[0:max_rank])

def get_parsed_dickinson_list(filename='dickinson.txt'):
    '''
    Returns list of sentences in dickinson.txt with punctuation, capitalization, 
    and whitespace removed. 
    '''
    dickinson_list = []

    # Turn dickinson.txt into a list of strings.
    with open(dir_path + filename) as file:
        dickinson_list = file.readlines()

    return dickinson_list


###############################################################################################
# EXAMPLE USAGE / TESTS, DO NOT DELETE
###############################################################################################
# # Prints 20 random lines from simon_and_garfunkel.txt
# print(get_padding(20))
# # Prints one of the two most important sentences in the source list.
# print(get_sentence_by_importance(2, ["hey","sentence one", "sentence sentence two", "very important sentence, please be aware of my importance"]))

# # Test get_poem()
#testfile = "silverstein.txt"
#with open(testfile) as file:
#    test_list = file.readlines()
#print("Poem Output:\n\n" + get_poem(test_list))
#
#
#
