import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

with open("Results_Acineto_Jianbo.txt", "r") as fh1, open("Results_Acineto_Coris.txt", "r") as fh2:
    ji = [line.strip().split('\t') for line in fh1]
    co = [line.strip().split('\t') for line in fh2]

    tests = [co, ji]
    positives = [[[], [], []], [[], [], []]]
    negatives = [[[], [], []], [[], [], []]]

    for l in range(2): # zeile: co, ji
        for m in range(2): # spalte: co, ji
            for n in range(1, 3): # gen: oxa-23, ndm
                pos = neg = 0
                for p in range(1, 26):
                    if int(tests[l][p][n]) == int(tests[m][p][n]):
                        pos += 1
                    else:
                        neg += 1
                positives[l][n-1].append(pos)
                negatives[l][n-1].append(neg)

for q in range(2):
    for r in range(2):
        sum_P = sum_N = 0
        for s in range(2):
            sum_P += positives[q][s][r]
            sum_N += negatives[q][s][r]
        positives[q][2].append(sum_P)
        negatives[q][2].append(sum_N)

reihenfolge = ("OXA-23", "NDM", "total")
testnamen = ['Coris BioConcept', 'Jianbo']
for b in range(3):
    data = [[], []]
    for a in range(2):
        for c in range(2):
            wert = int(positives[a][b][c]) / (int(positives[a][b][c]) + int(negatives[a][b][c]))
            data[a].append(wert)

    # heatmap erstellen
    df = pd.DataFrame(data, index=testnamen, columns=testnamen)
    sns.heatmap(df, annot=True, annot_kws={"size": 12} ,cmap='Greys', square=True, linewidths=0.5, linecolor="white", vmin=0.85, vmax=1.0)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.title(f"Test Comparison for {reihenfolge[b]}", fontsize=15, pad=15)
    plt.show()