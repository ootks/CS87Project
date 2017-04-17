The pipeline that we're using looks like this:

1. Run get_states.py, this produces two things: text documents associated with each state, which contain tokenized, stemmed versions of their wikipedia articles, where all the words are lower case. The second thing is a dictionary (stem2tokens.js) associating to each stemmed word, a list of all of the possible words that can be stemmed to that word.

2. Run sig_words, which outputs a dictionary associating to each state a list of its most significant word.

3. Run __init__.py, which starts a server at localhost:5000, and which will respond to each message.

======Contents=========
* clean_states.py is a utility script that takes the wikipedia pages scraped by get_states.py, removes non-alphanumeric character, stems all of the words, etc. IT writes all of these to the states folder. In addition, this outputs stem2tokens.js, a json file that maps the stems produced by the function to the words that originally produced them.
* cosine_similarity.py contains a function for computing the cosine similarity between two dictionaries mapping words to their tf_idf values
* get_states.py scrapes wikipedia pages and writes some neat output to the folder states_wiki
* sig_words.py contains a function that converts the cleaned state data in the states folder to tf_idf form, finds the top most significant g_NWORDS (set to 10) words and writes them to most_sig.js
* parse.py is contains the functions used by clean_states to clean the state data.
* tf_idf.py contains functions that take in text, converts them to a bag-of-words format (that is to say that it converts the text to a dictionary which maps each word to the corresponding count of how many times that word appears in the dictionary.)
* stem2tokens.js contains a dictionary which converts the converts the stems output by the parse function to the tokens that produced those stems, e.g. the word "Downhill" will be stemmed to become the word "downhil", and stem2tokens tells us which words originally produced which stems.
* states.txt has a list of all US states.
* most_sig.js contains a json dictionary mapping states to the 10 most significant words related to that state.
