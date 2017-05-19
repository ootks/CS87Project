import os, sys
import pickle
import scraper
from sklearn.preprocessing import LabelEncoder
# Pad a line of text up to line_len characters. If a line is too long, then 
# it will be truncated to line_len characters instead.
def pad_line(line_len, pad_char, line):
    if len(line) < line_len:
        return line + [pad_char] * (line_len - len(line))
    else:
        return line[:line_len]

# Return a text as a list of lines from top_[num_posts]_posts.txt
def load_text(num_posts):
    filename = os.path.join(scraper.scraped_path, 'top_%d_posts.txt' % num_posts)
    return [list(line) for line in open(filename)]

# Creates a LabelEncoder which maps each character in the text into a unique
# integer, such that the Keras RNN can process it.
# Returns: (corpus, transformed_text)
#   corpus: LabelEncoder which specifies mapping between characters and integers
#   transformed_text: text in which all characters have been replaced with integers
def encode_text(text, line_len):
    padded_text = list(map(lambda l : pad_line(line_len, '\n', l), text))
    chars = set([char for line in padded_text for char in line])
    corpus = LabelEncoder()
    corpus.fit(list(chars))
    return corpus, list(map(corpus.transform, padded_text))


text = load_text(100)
print("Total characters:", sum(map(len, text)))
corpus, encoded_text = encode_text(text, 250)

with open("corpus.pkl", 'wb') as f:
    pickle.dump(corpus, f)
