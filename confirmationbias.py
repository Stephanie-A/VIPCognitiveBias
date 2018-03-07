def confirmationBias(isSupportingQuestion, hypothesis):
    hypo = hypothesis.split(',')
    topics = {
        'location': 0,
        'time' : 0,
        'person' : 0
    }

    for word in hypo:
        if word in open('Resources/cities15000.txt').read():
            topics['location'] += 1
        elif word in open('Resources/time.txt').read():
            topics['time'] += 1
        elif word in open('Resources/clothes.txt').read():
            topics['person'] += 1
    maxTopic = ""
    if (topics['location'] > topics['time'] and topics['location'] > topics['person']):
        maxTopic = 'location'
    elif (topics['time'] > topics['location'] and topics['time'] > topics['person']):
        maxTopic = 'time'
    else:
        maxTopic = 'person'

    if (isSupportingQuestion):
        return "What evidence do you have which supports this " + maxTopic
    else:
        return "What evidence do you have which doesn't support this " + maxTopic
