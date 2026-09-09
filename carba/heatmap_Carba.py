import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

with open("Results_Jianbo.txt", "r") as fh1, open("Results_coris.txt", "r") as fh2, open("Results_NG.txt", "r") as fh3:
    ji = [line.strip().split('\t') for line in fh1]
    co = [line.strip().split('\t') for line in fh2]
    ng = [line.strip().split('\t') for line in fh3]

    tests = [co, ng, ji]
    positives = [[[], [], [], [], [], []], [[], [], [], [], [], []], [[], [], [], [], [], []]]
    negatives = [[[], [], [], [], [], []], [[], [], [], [], [], []], [[], [], [], [], [], []]]

    for l in range(3): # row: co, ng oder ji
        for m in range(3): # collumn: co, ng oder ji
            for n in range(1, 6): # gen: kpc, ndm, imp, vim, oxa-48
                pos = neg = 0
                for p in range(1, 62): # isolate
                    if int(tests[l][p][n]) == int(tests[m][p][n]):
                        pos += 1
                    else:
                        neg += 1
                positives[l][n-1].append(pos)
                negatives[l][n-1].append(neg)

print(positives)
print(negatives)
for q in range(3): # row: co, ng, ji
    for r in range(3): # collumn: co ng ji
        sum_P = sum_N = 0
        for s in range(5): # gen: kpc, ndm, imp, vim, oxa-48
            sum_P += positives[q][s][r]
            sum_N += negatives[q][s][r]
        positives[q][5].append(sum_P)
        negatives[q][5].append(sum_N)

reihenfolge = ("KPC", "NDM", "IMP", "VIM", "OXA-48", "total")
testnamen = ['Coris Bioconcept', 'NG Biotech', 'Jianbo']
for b in range(6): # gen: kpc, ndm, imp, vim, oxa-48, total
    data = [[], [], []]
    for a in range(3): # row
        for c in range(3): # collumn
            wert = int(positives[a][b][c]) / (int(positives[a][b][c]) + int(negatives[a][b][c]))
            data[a].append(wert)

    # heatmap
    df = pd.DataFrame(data, index=testnamen, columns=testnamen)
    sns.heatmap(df, annot=True, annot_kws={"size": 12} ,cmap='Greys', square=True, linewidths=0.5, linecolor="white", vmin=0.85, vmax=1.0)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.title(f"{reihenfolge[b]}", fontsize=15, pad=15)
    plt.show()