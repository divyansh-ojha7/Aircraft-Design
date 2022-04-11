"""
GRAPHING FOR SIMILAR AIRCRAFTS
3/29/22
"""

from Drag_Buildup import *


# Format is [MTOW [lbs], AR]
BAE_146 = [84000, 8.98] # British Aerospace 146
LHC130 = [175000, 10.1] # Lockheed HC-130
CL215 = [43499, 8.15] # Canadair CL-215
DC10 = [430000, 6.91] # Douglas DC-10
B747 = [735000, 8.4] # Boeing 747
GS2T = [26147, 10.863] # Grumman S2T Airtanker

# Line of Best Fit
x = [BAE_146[0], LHC130[0], CL215[0], DC10[0], B747[0], GS2T[0]]
y = [BAE_146[1], LHC130[1], CL215[1], DC10[1], B747[1], GS2T[1]]
[a, b] = np.polyfit(x, y, 1)


plt.plot(BAE_146[0], BAE_146[1], marker='o', color='black')
plt.annotate('British Aerospace 146', BAE_146, textcoords='offset points', xytext=(-10,-15), ha='center')


plt.plot(LHC130[0], LHC130[1], marker='o', color='black')
plt.annotate('Lockheed HC-130', LHC130, textcoords='offset points', xytext=(0,-15), ha='center')

plt.plot(CL215[0], CL215[1], marker='o', color='black')
plt.annotate('Canadair CL-215', CL215, textcoords='offset points', xytext=(0,-15), ha='center')

plt.plot(DC10[0], DC10[1], marker='o', color='black')
plt.annotate('Douglas DC-10', DC10, textcoords='offset points', xytext=(0,10), ha='center')

# plt.plot(B747[0], B747[1], marker='o')
# plt.annotate('Boeing 747', B747, textcoords='offset points', xytext=(0,10), ha='center')

plt.plot(GS2T[0], GS2T[1], marker='o', color='black')
plt.annotate('Grumman S2T Airtanker', GS2T, textcoords='offset points', xytext=(0,-15), ha='center')

x = range(-400000, 1000000)
y = [a*x + b for x in x]

plt.plot(x, y, color='red')
plt.title('MTOGW vs Aspect Ratio')
plt.ylabel('Aspect Ratio')
plt.xlabel('MTOGW [lbs]')
plt.xlim(-400000,1000000)
plt.xticks([0, 200000, 400000, 600000, 800000, 1000000])
plt.grid()
plt.show()



# Format is [WS [lb/ft^2], MTOGW]
BAE_146 = [100.961538462, 84000] # British Aerospace 146
LHC130 = [100.286532951, 175000] # Lockheed HC-130
CL215 = [40.2805815353, 43499] # Canadair CL-215
DC10 = [121.126760563 , 430000] # Douglas DC-10
B747 = [134, 735000] # Boeing 747
GS2T = [48.3, 26147] # Grumman S2T Airtanker

#Line of best fit
x = [BAE_146[0], LHC130[0], CL215[0], DC10[0], B747[0], GS2T[0]]
y = [BAE_146[1], LHC130[1], CL215[1], DC10[1], B747[1], GS2T[1]]
[a, b] = np.polyfit(x, y, 1)

plt.plot(BAE_146[0], BAE_146[1], marker='o', color='black')
plt.annotate('British Aerospace 146', BAE_146, textcoords='offset points', xytext=(50,-2), ha='center')


plt.plot(LHC130[0], LHC130[1], marker='o', color='black')
plt.annotate('Lockheed HC-130', LHC130, textcoords='offset points', xytext=(43.5,-2), ha='center')

plt.plot(CL215[0], CL215[1], marker='o', color='black')
plt.annotate('Canadair CL-215', CL215, textcoords='offset points', xytext=(-40,0), ha='center')

plt.plot(DC10[0], DC10[1], marker='o', color='black')
plt.annotate('Douglas DC-10', DC10, textcoords='offset points', xytext=(-30, 7), ha='center')

