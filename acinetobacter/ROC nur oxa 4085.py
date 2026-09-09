import matplotlib.pyplot as plt
import numpy as np

with open('Data_ROC_curve_Acineto.txt', "r") as fh:
    werte = [line.strip().split('\t') for line in fh]
    tests = {
        "Coris BioConcept": {"sensitivity": float(werte[4][1]), "sensitivity_std": float(werte[4][3]),
                   "specificity": float(werte[4][2]), "specificity_std": float(werte[4][4])},
    }

    plt.figure(figsize=(6, 6))
    plt.plot([0, 1], [0, 1], 'k--', label="Chance Line") # gestrichelte Linien die durch Punkte (0/0) und (1/1) geht

    for test_name, metrics in tests.items():
        tpr = metrics["sensitivity"]
        fpr = 1 - metrics["specificity"]
        tpr_std = metrics["sensitivity_std"]
        fpr_std = metrics["specificity_std"]

        colors = {'Coris BioConcept' : '#1f77b4'}

        # Fehlerbalken zeichnen
        plt.errorbar(fpr, tpr, xerr=fpr_std, yerr=tpr_std, fmt='o', capsize=5, label=test_name, color=colors[test_name])

    plt.xlabel("False Positive Rate (1 - Specificity)")
    plt.ylabel("True Positive Rate (Sensitivity)")
    plt.title(f"{werte[4][0]}")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlim([- 0.1, 1.1])
    plt.ylim([- 0.1, 1.1])
    plt.show()
