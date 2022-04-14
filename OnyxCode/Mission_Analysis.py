"""
MISSION ANALYSIS
4/8/22
"""
from SimAircrafts_Graphs import *



cruise_alt = 15000  # cruise altitude, m
airport_alt = 39  # LAX altitude, m
a1 = -6.5e-3  # Temperature lapse rate below 11 km, in deg K/m
Temp0 = 288.15  # Temperature at Sea Level, Kelvin
h0 = 0  # Altitude at Sea Level, m
Ratm = 287  # ideal gas constant J/(kg*K)
gamma_atm = 1.4  # ratio of specific heats
Beta = 1.458e-6  # kg/(s*m*sqrt(K)) from 1976 US standard atmosphere, page 19
Suth = 110.4  # deg K, Sutherland's constant, from 1976 US standard atmosphere, page 1

Tcruise = Temp0 + (cruise_alt*a1)  # Calculate temperature at cruise altitude based on lapse rate
Tairport = 287.51  # Calculate temperature at airport altitude based on lapse rate
rhocruise = rho_0*(Tcruise/Temp0)**(-g/(a1*Ratm)-1) # Calculate density at cruise altitude
# based on standard atmosphere formula
rhoairport = 47.5192035  # Calculate density at cruise altitude based on standard atmosphere formula (kg/m^2)
mucruise = (Beta*Tcruise**(3/2))/(Tcruise+Suth)  # Dynamic viscosity from 1976 US standard atmosphere, page 19,
# eq 51.... Valid below 86 km
muairport = (Beta*Tairport**(3/2))/(Tairport+Suth)  # Dynamic viscosity from 1976 US standard atmosphere, page 19,
# eq 51.... Valid below 86 km

print(f'Tcruise = {Tcruise:.4g} ## cruise temperature (deg K)')
print(f'Tairport = {Tairport:.4g} ## airport temperature (deg K)')
print(f'rhocruise = {rhocruise:.4g} ## cruise density (kg/m^3)')
print(f'rhoairport = {rhoairport:.4g} ## airport density (kg/m^3)')
print(f'mucruise = {mucruise:.4g} ## cruise viscosity (kg/m^3)')
print(f'muairport = {muairport:.4g} ## airport viscosity (kg/m^3)')
print(f'tsfc = {tsfc}')

Ta_airport = 253548.63  # Thrust of engine in Newtons
#NOTE: TSFC UNITS MAY BE ISSUE

n_takeoff = 1.15 # takeoff load factor (typically 1.15)
v_LO = 1.2*v_stall  # Lift-off Velocity
takeoffclimbangle = 5 # gamma (deg) typically 5 deg.
mu_roll = 0.04  # coefficient of rolling friction
alpha_wheelsdown = 5 # angle of attack when wheels on runway (deg)
L_TO = 0.5*rho_0*((0.7*v_LO)**2)*S*Cl[35]
D_TO = 0.5*rho_0*((0.7*v_LO)**2)*S*(c_d_0 + k*(Cl[35]**2))



#SELF CODE
# TAKEOFF
L_TO = 0.5*rho_0*((0.7*v_LO)**2)*S*Cl[35]
D_TO = 0.5*rho_0*((0.7*v_LO)**2)*S*(c_d_0 + k*(Cl[35]**2))
Sg_takeoff = (1.44*(W**2)) / ((g*rho_0*S*cl_max)*(Ta_airport - D_TO - mu_roll*(W - L_TO)))
print(f'Sg_takeoff = {Sg_takeoff} m')




