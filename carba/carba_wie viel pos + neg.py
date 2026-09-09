import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# wie viel pos und neg gibt es in der referenzliste von Boxplot
with open("referenzen boxplot.txt", "r") as fh1:
    ref = [line.strip().split('\t') for line in fh1]

    positive = [[], [], []]
    negative = [[], [], []]
    gesamt = [[], [], []]

    for a in range(3):
        for b in range(1, 6):
            pos = neg = 0
            for c in range(1, 62):
                value = int(ref[c][b + a * 5])
                if value == 1:
                    pos += 1
                if value == 0:
                    neg += 1
            positive[a].append(pos)
            negative[a].append(neg)

for d in range(3):
    positive[d].append(sum(positive[d]))
    negative[d].append(sum(negative[d]))

for e in range(3):
    for f in range(6):
        gesamt[e].append((positive[e][f] + negative[e][f]))

print(positive)
print(negative)
print(gesamt)