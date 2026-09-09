from statsmodels.stats.proportion import proportion_confint

# Funktion: Clopper–Pearson Konfidenzintervall
def clopper_pearson_ci(successes, total, alpha=0.05):
    if total == 0:
        return (0.0, 0.0)
    lower, upper = proportion_confint(count=successes, nobs=total, alpha=alpha, method='beta')
    return lower, upper

# Results ändern
with open('Referenzen_Acineto.txt', "r") as a, open("Results_Acineto_Jianbo.txt", "r") as b:
    ref = [line.strip().split('\t') for line in a]
    test = [line.strip().split('\t') for line in b]

    TP_total = 0
    FP_total = 0
    FN_total = 0
    TN_total = 0

    for i in range(1, 3): # Coris: range(1,4). Jianbo: range(1,3)

        TP = 0
        FP = 0
        FN = 0
        TN = 0

        for j in range(1, 26): # Coris: 41. Jianbo: 26
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
        sensitivity = TP / (TP + FN)
        specificity = TN / (FP + TN)
        accuracy = (TP + TN) / (TP + FP + TN + FN)

        # 95%-CIs berechnen
        sens_ci = clopper_pearson_ci(TP, TP + FN)
        spec_ci = clopper_pearson_ci(TN, TN + FP)
        acc_ci = clopper_pearson_ci(TP + TN, TP + TN + FP + FN)

        # Ausgabe je Gen
        print(f"sensitivity = {sensitivity:.3f}; ({sens_ci[0]:.3f} – {sens_ci[1]:.3f}); ", end="")
        print(f"specificity = {specificity:.3f}; ({spec_ci[0]:.3f} – {spec_ci[1]:.3f}); ", end="")
        print(f"accuracy = {accuracy:.3f}; ({acc_ci[0]:.3f} – {acc_ci[1]:.3f})")

        FP_total += FP
        FN_total += FN
        TP_total += TP
        TN_total += TN

    # Gesamtmetriken
    total_sensitivity = TP_total / (TP_total + FN_total)
    total_specificity = TN_total / (TN_total + FP_total)
    total_accuracy = (TP_total + TN_total) / (TP_total + TN_total + FP_total + FN_total)

    # Gesamt-CIs
    total_sens_ci = clopper_pearson_ci(TP_total, TP_total + FN_total)
    total_spec_ci = clopper_pearson_ci(TN_total, TN_total + FP_total)
    total_acc_ci = clopper_pearson_ci(TP_total + TN_total, TP_total + TN_total + FP_total + FN_total)

    # Ausgabe Gesamtwerte
    print(f"total: sensitivity = {total_sensitivity:.3f}; ({total_sens_ci[0]:.3f} – {total_sens_ci[1]:.3f}); ", end="")
    print(f"specificity = {total_specificity:.3f}; ({total_spec_ci[0]:.3f} – {total_spec_ci[1]:.3f}); ", end="")
    print(f"accuracy = {total_accuracy:.3f}; ({total_acc_ci[0]:.3f} – {total_acc_ci[1]:.3f})")