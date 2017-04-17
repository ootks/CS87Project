import math
import string

###############################################################################################
# C A U T I O N - C A U T I O N - C A U T I O N - C A U T I O N - C A U T I O N - C A U T I O N 
# "corpus" = list of strings, each string is a sentence
# "sentence" = a string that is multiple words(such as "this is a line in a poem")
# "word" = a string that is one word only (use "term" when "word" is already in use)
# Finally, use the order "corpus -> sentence -> word" (biggest to smallest), whenever relevant.
###############################################################################################

def cosine_similarity(tfidf_dict, sentence1, sentence2):
    '''
    Returns the cosine similarity of two vectors representing two sentences
    tfidf_dict maps (sentence, word) -> importance
    sentence1, sentence2 are multi-word strings
    '''

    # Cleanse sentences of punctuation and extraneous whitespace, then convert to lists
    translator = str.maketrans('','', string.punctuation)
    sentence1 = sentence1.translate(translator).strip().lower()
    sentence2 = sentence2.translate(translator).strip().lower()

    # Store each sentence as a set for iteration
    set_sen1 = set(sentence1.split())
    set_sen2 = set(sentence2.split())

    similarity = 0
    # We only care about words that are in BOTH sentences, because we'd multiply a value by 0 
    # if the word was in only one sentence, and this is a summation of those values.
    dot_product = sum([tfidf_dict[sentence1, word] * tfidf_dict[sentence2, word] for word in set_sen1 if word in set_sen2])
    magnitude1 = math.sqrt(sum([tfidf_dict[sentence1, word] ** 2 for word in set_sen1]))
    magnitude2 = math.sqrt(sum([tfidf_dict[sentence2, word] ** 2 for word in set_sen2]))
    similarity = dot_product/(magnitude1 * magnitude2)
    return similarity



###############################################################################################
# EXAMPLE USAGE / TESTS, DO NOT DELETE
###############################################################################################
# test_sentence1 = 'hello hello world'
# test_sentence2 = 'hello jello world'
# test_sentence3 = "let's go to tommy's"

# from tf_idf_claire import get_tfidf_dict
# test_tfidf_dict = get_tfidf_dict([test_sentence1, test_sentence2, test_sentence3])

# # Compare 'hello hello world' to 'hello jello'
# print(cosine_similarity(test_tfidf_dict, test_sentence1, test_sentence2))

# # Compare 'hello hello world' to "let's go to tommy's"
# print(cosine_similarity(test_tfidf_dict, test_sentence1, test_sentence3))


