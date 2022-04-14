"""
MISSION ANALYSIS
4/8/22
"""
from SimAircrafts_Graphs import *

T0 = 253548.63  # Thrust of engine in Newtons

# TAKEOFF
v_LO = 1.2*v_stall  # Lift-off Velocity
mu_roll = 0.04  # coefficient of rolling friction

L_TO = 0.5*rho_0*((0.7*v_LO)**2)*S*Cl[35]
D_TO = 0.5*rho_0*((0.7*v_LO)**2)*S*(c_d_0 + k*(Cl[35]**2))

Sg_takeoff = (1.44*(W**2)) / ((g*rho_0*S*cl_max)*(T0 - D_TO - mu_roll*(W - L_TO)))
print(f'Sg_takeoff = {Sg_takeoff}')

