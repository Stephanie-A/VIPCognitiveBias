from Generalize import generalize
from Task3 import confidenceRating

hypothesis = "Maybe this is the 50s or 60s"
newHypo = generalize("extraneousWords.txt", hypothesis)

print newHypo
print confidenceRating(newHypo)
