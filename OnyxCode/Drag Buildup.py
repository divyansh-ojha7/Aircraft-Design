"""
DRAG BUILDUP
2/25/22
"""

from Tail_Sizing import *

mu = 1.789 * (10**-5)  # dynamic viscosity at sea level
Re = (rho_airport * v_cruise * c_ave) / mu  # Reynold's number
M = 0.65  # Mach number, estimation

Cf = 0.455 / ((math.log(Re,10)**2.58) * (1 + 0.144*M**2)**0.65)  # Flat Plate Skin Friction Coefficient for turbulent flow
