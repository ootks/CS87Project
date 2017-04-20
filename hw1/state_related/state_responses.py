def get_mentioned_states(message):
    """Gets all of the states mentioned in message"""
    found_states = []
    lower_message = message.lower()
    for state in states:
        if lower_message.find(state.lower()) != -1:
            found_states.append(state)
    return found_states

def most_similar_state(message):
    """Finds the state most similar to the message"""
    message = parse.clean_text(message, dict())
    bags["message"] = tf_idf.text2bag(message)
    tf_idfs = tf_idf.bags2tfidfs(bags)

    max_cos = cosine_similarity.cos_sim(bags["message"], bags["Michigan"])
    candidate = "Michigan"
    for state in bags:
        if state != "message":
            cos = cosine_similarity.cos_sim(bags["message"], bags[state])
            if cos > max_cos:
                candidate = state
                max_cos = cos
    return candidate



def get_response(state):
    return "{} is all about {}, {}, and {}.".format(
            state,
            stem2tokens[most_sig[state][1]][0],
            stem2tokens[most_sig[state][2]][0],
            stem2tokens[most_sig[state][3]][0]
            )
    
