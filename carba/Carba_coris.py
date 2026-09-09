import math
import statsmodels
from statsmodels.stats.proportion import proportion_confint

def clopper_pearson_ci(successes, total, alpha=0.05):
    if total == 0:
        return (0.0, 0.0)
    lower, upper = proportion_confint(count=successes, nobs=total, alpha=alpha, method='beta')
    return lower, upper

with (open('referenzen.txt', "r") as ref, open("Results_coris.txt", "r") as test):
    ref_lines = [line.strip().split('\t') for line in ref]
    test_lines = [line.strip().split('\t') for line in test]

    for k in range(2): # to only use collumns in reference table that are relevant for this test

        TP_total = 0
        FP_total = 0
        FN_total = 0
        TN_total = 0

        for i in range(k*5 + 1, (k+1) * 5 + 1): # to continue in steps of 5
            TP = 0
            FP = 0
            FN = 0
            TN = 0

        # to go through every row befor jumping to index 2
            for j in range(1, len(ref_lines)):
                l_ref = int(ref_lines[j][i])
                l_test = int(test_lines[j][i - k * 5])

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

            # confidence intervalls
            sens_ci = clopper_pearson_ci(TP, TP + FN)
            spec_ci = clopper_pearson_ci(TN, FP + TN)
            acc_ci = clopper_pearson_ci(TP + TN, TP + TN + FP + FN)

            print(f"Sensitivity = {sensitivity:.3f}, ({sens_ci[0]:.3f} – {sens_ci[1]:.3f}); ", end="")
            print(f"Specificity = {specificity:.3f}, ({spec_ci[0]:.3f} – {spec_ci[1]:.3f}); ", end="")
            print(f"Accuracy = {accuracy:.3f}, ({acc_ci[0]:.3f} – {acc_ci[1]:.3f})")
            FP_total += FP
            FN_total += FN
            TP_total += TP
            TN_total += TN
            # FP, FN, TP and TN of every gen is added to total

        total_sensitivity = TP_total / (TP_total + FN_total)
        total_specificity = TN_total / (TN_total + FP_total)
        total_accuracy = (TP_total + TN_total) / (TP_total + TN_total + FP_total + FN_total)
        total_sens_ci = clopper_pearson_ci(TP_total, TP_total + FN_total)
        total_spec_ci = clopper_pearson_ci(TN_total, TN_total + FP_total)
        total_acc_ci = clopper_pearson_ci(TP_total + TN_total, TP_total + TN_total + FP_total + FN_total)

        print(f"total: Sensitivity = {total_sensitivity:.3f}, ({total_sens_ci[0]:.3f} – {total_sens_ci[1]:.3f}); ",
              end="")
        print(f"Specificity = {total_specificity:.3f}, ({total_spec_ci[0]:.3f} – {total_spec_ci[1]:.3f}); ", end="")
        print(f"Accuracy = {total_accuracy:.3f}, ({total_acc_ci[0]:.3f} – {total_acc_ci[1]:.3f})")