import random
import numpy as np
import statistics

with open('Referenzen_Acineto.txt', "r") as a, open("Results_Acineto_Jianbo.txt", "r") as b: # Results anpassen
    ref = [line.strip().split('\t') for line in a]
    test = [line.strip().split('\t') for line in b]

    random.seed(0)

    alles = [[[], [], []], [[], [], []], [[], [], []]] # 1: O23, NDM, O40/58, total. 2: se, sp, ac. anpassen

    for k in range(10000): # 10000 wdh

        TP_total = FP_total = FN_total = TN_total = 0

        numbers = random.sample(range(1, 26), 13) # range + k anpassen

        for i in range(1, 3): # gen. c: 1,4. j: 1,3
            TP = FP = FN = TN = 0

            for j in numbers:
                l_ref = int(ref[j][i])
                l_test = int(test[j][i])

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
            #print([TP, FP, TN, FN])
            if TP + FN == 0:
                sensitivity = None
            else:
                sensitivity = TP / (TP + FN)
            if FP + TN == 0:
                specificity = None
            else:
                specificity = TN / (FP + TN)
            accuracy = (TP + TN) / (TP + FP + TN + FN)

            alles[i-1][0].append(sensitivity)
            alles[i-1][1].append(specificity)
            alles[i-1][2].append(accuracy)

            FP_total += FP
            FN_total += FN
            TP_total += TP
            TN_total += TN

        total_sensitivity = TP_total / (TP_total + FN_total)
        total_specificity = TN_total / (TN_total + FP_total)
        total_accuracy = (TP_total + TN_total) / (TP_total + TN_total + FP_total + FN_total)
        alles[2][0].append(total_sensitivity) # c: 3. j: 2
        alles[2][1].append(total_specificity) # c: 3. j: 2
        alles[2][2].append(total_accuracy) # c: 3. j: 2

alles_neu = [[[wert for wert in inner if wert is not None]for inner in mittel]for mittel in alles]

ergebnisse = [[(np.mean(inner), np.std(inner)) for inner in mittel] for mittel in alles_neu]
Gen = ['OXA-23', 'NDM', 'total'] # anpassen
what = ['sensitivity', 'specifity', 'accuracy']

for i, mittel in enumerate(ergebnisse):
    print(Gen[i])
    for j, (mean, std) in enumerate(mittel):
        print(what[j], f" Mittelwert = {mean:.4f}, Standard Deviation = {std:.4f}")
