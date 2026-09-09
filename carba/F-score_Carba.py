import random
import numpy as np
import statistics
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

with open('referenzen boxplot ngs', "r") as a, open("results for boxplot.txt", "r") as b:
    list_ref = [line.strip().split('\t') for line in a]
    list_test = [line.strip().split('\t') for line in b]

    for c in range(1):
        random.seed(0)
        f1_scores = [[[], [], [], [], [], []], [[], [], [], [], [], []], [[], [], [], [], [], []]]

        for d in range(10000): # 100
            numbers = random.sample(range(1, 62), 30) # 30 samples
            total = [[[], [], []], [[], [], []], [[], [], []]]
            for f in range(1, 6):
                for e in range(3):

                    TP = FP = FN = 0

                    for g in numbers:
                        ref = int(list_ref[g][f + e * 5])
                        test = int(list_test[g][f + e * 5])

                        if ref == 1:
                            if test == 1:
                                TP += 1
                            else:
                                FN += 1
                        elif ref == 0:
                            if test == 1:
                                FP += 1
                    total[e][0].append(TP)
                    total[e][1].append(FP)
                    total[e][2].append(FN)
                    if 2 * TP + FP + FN == 0:
                        F1 = None
                    else:
                        F1 = (2 * TP) / (2 * TP + FP + FN)
                    if F1 is not None:
                        f1_scores[e][f-1].append(F1)
            for h in range(3):
                F1_total = (2 * sum(total[h][0])) / (2 * sum(total[h][0]) + sum(total[h][1]) + sum(total[h][2]))
                f1_scores[h][5].append(F1_total)

        # Boxplot
        testnamen = ['Coris BioConcept', 'NG Biotech', 'Jianbo']
        gen = ['KPC', 'NDM', 'IMP', 'VIM', 'OXA-48', 'total']
        alle_daten = []
        for gen_ind in range(6):
            for test_ind in range(3):
                werte = f1_scores[test_ind][gen_ind]
                for wert in werte:
                    alle_daten.append({
                        'Gen': gen[gen_ind],
                        'Test': testnamen[test_ind],
                        'Wert': wert
                    })

        df = pd.DataFrame(alle_daten)

        plt.figure(figsize = (7, 5))
        sns.boxplot(x="Gen", y="Wert", hue='Test', data=df)

        plt.title(f"F-Scores")
        plt.ylabel('F1-Score')

        plt.xlabel('')
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.show()