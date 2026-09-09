import random
import numpy as np
import statistics

with open('Referenzen', "r") as a, open("Resultate", "r") as b:
    ref = [line.strip().split('\t') for line in a]
    test = [line.strip().split('\t') for line in b]

    random.seed(0) # 0

    alles = [[], [], []]

    for k in range(10000): # 10.000 wdh

        TP_total = FP_total = FN_total = TN_total = 0

        numbers = random.sample(range(1, 41), 20) # 20

        TP = FP = FN = TN = 0

        for j in numbers:
            l_ref = int(ref[j][1]) # NGS: 1. Coris: 2. NG: 3.
            l_test = int(test[j][2]) # Coris: 1. NG: 2

            if l_ref == 1:
                if l_test == 1:
                    TP += 1
                else:
                    FN += 1
            elif l_ref == 0:
                if l_test == 1:
                    FP += 1
                else:
                    TN += 1
        if TP + FN == 0:
            sensitivity = None
        else:
            sensitivity = TP / (TP + FN)
        if FP + TN == 0:
            specificity = None
        else:
            specificity = TN / (FP + TN)
        accuracy = (TP + TN) / (TP + FP + TN + FN)
        alles[0].append(sensitivity)
        alles[1].append(specificity)
        alles[2].append(accuracy)

alles_neu = [[x for x in inner if x != None] for inner in alles]

mittelwert = []
standardabweichung = []

for p, gruppe in enumerate(alles_neu):
    mw = statistics.mean(gruppe)
    stw = statistics.stdev(gruppe)
    mittelwert.append(mw)
    standardabweichung.append(stw)

print('se, sp, ac')
print(mittelwert)
print(standardabweichung)