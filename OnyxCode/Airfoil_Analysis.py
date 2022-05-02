"""
AIRFOIL ANALYSIS
2/10/22
"""


import pandas as pd

import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"

import numpy as np

print('########################################')
print('      RUNNING AIRCRAFT ANALYSIS         ')
print('########################################')

show_graphs = 'Y'

df = pd.read_csv('4417_EditedData.csv')
alpha = df["alpha"]
Cl = df["CL"]
Cd = df["CD"]


avscl_data = np.polyfit(alpha[0:13], Cl[0:13], 1)

if show_graphs == 'Y':
    plt.plot(alpha,Cl, label='2D')
    plt.plot(alpha, (avscl_data[0]*alpha)+avscl_data[1], label='$a_0$', color='green', linewidth=1)
    plt.axhline(y = max(Cl), linestyle='--', label='Maximum $C_l$', color='red', linewidth=1)
    plt.axvline(x = 14, linestyle='--', label='Alpha at Stall', color='purple', linewidth=1)
    plt.title('Alpha vs $C_L$')
    plt.xlabel('Alpha')
    plt.ylabel('$C_L$')
    plt.legend()
    ax = plt.gca()
    plt.show()

    plt.plot(Cl,Cd)
    plt.axhline(y = min(Cd), linestyle='--', label='Minimum $C_d$', color='green', linewidth=1)
    plt.axvline(x = 1.725, linestyle='--', label='$C_l$ at Stall', color='red', linewidth=1)
    plt.xlabel('$C_L$')
    plt.ylabel('$C_D$')
    plt.title('$C_L$ vs $C_D$')
    plt.legend()
    plt.show()