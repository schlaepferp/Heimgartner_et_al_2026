import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

with (open('Referenzen_Boxplot_Aciento.txt', "r") as a, open("Results_Boxplot_Acineto.txt", "r") as b):
    list_ref = [line.strip().split('\t') for line in a]
    list_test = [line.strip().split('\t') for line in b]

random.seed(0)

# [Test][Gen]
# Coris:  OXA-23, NDM, OXA-40/58, total
# Jianbo: OXA-23, NDM, OXA-40/58 (leer), total
f1_scores = [[[], [], [], []], [[], [], [], []]]

# werte generieren
for d in range(10000):  # 10000 iterations

    numbers_c = random.sample(range(1, 41), 20)     # coris
    numbers_j = random.sample(range(1, 26), 13)     # jianbo

    # total[test][TP/FP/FN]
    total = [[[], [], []], [[], [], []]]

    # coris. spalten 1-3. OXA-23, NDM, OXA-40/58
    for f in range(1, 4):
        TP = FP = FN = 0

        for g in numbers_c:
            ref = int(list_ref[g][f])
            test = int(list_test[g][f])

            if ref == 1:
                if test == 1:
                    TP += 1
                else:
                    FN += 1
            elif ref == 0:
                if test == 1:
                    FP += 1

        total[0][0].append(TP)
        total[0][1].append(FP)
        total[0][2].append(FN)

        denominator =  2 * TP + FP + FN
        if denominator > 0:
            F1 = (2 * TP) / denominator
            f1_scores[0][f - 1].append(F1)

    # jianbo. spalte 4 und 5
    for f in range(4, 6):
        TP = FP = FN = 0

        for g in numbers_j:
            ref = int(list_ref[g][f])
            test = int(list_test[g][f])

            if ref == 1:
                if test == 1:
                    TP += 1
                else:
                    FN += 1
            elif ref == 0:
                if test == 1:
                    FP += 1

        total[1][0].append(TP)
        total[1][1].append(FP)
        total[1][2].append(FN)

        denominator =  2 * TP + FP + FN
        if denominator > 0:
            F1 = (2 * TP) / denominator
            f1_scores[1][f - 4].append(F1)

    for h in range(2):
        denominator = (2 * sum(total[h][0]) + sum(total[h][1]) + sum(total[h][2]))
        if denominator > 0:
            F1_total = (2 * sum(total[h][0])) / denominator
            f1_scores[h][3].append(F1_total)

# Boxplot erstellen
testnamen = ['Coris BioConcept', 'Jianbo']
gen = ['OXA-23', 'NDM', 'OXA-40/58', 'total']
alle_daten = []

for gen_ind in range(4):
    for test_ind in range(2):
        werte = f1_scores[test_ind][gen_ind]
        for wert in werte:
            alle_daten.append({
                'Gen': gen[gen_ind],
                'Test': testnamen[test_ind],
                'Wert': wert
            })

for test_ind, test in enumerate(["Coris", "Jianbo"]):
    print(test)
    for gen_ind, gen in enumerate(["OXA-23", "NDM", "OXA-40/58", "total"]):
        print(gen, len(f1_scores[test_ind][gen_ind]))

df = pd.DataFrame(alle_daten)

plt.figure(figsize=(5, 5))
sns.boxplot(x="Gen", y="Wert", hue='Test', data=df, palette= {"Coris BioConcept" : "#1f77b4", "Jianbo" : "#2ca02c"})

plt.title(f"F-Scores")
plt.ylabel('F1-Score')

plt.xlabel('')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()