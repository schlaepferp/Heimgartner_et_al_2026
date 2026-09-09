import matplotlib.pyplot as plt
import numpy as np

with open('roc curve data ngs', "r") as fh:
    werte = [line.strip().split('\t') for line in fh]

    tests = {
        "Coris BioConcept": {"sensitivity": float(werte[1][0]), "sensitivity_std": float(werte[1][2]),
                   "specificity": float(werte[1][1]), "specificity_std": float(werte[1][3])},
        "NG Biotech": {"sensitivity": float(werte[1][4]), "sensitivity_std": float(werte[1][6]),
                   "specificity": float(werte[1][5]), "specificity_std": float(werte[1][7])}
    }

    plt.figure(figsize=(6, 6))
    plt.plot([0, 1], [0, 1], 'k--', label="Chance Line")

    for test_name, metrics in tests.items():
        tpr = metrics["sensitivity"]
        fpr = 1 - metrics["specificity"]
        tpr_std = metrics["sensitivity_std"]
        fpr_std = metrics["specificity_std"]

        plt.errorbar(fpr, tpr, xerr=fpr_std, yerr=tpr_std, fmt='o', capsize=5, label=test_name)

    plt.xlabel("False Positive Rate (1 - Specificity)")
    plt.ylabel("True Positive Rate (Sensitivity)")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlim([- 0.1, 1.1])
    plt.ylim([- 0.1, 1.1])
    plt.show()
