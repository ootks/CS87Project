# Functions as a "textual toy" for part 3 of homework 1.

import random # Used to randomize sentence-padding.

# This constant indicates the minimum number of sentences as input.
# If input is below this minimum, we pad with random Simon & Garfunkel lyrics
# in simon_and_garfunkel.txt
minimum_length = 20 # sentences

# Input: A text made out of sentences, in the form of a list of strings.
# Output: A 3-line short story / poem.
# Techniques: Cosine Similarity, TF-IDF.
# Two out of the three lines should be taken from the original text.
# One line may be (totally or partially) fixed (from a prearranged list of at least 3 lines), 
# but the three lines should represent some sort of similarity (in pairs).
def make_story(user_input):
	# Story will contain the 3-line output.
	story = ""

	# Pad with sentences from simon_and_garfunkel.txt if not sufficiently long
	deficit = minimum_length - len(user_input)
	if (deficit > 0):
		user_input.extend(get_padding(deficit))

	###########################################################################
	# Output two strings from the sentence, preferably important ones.
	###########################################################################

	# 1. Randomly pick one of the 3 most important sentences- output it.



	# 3. Output the most similar sentence in dickinson_first_lines.txt

	# 2. Pick a similar sentence to the dickinson line, output that.

	return story

# Returns "number_sentences"-length list of random sentences from 
# Simon & Garfunkel lyrics, found in "simon_and_garfunkel.txt".
def get_padding(number_sentences):
	new_lines = []

	# No padding required. This shouldn't ever be tripped
	if number_sentences <= 0:
		return []

	with open('simon_and_garfunkel.txt') as file:
		new_lines = random.sample(file.readlines(), number_sentences)

	return new_lines


############################################################
# EXAMPLE USAGE:
############################################################

# # Prints 10 random lines from simon_and_garfunkel.txt
# print(get_padding(19))
# # Makes the story.


