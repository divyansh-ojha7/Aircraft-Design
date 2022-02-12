"""
Intermediate Values
2/12/22
"""

from Wing_Sizing import *

#2D Analysis
a0 = avscl_data[0]
alpha_l0 = avscl_data[1]



#Efficiency Ratios

eff_32 = 3**(3/4) / (4*c_d_0**(1/4)*k**(3/4))  # 3/2 Efficiency Ratio
eff = math.sqrt(1 / (4*k*c_d_0))  # Cl/Cd Efficiency Ratio
eff_12 = 0.75 * (1 / 3*k*(c_d_0**3))**(1/4)  # 1/2 Efficiency Ratio

v_max_range = math.sqrt((2*(m_takeoff*g) / (rho_0*S_to) * math.sqrt(k / c_d_0)))

