hypothesis = "50s,or,60s"
other = "Other,"
notFocusing = 'people'

confidence = {
    hypothesis + '1': 10,
    hypothesis + '2': 3,
    hypothesis + '3': 2,
    hypothesis + '4': 20,
    hypothesis + '5': 40,
    other + '1': 1,
    other + '2': 2,
    other + '3': 3,
    other + '4': 4,
    other + '5': 5,
}

questions = {
    'location' : 'Why do you think it is in that location?',
    'person' : 'Why do you think it is that person?',
    'time' : 'Why do you think it is during that time period',
    'notFocusing' : 'User is not focusing on ' + notFocusing
    'anchor' : 'Any evidence that it is not ' + hypothesis
}

# Make function that returns questions to ask user and asks for anchoring bias
