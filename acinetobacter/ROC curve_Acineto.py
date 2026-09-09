import matplotlib.pyplot as plt
import numpy as np

with open('Data_ROC_curve_Acineto.txt', "r") as fh:
    werte = [line.strip().split('\t') for line in fh]
    for j in range(1, len(werte) - 1): # ein Graph für jede Zeile im Dokument
        tests = {
            "Coris BioConcept": {"sensitivity": float(werte[j][1]), "sensitivity_std": float(werte[j][3]),
                       "specificity": float(werte[j][2]), "specificity_std": float(werte[j][4])},
            "Jianbo": {"sensitivity": float(werte[j][5]), "sensitivity_std": float(werte[j][7]),
                      "specificity": float(werte[j][6]), "specificity_std": float(werte[j][8])}
        }

        plt.figure(figsize=(6, 6))
        plt.plot([0, 1], [0, 1], 'k--', label="Chance Line")

        jitter_strength = 0.005

        for test_name, metrics in tests.items():
            tpr = metrics["sensitivity"]
            fpr = 1 - metrics["specificity"]
            tpr_std = metrics["sensitivity_std"]
            fpr_std = metrics["specificity_std"]

            tpr += np.random.uniform(-jitter_strength, jitter_strength)
            fpr += np.random.uniform(-jitter_strength, jitter_strength)

            colors = {'Coris BioConcept' : '#1f77b4', 'Jianbo' : '#2ca02c'}

            plt.errorbar(fpr, tpr, xerr=fpr_std, yerr=tpr_std, fmt='o', capsize=5, label=test_name, color=colors[test_name])

        plt.xlabel("False Positive Rate (1 - Specificity)")
        plt.ylabel("True Positive Rate (Sensitivity)")
        plt.title(f"{werte[j][0]}")
        plt.legend(loc="lower right")
        plt.grid(True)
        plt.xlim([- 0.1, 1.1])
        plt.ylim([- 0.1, 1.1])
        plt.show()
