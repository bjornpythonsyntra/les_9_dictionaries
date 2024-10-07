# Functie dat getallen genereert en verdeelt over 4 lijsten
import random
lijstmatrix = [[] for _ in range(4)]
print(lijstmatrix)
for i in range(1,21):
    willekeur=random.randint(10,200)
    for lijst in range(1,5): # lijsten 1 tot en met 4
        if ((willekeur-lijst)%4)==0:
            lijstmatrix[lijst-1].append(willekeur)
print(lijstmatrix)
for k in range(len(lijstmatrix)):
    lijstmatrix[k].sort()
print(lijstmatrix)
