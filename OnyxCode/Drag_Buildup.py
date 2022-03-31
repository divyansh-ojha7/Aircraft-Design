"""
DRAG BUILDUP
2/25/22
"""

from Tail_Sizing import *

mu = 1.789 * (10**-5)  # dynamic viscosity at sea level
Re = (rho_airport * v_cruise * c_ave) / mu  # Reynold's number
M = 0.65  # Mach number, estimation
l_fuse = 1  # length of fuselage
A_f_max = 1  # maximum cross-sectional area of fuselage

Cf = 0.455 / ((math.log(Re,10)**2.58) * (1 + 0.144*M**2)**0.65)  # Flat Plate Skin Friction Coefficient for turbulent flow

f_fuse = l_fuse / math.sqrt((4/math.pi)*A_f_max)
FF = (0.9 + (5/(f_fuse**1.5)) + (f_fuse/400))  # Form factor, used for fuselage in drag buildup


