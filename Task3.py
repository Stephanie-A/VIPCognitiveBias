from dicts import confidence

def confidenceRating(hypothesis): # pass in the hypothesis that has removed all generic words as a string, hypothesis
# is a string, pass in database which is a dictionary
    hypo = hypothesis.split(',')

    for key in confidence.keys():
        keyString = key[:-3] # keep track of the string that does not contain the rating in it, only the hypothesis
        store = keyString.split(' ')

        similarity = 0 # keep track of how many phrases are the same
        num = int(confidence[key])

        words = hypothesis.split(' ')

        for storeKey in store: # trace through hyposthesis' keywords, and try finding it in the dictionary
            for w in words:
                if storeKey == w:
                    similarity = similarity + 1

        if similarity >= 2: # if it is the same hypothesis, then return a phrase
            if key[-1] == '5':
                return "There are " + str(num) + " people who are super confident about your hypothesis."
            if key[-1] == '4':
                return "There are " + str(num) + " people who are kind of confident about your hypothesis."
            if key[-1] == '3':
                return "There are " + str(num) + " people who are somewhat confident about your hypothesis."
