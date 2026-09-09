import random
import numpy as np
import statistics

with open('referenzen.txt', "r") as a, open("Results_Coris.txt", "r") as b:
    ref = [line.strip().split('\t') for line in a]
    test = [line.strip().split('\t') for line in b]

    random.seed(0)

    se_KPC = []
    sp_KPC = []
    ac_KPC = []
    se_NDM = []
    sp_NDM = []
    ac_NDM = []
    se_IMP = []
    sp_IMP = []
    ac_IMP = []
    se_VIM = []
    sp_VIM = []
    ac_VIM = []
    se_OXA = []
    sp_OXA = []
    ac_OXA = []
    se_total = []
    sp_total = []
    ac_total = []

    for k in range(10000): # 100 wdh

        TP_total = FP_total = FN_total = TN_total = 0

        numbers = random.sample(range(1, 62), 30) # 30

        for i in range(1, 6):
            d = 1 * 5 + i # has to be changed depending on which reference should be used

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

            if TP + FN == 0:
                sensitivity = None
            else:
                sensitivity = TP / (TP + FN)
            if FP + TN == 0:
                specificity = None
            else:
                specificity = TN / (FP + TN)
            accuracy = (TP + TN) / (TP + FP + TN + FN)

            FP_total += FP
            FN_total += FN
            TP_total += TP
            TN_total += TN

            if i == 1:
                se_KPC.append(sensitivity)
                sp_KPC.append(specificity)
                ac_KPC.append(accuracy)
            elif i == 2:
                se_NDM.append(sensitivity)
                sp_NDM.append(specificity)
                ac_NDM.append(accuracy)
            elif i == 3:
                se_IMP.append(sensitivity)
                sp_IMP.append(specificity)
                ac_IMP.append(accuracy)
            elif i == 4:
                se_VIM.append(sensitivity)
                sp_VIM.append(specificity)
                ac_VIM.append(accuracy)
            elif i == 5:
                se_OXA.append(sensitivity)
                sp_OXA.append(specificity)
                ac_OXA.append(accuracy)

        total_sensitivity = TP_total / (TP_total + FN_total)
        total_specificity = TN_total / (TN_total + FP_total)
        total_accuracy = (TP_total + TN_total) / (TP_total + TN_total + FP_total + FN_total)
        se_total.append(total_sensitivity)
        sp_total.append(total_specificity)
        ac_total.append(total_accuracy)

alles = [se_KPC, sp_KPC, ac_KPC, se_NDM, sp_NDM,ac_NDM, se_IMP, sp_IMP, ac_IMP, se_VIM, sp_VIM, ac_VIM, se_OXA, sp_OXA, ac_OXA, se_total, sp_total, ac_total]

alles_neu = [[x for x in inner if x != None] for inner in alles]

mittelwert = []
standardabweichung = []

for p, gruppe in enumerate(alles_neu):
    mw = statistics.mean(gruppe)
    stw = statistics.stdev(gruppe)
    mittelwert.append(mw)
    standardabweichung.append(stw)

print("se_KPC, sp_KPC, ac_KPC, se_NDM, sp_NDM,ac_NDM, se_IMP, sp_IMP, ac_IMP, se_VIM, sp_VIM, ac_VIM, se_OXA, sp_OXA, ac_OXA, se_total, sp_total, ac_total")
print(mittelwert)
print(standardabweichung)