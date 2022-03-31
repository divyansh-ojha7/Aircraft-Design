"""
AIRFOIL IMAGE GENERATOR
3/3/22
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('NACA4417.csv')
x_val = df["x"]
y_val = df["y"]

plt.rcParams['toolbar'] = 'None'
plt.figure(figsize=(10,1.5))
plt.plot(x_val,y_val)
plt.title('NACA 4417')
plt.show()