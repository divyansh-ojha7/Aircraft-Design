import matplotlib.pyplot as plt
import numpy as np

y = np.array([50, 20, 15, 10, 5])
total_mats = 50 + 20 + 15 + 10 + 5
mylabels = [f"{100*(50/total_mats)}%", f"{100*(20/total_mats)}%",f"{100*(15/total_mats)}%", f"{100*(10/total_mats)}%", f"{100*(5/total_mats)}%"]

plt.pie(y, labels = mylabels)
plt.legend(["Composites", "Aluminum", "Titanium", "Steel", "Other"], bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
plt.show()