plt.plot(B747[0], B747[1], marker='o', color='black')
plt.annotate('Boeing 747', B747, textcoords='offset points', xytext=(0,-15), ha='center')

plt.plot(GS2T[0], GS2T[1], marker='o', color='black')
plt.annotate('Grumman S2T Airtanker', GS2T, textcoords='offset points', xytext=(50,-15), ha='center')

x = range(-10, 160)
y = [a*x + b for x in x]
plt.plot(x, y, color='red')
plt.xlim(-10,160)
plt.ylim(-200000, 800000)
plt.title('W/S vs MTOGW')
plt.xlabel('W/S [lb/sqft]')
plt.ylabel('MTOGW [lb]')
plt.yticks([0, 200000, 400000, 600000, 800000])
plt.xticks([0, 40, 80, 120, 160])
plt.grid()
plt.show()

# Format is [MTOGW, Retardant Capacity [Gallons]]

BAE_146 = [84000, 3000] # British Aerospace 146
LHC130 = [175000, 3000] # Lockheed HC-130
CL215 = [43499, 1850] # Canadair CL-215
DC10 = [430000, 12000] # Douglas DC-10
B747 = [735000, 20000] # Boeing 747
GS2T = [26147, 800] # Grumman S2T Airtanker

# Line of Best Fit
x = [BAE_146[0], LHC130[0], CL215[0], DC10[0], B747[0], GS2T[0]]
y = [BAE_146[1], LHC130[1], CL215[1], DC10[1], B747[1], GS2T[1]]
[a, b] = np.polyfit(x, y, 1)


plt.plot(BAE_146[0], BAE_146[1], marker='o', color='black')
plt.annotate('British Aerospace 146', BAE_146, textcoords='offset points', xytext=(-30, 10), ha='center')


plt.plot(LHC130[0], LHC130[1], marker='o', color='black')
plt.annotate('Lockheed HC-130', LHC130, textcoords='offset points', xytext=(45, -3), ha='center')

plt.plot(CL215[0], CL215[1], marker='o', color='black')
plt.annotate('Canadair CL-215', CL215, textcoords='offset points', xytext=(-45, 0), ha='center')

plt.plot(DC10[0], DC10[1], marker='o', color='black')
plt.annotate('Douglas DC-10', DC10, textcoords='offset points', xytext=(-40, 2), ha='center')

plt.plot(B747[0], B747[1], marker='o', color='black')
plt.annotate('Boeing 747', B747, textcoords='offset points', xytext=(-30, 2), ha='center')

plt.plot(GS2T[0], GS2T[1], marker='o', color='black')
plt.annotate('Grumman S2T Airtanker', GS2T, textcoords='offset points', xytext=(50,-12), ha='center')

x = range(-400000, 1000000)
y = [a*x + b for x in x]
plt.plot(x, y, color='red')
plt.xlim(-300000, 800000)
plt.ylim(-5000, 25000)
plt.xticks([0, 200000, 400000, 600000, 800000])
plt.yticks([0, 5000, 10000, 15000, 20000, 25000])
plt.grid()
plt.title('MTOGW vs Retardant Capacity')
plt.xlabel('MTOGW [lb]')
plt.ylabel('Retardant Capacity [gal]')
plt.show()



# Format is [Empty Weight, MTOGW lb]

BAE_146 = [52510, 84000] # British Aerospace 146
LHC130 = [76700, 175000] # Lockheed HC-130
CL215 = [26808, 43499] # Canadair CL-215
DC10 = [240171, 430000] # Douglas DC-10
B747 = [412300, 735000] # Boeing 747
GS2T = [18316, 26147] # Grumman S2T Airtanker

# Line of Best Fit
x = [BAE_146[0], LHC130[0], CL215[0], DC10[0], B747[0], GS2T[0]]
y = [BAE_146[1], LHC130[1], CL215[1], DC10[1], B747[1], GS2T[1]]
[a, b] = np.polyfit(x, y, 1)


