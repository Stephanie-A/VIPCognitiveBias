from Generalize import generalize
from Task3 import confidenceRating
from confirmationbias import confirmationbias

# This main function takes in a hypothesis String, then:
# 1.) Generalizes the hypothesis by removing all extraneous words.
# 2.) Calls the Confidence Rating function to get a sentence on others' agreement.
# 3.) Calls Confirmation Bias function to prompt explanations for hypothesis.
def main(hypothesis):

    gen_hypo = generalize("extraneousWords.txt", hypothesis)
    agree_phrase = confidenceRating(gen_hypo)

    print agree_phrase

    prompt = confirmationbias(true, gen_hypo)

    return prompt