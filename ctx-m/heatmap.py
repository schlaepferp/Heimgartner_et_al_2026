import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

with open("Resultate", "r") as fh1:
    tests = [line.strip().split('\t') for line in fh1]

    data = [[1], []]
    pos = 0

    for p in range(1, 41):
        if int(tests[p][1]) == int(tests[p][2]):
            pos += 1

    agreement = pos / 41
    data[0].append(agreement)
    data[1].append(agreement)
    data[1].append(1)

testnamen = ['Coris BioConcept', 'NG Biotech']

# heatmap
df = pd.DataFrame(data, index=testnamen, columns=testnamen)
sns.heatmap(df, annot=True, annot_kws={"size": 12} ,cmap='Greys', square=True, linewidths=0.5, linecolor="white", vmin=0.85, vmax=1.0)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.title("Test Comparison", fontsize=15, pad=15)
plt.show()