def confidenceRating(database, hypothesis): # pass in the hypothesis that has removed all generic words as a string, hypothesis
# is a string, pass in database which is a dictionary
    hypo = hypothesis.split(',')

    for key in database.keys():
        keyString = key[:-3] # keep track of the string that does not contain the rating in it, only the hypothesis
        store = keyString.split(',')
        [item.strip() for item in keyString.split(',')] #remove the white space at the front of each phrase,
        #for instance, make ' 2000'->'2000'since at the front
        #of store, it would be 'Atlanta', but ' 2000' at the end. If in the dictionary, '2000' is at the front, this could trigger
        #problems

        similarity = 0 # keep track of how many phrases are the same
        num = int(database[key])

        for storeKey in store: # trace through hyposthesis' keywords, and try finding it in the dictionary
            for hypoKey in hypo:
                if storeKey == hypoKey:
                    similarity = similarity + 1

        if similarity >= 2: # if it is the same hypothesis, then return a phrase
            if key[-1] == '5':
                return "There are " + str(num) + " people who are super confident about your hypothesis."
            if key[-1] == '4':
                return "There are " + str(num) + " people who are kind of confident about your hypothesis."
            if key[-1] == '3':
                return "There are " + str(num) + " people who are somewhat confident about your hypothesis."


dict = {'Atlanta, people, 2000, 4': '6', 'New York City, 1949, 5': '7', 'Thai, 10 people, 1998, 3': '11'}
hypothesis = "New York City, 1949, 5"
print(confidenceRating(dict, hypothesis))
hypothesis2 = "Thai, 1997, 10 people"
print(confidenceRating(dict, hypothesis2))

hypothesis3 = "Thai, 1998, 10 people"
print(confidenceRating(dict, hypothesis2))




