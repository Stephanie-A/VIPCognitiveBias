def confirmationBias(isSupportingQuestion, hypothesis):
    hypo = hypothesis.split(',')
    dict topics = {
        'location': 0,
        'time' : 0,
        'person' : 0
    }

    for word in hypo:
        if word in open('cities15000.txt').read():
            topics['location'] += 1
        # elif word in
            # NEED TO IMPLEMENT OTHER DBS

    maxTopic = ""
    if (topics['location'] > topics['time'] && topics['location'] > topics['people']):
        maxTopic = 'location'
    elif (topics['time'] > topics['location'] && topics['time'] > topics['people']):
        maxTopic = 'time'
    else:
        maxTopic = 'person'

    if (isSupportingQuestion):
        return "What evidence do you have which supports this " + maxTopic
    else:
        return "What evidence do you have which doesn't support this " + maxTopic
