import matplotlib.pyplot as plt
import numpy as np

y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.5, 2, 2.5, 3, 3.5,
     4, 4.5, 5, 5.5,
     6, 6, 6, 6, 6, 6, 6,
     10, 14, 18, 18, 18, 18, 18, 18, 18, 21, 25,
     25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25,
     23, 21, 19, 17, 15, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
     13, 13, 13, 13, 13, 13, 13, 13, 13,
     15, 17, 19, 21, 23, 25, 25, 25, 25, 25,
     25, 25, 25, 25, 25,
     25, 25, 25, 25, 25,
     25, 25, 25, 25, 25, 23, 21, 19, 17, 15, 13, 11, 9,
     7, 5, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

x = []
for i in range(len(y)):
    x.append(i)

fig, ax = plt.subplots(1)

# my_string = '2018-08-11'
# ax.text(0.1, 0.5, my_string, va='center')
# ax.text(0.3, 0.5, my_string, rotation=90, va='center')
# ax.text(0.5, 0.5, '\n'.join(my_string), va='center')
# ax.text(0.7, 0.5, '\n'.join(my_string.replace('-', '')), va='center')

ax.text(4, 7, 'Taxi Out (16 minutes)', rotation=90, va='center')
ax.text(14, 10, 'Take Off To 50 Feet', rotation=90, va='center')
ax.text(22, 20, 'Climb out and accelerate to 1500 feet and 250 knots ', rotation=90, va='center')
ax.text(65, 20, 'Cruise and Deploy Retardant', rotation=90, va='center')

ax.set_axis_off()


plt.plot(x, y)
plt.title("Mission Profile")
plt.grid(False)
plt.show()
