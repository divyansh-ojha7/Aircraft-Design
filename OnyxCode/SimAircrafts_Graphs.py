"""
GRAPHING FOR SIMILAR AIRCRAFTS
3/29/22
"""

from Drag_Buildup import *


# Format is [MTOW [lbs], AR]
BAE_146 = [84000, 8.98] # British Aerospace 146
LHC130 = [175000, 10.1] # Lockheed HC-130
CL215 = [43499 ,8.15] # Canadair CL-215
DC10 = [430000, 6.91] # Douglas DC-10
B747 = [735000, 8.4] # Boeing 747
GS2T = [26147, 10.863] # Grumman S2T Airtanker


plt.plot(BAE_146[0], BAE_146[1], marker='o')
plt.annotate('British Aerospace 146', BAE_146, textcoords='offset points', xytext=(0,10), ha='center')

plt.plot(LHC130[0], LHC130[1], marker='o')
plt.annotate('Lockheed HC-130', LHC130, textcoords='offset points', xytext=(0,10), ha='center')

plt.plot(CL215[0], CL215[1], marker='o')
plt.annotate('Canadair CL-215', CL215, textcoords='offset points', xytext=(0,10), ha='center')

plt.plot(DC10[0], DC10[1], marker='o')
plt.annotate('Douglas DC-10', DC10, textcoords='offset points', xytext=(0,10), ha='center')

# plt.plot(B747[0], B747[1], marker='o')
# plt.annotate('Boeing 747', B747, textcoords='offset points', xytext=(0,10), ha='center')

plt.plot(GS2T[0], GS2T[1], marker='o')
plt.annotate('Grumman S2T Airtanker', GS2T, textcoords='offset points', xytext=(0,10), ha='center')

plt.title('MTOW vs Aspect Ratio')
plt.ylabel('Aspect Ratio')
plt.xlabel('MTOW (lbs)')
plt.xlim(0,1000000)
plt.show()
