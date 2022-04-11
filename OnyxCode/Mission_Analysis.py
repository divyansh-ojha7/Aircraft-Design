"""
MISSION ANALYSIS
4/8/22
"""
from SimAircrafts_Graphs import *

T0 = 253548.63  # Thrust of engine in Newtons

# TAKEOFF
v_LO = 1.2*v_stall  # Lift-off Velocity

mu_roll = 0.04  # coefficient of rolling friction

takeoff_A = g*((T0/W) - mu_roll)
takeoff_B = (g/W)*(0.5*rho_0*S*(Cd_3D[33] - mu_roll*Cl_3D[33])


