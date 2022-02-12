"""
AIRFOIL ANALYSIS
2/10/22
"""


import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

graphs = 'N'

df = pd.read_csv('4417_EditedData.csv')
alpha = df["alpha"]
Cl = df["CL"]
Cd = df["CD"]


avscl_data = np.polyfit(alpha[0:13], Cl[0:13], 1)
plt.figure("Alpha vs Cl")
plt.plot(alpha,Cl)
plt.plot(alpha, (avscl_data[0]*alpha)+avscl_data[1])
plt.title('Alpha vs $C_L$')
plt.xlabel('Alpha')
plt.ylabel('$C_L$')
ax = plt.gca()
if graphs == 'Y':
    plt.show()

plt.figure('Cl vs Cd')
plt.plot(Cl,Cd)
plt.xlabel('$C_L$')
plt.ylabel('$C_D$')
plt.title('$C_L$ vs $C_D$')
plt.figure("Cl vs Cd")
if graphs == 'Y':
    plt.show()





