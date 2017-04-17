# Functions as a "textual toy" for part 3 of homework 1.

import random # Used to randomize sentence-padding & sentence selection.
from tf_idf import * # Contains tf-idf implementation

# This constant indicates the minimum number of sentences as input.
# If input is below this minimum, we pad with random Simon & Garfunkel lyrics
# in simon_and_garfunkel.txt
minimum_length = 20 # sentences

# We cannot randomly select a sentence ranked below this constant in importance.
# Ex: If this constant is 5, we cannot select the 6th most important sentence.
# This number is used in *all* sentence selections, and so functions as a 
# general "entropy" constant.
importance_rank = 5

def make_story(user_input):
	'''
	Input: A text made out of sentences, in the form of a list of strings.
	Output: A 3-line short story / poem.
	Techniques: Cosine Similarity, TF-IDF.

	Two out of the three lines should be taken from the original text.
	One line may be (totally or partially) fixed (from a prearranged list of at least 3 lines), 
	but the three lines should represent some sort of similarity (in pairs).
	'''

	# Story will contain the 3-line output.
	story = ""

	# Pad with sentences from simon_and_garfunkel.txt if not sufficiently long
	deficit = minimum_length - len(user_input)
	if (deficit > 0):
		user_input.extend(get_padding(deficit))


	# 1. Randomly pick one of the 3 most important sentences- output it.
	first_sentence = get_first_sentence(importance_rank, user_input)
	story += first_sentence

	# 2. Output the most similar sentence in dickinson_first_lines.txt
	dickinson_sentence = get_dickinson_sentence(importance_rank, first_sentence, "dickinson.txt")
	story += dickinson_sentence

	# 3. Pick a similar sentence to the dickinson line, output that.
	story += get_second_sentence(importance_rank, dickinson_sentence, user_input)

	return story

############################################################
# HELPER FUNCTIONS FOR make_story():
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

	with open(filename) as file:
		new_lines = random.sample(file.readlines(), number_sentences)

	return new_lines


def get_first_sentence(rank, source):
	'''
	Gets a sentence within the "rank"-most importance sentences.
	Source variable is a list of strings.
	'''
	sentence = ""

	# Sort sentences in user input by importance rank
	source = sorted(source, key=lambda x: sum(map(importance, x.split())))

	# Return a sentence at random from the top-ranked, using rank variable.
	return random.choice(source[0:rank])

def get_dickinson_sentence(rank, prev_sentence, filename='dickinson.txt'):
	'''
	Gets a sentence that was similar to the previous sentence, prev_sentence.
	Sources sentences from filename.
	'''
	sentence = ""
	dickinson_lines = []

	# Turn dickinson.txt into a list of strings.
	with open(filename) as file:
    	dickinson_lines = file.readlines()

	# Sort sentences by similarity to prev_sentence


	# Pick one of the top-ranked similar sentences.

	return random.choice(dickinson_lines[0:rank])

def get_second_sentence(rank, prev_sentence, source):
	'''
	Gets a sentence that was similar to the previous sentence, prev_sentence.
	Source variable is a list of strings.
	'''
	sentence = ""

	# Sort sentences by similarity to prev_sentence

	# Pick one of the top-ranked similar sentences.

	return return random.choice(source[0:rank])



############################################################
# EXAMPLE USAGE:
############################################################

# # Prints 10 random lines from simon_and_garfunkel.txt
# print(get_padding(19))
# # Makes the story.