plt.plot(BAE_146[0], BAE_146[1], marker='o', color='black')
plt.annotate('British Aerospace 146', BAE_146, textcoords='offset points', xytext=(50, -5), ha='center')


plt.plot(LHC130[0], LHC130[1], marker='o', color='black')
plt.annotate('Lockheed HC-130', LHC130, textcoords='offset points', xytext=(-40, 3), ha='center')

plt.plot(CL215[0], CL215[1], marker='o', color='black')
plt.annotate('Canadair CL-215', CL215, textcoords='offset points', xytext=(-45, -5), ha='center')

plt.plot(DC10[0], DC10[1], marker='o', color='black')
plt.annotate('Douglas DC-10', DC10, textcoords='offset points', xytext=(-40, 2), ha='center')

plt.plot(B747[0], B747[1], marker='o', color='black')
plt.annotate('Boeing 747', B747, textcoords='offset points', xytext=(-30, 2), ha='center')

plt.plot(GS2T[0], GS2T[1], marker='o', color='black')
plt.annotate('Grumman S2T Airtanker', GS2T, textcoords='offset points', xytext=(50,-12), ha='center')

x = range(-400000, 1000000)
y = [a*x + b for x in x]
plt.plot(x, y, color='red')


plt.grid()
plt.xlim([-400000, 700000])
plt.ylim([-300000, 1000000])
plt.xticks([0, 200000, 400000, 600000])
plt.yticks([0, 200000, 400000, 600000, 800000, 1000000])
plt.title('Empty Weight vs. MTOGW')
plt.xlabel('Empty Weight [lb]')
plt.ylabel('MTOGW [lb]')
plt.show()



# Format is [MTOGW, Fuel Capacity [gal]]

BAE_146 = [84000, 3098]  # British Aerospace 146
LHC130 = [175000, 6700]  # Lockheed HC-130
CL215 = [43499, 1561.3]  # Canadair CL-215
DC10 = [430000, 36650]  # Douglas DC-10
B747 = [735000, 63094.853]  # Boeing 747
GS2T = [26147, 520]  # Grumman S2T Airtanker

# Line of Best Fit
x = [BAE_146[0], LHC130[0], CL215[0], DC10[0], B747[0], GS2T[0]]
y = [BAE_146[1], LHC130[1], CL215[1], DC10[1], B747[1], GS2T[1]]
[a, b] = np.polyfit(x, y, 1)


plt.plot(BAE_146[0], BAE_146[1], marker='o', color='black')
plt.annotate('British Aerospace 146', BAE_146, textcoords='offset points', xytext=(-35, 10), ha='center')


plt.plot(LHC130[0], LHC130[1], marker='o', color='black')
plt.annotate('Lockheed HC-130', LHC130, textcoords='offset points', xytext=(45, -3), ha='center')

plt.plot(CL215[0], CL215[1], marker='o', color='black')
plt.annotate('Canadair CL-215', CL215, textcoords='offset points', xytext=(-45, 0), ha='center')

plt.plot(DC10[0], DC10[1], marker='o', color='black')
plt.annotate('Douglas DC-10', DC10, textcoords='offset points', xytext=(-40, 2), ha='center')

plt.plot(B747[0], B747[1], marker='o', color='black')
plt.annotate('Boeing 747', B747, textcoords='offset points', xytext=(-30, 2), ha='center')

plt.plot(GS2T[0], GS2T[1], marker='o', color='black')
plt.annotate('Grumman S2T Airtanker', GS2T, textcoords='offset points', xytext=(50,-12), ha='center')

x = range(-400000, 1000000)
y = [a*x + b for x in x]
plt.plot(x, y, color='red')

plt.grid()
plt.xlim([-400000, 1000000])
plt.ylim([-40000, 80000])
plt.yticks([0, 20000, 40000, 60000, 80000])
plt.xticks([0, 200000, 400000, 600000, 800000, 1000000])
plt.title('MTOGW vs Fuel Capacity')
plt.xlabel('MTOGW [lb]')
plt.ylabel('Fuel Capacity [gal]')
plt.show()