import re, math

def to_word_table(text):
    words = re.split(" ", text)
    words_table = dict()
    for word in words:
        c = words_table.get(word, 0)
        words_table[word] = c + 1

    return words_table

def word_idf(bags, word):
    return math.log(sum([word in bag for bag in bags])/float(len(bags)))

def idfs(bags):
    idf = dict()
    for bag in bags:
        for word in bag:
            if word not in idf:
                idf[word] = word_idf(bags, word)
    return idf
            
print(to_word_table("hello world"))
print(word_idf(["hello world", "hello man"], "man"))
