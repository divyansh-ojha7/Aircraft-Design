"""
Design Variables
2/11/22
"""
from Airfoil_Analysis import *

g = 9.81  # gravity
rho_0 = 1.225  # sea level air density
rho_airport = 1.2  # airport air density
k_l = 0.107  # kg/m^3
k_to = 2.34  # m^3/kg
cl_max = max(Cl)  # from Onyx program
cl_to = Cl[35]  # cl at takeoff, at whatever angle the wing is on the ground, estimated as 6 deg
c_d_0 = min(Cd)
s_lfl = 1470  # landing field length,
s_tofl = 2336  # takeoff field length,
m_takeoff = 87020.04431  # takeoff mass
# 39846.493059 kg (RETARDANT) + 26286.7 kg (EMPTY WEIGHT) + 10372.1712538 kg (FUEL)
m_landing = m_takeoff*0.82  # landing mass, 82% of takeoff mass
c_d_flap = 0.02  # estimation
c_d_lgear = 0.015  # estimation
AR = 9  # aspect ratio, taken off of BAE-146
e = 0.85
n = 2  # number of engines
theta_climb = 9.5  # estimation
v_cruise = 222.626  # m/s taken from bae-146
c_root = 7.6  # m root wing chord
c_tip = 3.13  # m tip wing chord
L_HT = 34.59  # m length from estimated C.G. to 1/4 chord of horiz. tail
L_VT = 28.55  # m length from estimated C.G. to 1/4 chord of vert. tail