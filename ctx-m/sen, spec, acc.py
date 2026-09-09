import math
import statsmodels
from statsmodels.stats.proportion import proportion_confint

def clopper_pearson_ci(successes, total, alpha=0.05):
    if total == 0:
        return (0.0, 0.0)
    lower, upper = proportion_confint(count=successes, nobs=total, alpha=alpha, method='beta')
    return lower, upper

with open('Referenzen', "r") as a, open("Resultate", "r") as b:
    ref = [line.strip().split('\t') for line in a]
    test = [line.strip().split('\t') for line in b]

    for k in range(1, 4): #Coris: 1, 2. NG: 1, 3
        if k == 2:
            continue
        TP = FP = FN = TN = 0

        for j in range(1, 41):
            l_ref = int(ref[j][k])
            l_test = int(test[j][2]) #Coris: 1. NG: 2

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
        sensitivity = TP / (TP + FN)
        specificity = TN / (FP + TN)
        accuracy = (TP + TN) / (TP + FP + TN + FN)

        sens_ci = clopper_pearson_ci(TP, TP + FN)
        spec_ci = clopper_pearson_ci(TN, TN + FP)
        acc_ci = clopper_pearson_ci(TP + TN, TP + TN + FP + FN)

        print(f"sensitivity = {sensitivity:.3f}; ({sens_ci[0]:.3f} – {sens_ci[1]:.3f}); ", end="")
        print(f"specificity = {specificity:.3f}; ({spec_ci[0]:.3f} – {spec_ci[1]:.3f}); ", end="")
        print(f"accuracy = {accuracy:.3f}; ({acc_ci[0]:.3f} – {acc_ci[1]:.3f})")