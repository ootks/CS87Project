import os, sys
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.layers.embeddings import Embedding
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
import scraper

train = False

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

def generate_reply(model, corpus, seed):
    line = seed + '\x0b'
    while len(line) < 1000:
        x = np.reshape(corpus.transform(list(line[-30:])), (1, 30))
        prediction = model.predict(x, verbose=0)[0]
        # argmax often just results in an infinite loop in text generation,
        # so we pick the next letter with a probability distribution instead
        # in order to 
        # index = np.argmax(prediction)
        index = np.random.choice(range(len(corpus.classes_)), p=prediction)
        result = corpus.inverse_transform([index])[0]
        if result == '\n' or result == '\x0b':
            break
        line += result
    line.replace('\t', '\n')
    return line

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
# Comment out for one layer:
model.add(LSTM(256, dropout=0.2, recurrent_dropout=0.2, return_sequences=True))
model.add(LSTM(256, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(y.shape[1], activation='softmax'))

if not train:
    # filename = 'models/one_layer/weights-improvement-04-0.9329.hdf5'
    filename = 'models/two_layers/weights-improvement-62-0.7493.hdf5'
    model.load_weights(filename)

model.compile(loss='categorical_crossentropy', optimizer='adam')

if train:
    # Add checkpoints to save models at different points of training
    filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]
    model.fit(X, y, epochs=100, batch_size=1024, callbacks=callbacks_list)

print(generate_reply(model, corpus, "How are you doing today? I'm doing great!"))
