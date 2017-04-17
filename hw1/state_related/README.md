The pipeline that we're using looks like this:

1. Run get_states.py, this produces two things: text documents associated with each state, which contain tokenized, stemmed versions of their wikipedia articles, where all the words are lower case. The second thing is a dictionary (stem2tokens.js) associating to each stemmed word, a list of all of the possible words that can be stemmed to that word.

2. Run sig_words, which outputs a dictionary associating to each state a list of its most significant word.

3. Run __init__.py, which starts a server at localhost:5000, and which will respond to each message.
