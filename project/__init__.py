#!/usr/bin/python
from flask import Flask, render_template, request
import pickle
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.layers.embeddings import Embedding
import numpy as np

################################################################################
################################ Response Code #################################
################################################################################
# Pad a line of text up to line_len characters. If a line is too long, then 
# it will be truncated to line_len characters instead.
#def pad_line(line_len, pad_char, line):
#    if len(line) < line_len:
#        return line + [pad_char] * (line_len - len(line))
#    else:
#        return line[:line_len]
#
#
#def generate_reply(model, corpus, seed):
#    line = seed + '\x0b'
#    while len(line) < 1000:
#        x = np.reshape(corpus.transform(list(line[-30:])), (1, 30))
#        prediction = model.predict(x, verbose=0)[0]
#        # argmax often just results in an infinite loop in text generation,
#        # so we pick the next letter with a probability distribution instead
#        # index = np.argmax(prediction)
#        index = np.random.choice(range(len(corpus.classes_)), p=prediction)
#        result = corpus.inverse_transform([index])[0]
#        if result == '\n' or result == '\x0b':
#            break
#        line += result
#    line.replace('\t', '\n')
#    return line
#

def generate_reply(model, corpus, seed):
    line = seed + '\x0b'
    # Line needs to be of length at least 30
    if len(line) < 30:
        line = (" "*(30-len(line))) + line

    # line needs to be of length at least 30
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

################################################################################
################################## Server Code #################################
################################################################################

app = Flask(__name__)

# Homepage route
@app.route("/")
def homepage():
    return render_template("index.html")

# Route to get response
@app.route("/get_response")
def respond():
    msg = request.args.get("msg")
    reply = generate_reply(model, corpus, msg)
    print(repr(reply))
    return reply.split('\x0b')[1]


################################################################################
#################################### MAIN ######################################
################################################################################

if __name__ == '__main__':
    # Load the label encoder from the pickle
    with open("corpus.pkl", 'rb') as f:
        corpus = pickle.load(f)

    n_classes = len(corpus.classes_)

    # Define LSTM model
    model = Sequential()
    model.add(Embedding(n_classes, 32))
    model.add(LSTM(256, dropout=0.2, recurrent_dropout=0.2, return_sequences=True))
    model.add(LSTM(256, dropout=0.2, recurrent_dropout=0.2))

    # 97 is the output length?
    model.add(Dense(97, activation='softmax'))

    filename = 'models/two_layers/weights-improvement-62-0.7493.hdf5'
    model.load_weights(filename)

    model.compile(loss='categorical_crossentropy', optimizer='adam')

    msg = "ASdasdasD"
    print(generate_reply(model, corpus, str(msg)))
    app.run(debug = True)
