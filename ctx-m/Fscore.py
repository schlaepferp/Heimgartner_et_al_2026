import random
import numpy as np
import statistics
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

with open('Referenzen', "r") as a, open("Resultate", "r") as b:
    list_ref = [line.strip().split('\t') for line in a]
    list_test = [line.strip().split('\t') for line in b]

    for c in range(1): # seed 0 -5
        random.seed(c)
        f1_scores = [[], []]

        for d in range(10000):
            numbers = random.sample(range(1, 41), 20) # 20 samples

            for e in range(1, 3):
                TP = FP = FN = 0

                for g in numbers:
                    ref = int(list_ref[g][1])
                    test = int(list_test[g][e])

                    if ref == 1:
                        if test == 1:
                            TP += 1
                        else:
                            FN += 1
                    elif ref == 0:
                        if test == 1:
                            FP += 1
                if 2 * TP + FP + FN == 0:
                    F1 = None
                else:
                    F1 = (2 * TP) / (2 * TP + FP + FN)
                if F1 is not None:
                    f1_scores[e - 1].append(F1)

        # Boxplot
        testnamen = ['Coris BioConcept', 'NG Biotech']
        alle_daten = []

        for test_ind in range(2):
            werte = f1_scores[test_ind]
            for wert in werte:
                alle_daten.append({
                    'Test': testnamen[test_ind],
                    'Wert': wert
                })

        df = pd.DataFrame(alle_daten)

        plt.figure(figsize = (4, 5))
        sns.boxplot(y="Wert", hue='Test', data=df)

        plt.title(f"F-Scores")
        plt.ylabel('F1-Score')

        plt.xlabel('')
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.legend(loc='lower right')
        plt.show()

for test_id in range(2):
    q1 = np.percentile(f1_scores[test_id], 25)
    median = np.median(f1_scores[test_id])
    q3 = np.percentile(f1_scores[test_id], 75)

    print(f"\n{testnamen[test_ind]}")
    print(f"Q1     = {q1:.4f}")
    print(f"Median = {median:.4f}")
    print(f"Q3     = {q3:.4f}")