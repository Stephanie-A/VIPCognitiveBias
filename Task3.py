from dicts import confidence

def confidenceRating(hypothesis): # pass in the hypothesis that has removed all generic words as a string, hypothesis
# is a string, pass in database which is a dictionary
    hypo = hypothesis.split(',')
    diff = 0
    string = ""
    for key in confidence.keys():
        keyString = key[:-2] # keep track of the string that does not contain the rating in it, only the hypothesis
        store = keyString.split(',')

        similarity = 0 # keep track of how many phrases are the same

        num = int(confidence[key])

        words = hypothesis.split(',')

        for storeKey in store: # trace through hyposthesis' keywords, and try finding it in the dictionary
            isAdded = False
            for w in words:
                if storeKey == w:
                    similarity = similarity + 1
            if similarity == 0:
                diff += num

        if similarity >= 2: # if it is the same hypothesis, then return a phrase
            if key[-1] == '3':
                string += "There are " + str(num) + " people who are somewhat confident about your hypothesis.\n"
            if key[-1] == '4':
                string += "There are " + str(num) + " people who are kind of confident about your hypothesis.\n"
            if key[-1] == '5':
                string + "There are " + str(num) + " people who are super confident about your hypothesis.\n"
    string += "There are " + str(diff) + " people who don't agree with you.\n"
    return string
