import statsmodels
from statsmodels.stats.proportion import proportion_confint

def clopper_pearson_ci(successes, total, alpha=0.05):
    if total == 0:
        return (0.0, 0.0)
    lower, upper = proportion_confint(count=successes, nobs=total, alpha=alpha, method='beta')
    return lower, upper

with open('referenzen.txt', "r") as a, open("Results_Jianbo.txt", "r") as b:
    ref = [line.strip().split('\t') for line in a]
    test = [line.strip().split('\t') for line in b]

    for k in range(5):
        if k == 1 or k == 2:
            continue

        TP_total = FP_total = FN_total = TN_total = 0

        for i in range(1, 6):
            d = k * 5 + i

            TP = FP = FN = TN = 0

            for j in range(1, len(ref)):
                l_ref = int(ref[j][d])
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
            sensitivity = TP / (TP + FN)
            specificity = TN / (FP + TN)
            accuracy = (TP + TN) / (TP + FP + TN + FN)

            # Confidence interval
            sens_ci = clopper_pearson_ci(TP, TP + FN)
            spec_ci = clopper_pearson_ci(TN, FP + TN)
            acc_ci = clopper_pearson_ci(TP + TN, TP + TN + FP + FN)

            # sensitivity, specifity and accuracy for every gene
            print(f"Sensitivity = {sensitivity:.3f}, ({sens_ci[0]:.3f} – {sens_ci[1]:.3f}); ", end="")
            print(f"Specificity = {specificity:.3f}, ({spec_ci[0]:.3f} – {spec_ci[1]:.3f}); ", end="")
            print(f"Accuracy = {accuracy:.3f}, ({acc_ci[0]:.3f} – {acc_ci[1]:.3f})")
            FP_total += FP
            FN_total += FN
            TP_total += TP
            TN_total += TN

        total_sensitivity = TP_total / (TP_total + FN_total)
        total_specificity = TN_total / (TN_total + FP_total)
        total_accuracy = (TP_total + TN_total) / (TP_total + TN_total + FP_total + FN_total)
        total_sens_ci = clopper_pearson_ci(TP_total, TP_total + FN_total)
        total_spec_ci = clopper_pearson_ci(TN_total, TN_total + FP_total)
        total_acc_ci = clopper_pearson_ci(TP_total + TN_total, TP_total + TN_total + FP_total + FN_total)

        print(f"total: Sensitivity = {total_sensitivity:.3f}, ({total_sens_ci[0]:.3f} – {total_sens_ci[1]:.3f}); ", end="")
        print(f"Specificity = {total_specificity:.3f}, ({total_spec_ci[0]:.3f} – {total_spec_ci[1]:.3f}); ", end="")
        print(f"Accuracy = {total_accuracy:.3f}, ({total_acc_ci[0]:.3f} – {total_acc_ci[1]:.3f})")

