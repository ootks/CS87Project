import math

def cos_sim(text1, text2):
    '''
    Returns the cosine similarity of two texts, as represented as a 
    dictionary of tf_idfs
    '''
    dot = sum([text1[word] * text2[word] for word in text1 if word in text2])
    len1 = math.sqrt(sum([x*x for x in text1.values()]))
    len2 = math.sqrt(sum([x*x for x in text2.values()]))
    
    return dot/(len1 * len2)
