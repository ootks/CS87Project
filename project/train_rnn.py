import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.layers.embeddings import Embedding
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
import scraper

def load_text(num_posts):
    filename = os.path.join(scraper.scraped_path, 'top_%d_posts.txt' % num_posts)
    return [list(line) for line in open(filename)]

# Pad a line of text up to line_len characters. If a line is too long, then 
# it will be truncated to line_len characters instead.
def pad_line(line_len, pad_char, line):
    if len(line) < line_len:
        return line + [pad_char] * (line_len - len(line))
    else:
        return line[:line_len]

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

def generate_input_output(encoded_text, seq_len):
    line_len = len(encoded_text[0])
    num_lines = len(encoded_text)
    seqs_per_line = line_len - seq_len
    X = np.zeros((num_lines * seqs_per_line, seq_len), dtype=np.int32)
    dataY = np.zeros(num_lines * seqs_per_line, dtype=np.int32)
    for l in range(num_lines):
        for i in range(line_len - seq_len):
            X[l * seqs_per_line + i] = encoded_text[l][i:i + seq_len]
            dataY[l * seqs_per_line + i] = encoded_text[l][i + seq_len]
    # One-hot encode the output variable
    y = np_utils.to_categorical(dataY)
    return X, y

text = load_text(100)
print("Total characters:", sum(map(len, text)))

corpus, encoded_text = encode_text(text, 250)
n_classes = len(corpus.classes_)
print("Total characters:", n_classes)

X, y = generate_input_output(encoded_text, 30)
print("Total patterns:", X.shape[0])

# Define LSTM model
model = Sequential()
model.add(Embedding(n_classes, 32))
model.add(LSTM(256, dropout=0.2, recurrent_dropout=0.2))
# model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Add checkpoints to save models at different points of training
filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

model.fit(X, y, epochs=20, batch_size=128, callbacks=callbacks_list)

