"""
Tail Sizing
2/22/22
"""

from Intermediate_Value import *

C_HT = (0.91+1) / 2  # Hz. Sizing Coefficient
V_HT = (0.083+0.09) / 2  # Vt. Sizing Coefficient
c_ave = (c_tip + c_root) / 2  # average wing chord
AR_h = 4  # aspect ratio of horizontal tail
AR_v = 1.65  # aspect ratio of vertical tail
SM = 0.1  # stability margin, 0.1 is a little better than weakly stable, but we don't want it too stable

x_np = (0.25 + ((1+(2/AR))/(1+(2/AR_h)))*(1-(4/(AR+2)))*C_HT)*c_ave  # position of neutral point (m)
x_cg = x_np - (c_ave*SM)  # position of center of gravity (m)

print(f'x_np = {x_np} m')
print(f'x_cg = {x_cg} m')