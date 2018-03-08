from Generalize import generalize
from confirmationbias import confirmationBias
from anchoringbias import anchoringbias
from dicts import counter

# This main function takes in a hypothesis String, then:
# 1.) Generalizes the hypothesis by removing all extraneous words.
# 2.) Determines the hypothesis' focus.
# 3.) Every fifth time, calls Confirmation Bias function to prompt explanations for hypothesis.
#     Change its boolean value to swap for/against evidence questions each time it is called.
# 4.) Call Anchoring Bias function each time.
# 5.) Print both prompts.

counter = 0 # Global variable to keep track of times main is called.

def main(hypothesis):
    global counter
    counter = counter + 1
    gen_hypo = generalize("Resources/extraneousWords.txt", hypothesis) # Get hypothesis as ',' separated String

    ###### CREDIT: This section is Stephanie's focus-determining code right here,
    ######         obtained from the 'confirmationbias' file.
    hypo = gen_hypo.split(',')
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
    ######

    promptCB = "" # String to hold return statement from conf. bias function
    if counter % 5 == 0 :
        toggle = counter % 2 == 0 # Multiples of 5 switch between ending with
                                  # 5s and 0s. Use this even/odd to toggle boolean.
        promptCB = confirmationBias(toggle, gen_hypo)

        promptAB = "" # String to hold return statement from anch. bias function
        promptAB = anchoringbias(maxTopic, topics)

        counter = counter + 1 # Increment global counter variable

        print promptCB
        print promptAB
