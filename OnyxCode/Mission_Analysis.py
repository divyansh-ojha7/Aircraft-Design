"""
MISSION ANALYSIS
4/8/22
"""
from SimAircrafts_Graphs import *

print('########################################')
print('       RUNNING MISSION ANALYSIS         ')
print('########################################')
print(' ')

m_zero_ret = 36801.38 + 10372.1712538  # mass with no retardant, 36801.38 kg (EMPTY WEIGHT) + 10372.1712538 kg (FUEL)
W_zero_ret = m_zero_ret * 9.81 # weight with no retardant

cruise_alt = 5181.6  # cruise altitude, m, used to be 6096
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

print(f'Tcruise = {Tcruise:.4g} - cruise temperature (deg K)')
print(f'Tairport = {Tairport:.4g} - airport temperature (deg K)')
print(f'rhocruise = {rhocruise:.4g} - cruise density (kg/m^3)')
print(f'rhoairport = {rhoairport:.4g} - airport density (kg/m^3)')
print(f'mucruise = {mucruise:.4g} - cruise viscosity (kg/m^3)')
print(f'muairport = {muairport:.4g} - airport viscosity (kg/m^3)')
print(f'tsfc = {tsfc} - thrust specific fuel consumption (kg/(N*s))')

Ta_airport = 253548.63  # Thrust of engine in Newtons
#NOTE: TSFC UNITS MAY BE ISSUE

n_takeoff = 1.15 # takeoff load factor (typically 1.15)
v_LO = 1.2*v_stall  # Lift-off Velocity
takeoffclimbangle = 5 # gamma (deg) typically 5 deg.
mu_roll = 0.04  # coefficient of rolling friction
alpha_wheelsdown = 5 # angle of attack when wheels on runway (deg)
L_TO = 0.5*rho_0*((0.7*v_LO)**2)*S*Cl[35]
D_TO = 0.5*rho_0*((0.7*v_LO)**2)*S*(c_d_0 + k*(Cl[35]**2))
Sg_takeoff = (1.44*(W_zero_ret**2)) / ((g*rho_0*S*cl_max)*(Ta_airport - D_TO - mu_roll*(W_zero_ret - L_TO)))
R_takeoffpullup = (1.2**2)*(v_stall**2) / (0.15*g)  # radius of pull-up maneuver (m)
Str = R_takeoffpullup*math.sin(math.radians(takeoffclimbangle)) # distance for transition to flight (m)
Htr = R_takeoffpullup - R_takeoffpullup*math.cos(math.radians(takeoffclimbangle))  # height for transition to flight (m)
Sa = (35 - R_takeoffpullup + R_takeoffpullup*math.cos(math.radians(takeoffclimbangle))) / math.tan(math.radians(takeoffclimbangle))
# climb distance to clear 35' (10.7 m) obstacle (if positive)
s_takeoff = Sg_takeoff + Str + Sa  # total takeoff distance

print(f'Sg_takeoff = {Sg_takeoff} m - takeoff ground distance')
print(f'Str = {Str} m - transition distance')
print(f'Sa = {Sa} m - takeoff climb distnace')
print(f's_takeoff = {s_takeoff} m - total takeoff distance')

# CLIMB ANALYSIS

# Max ROC airport
Z_fact_airport = 1 + math.sqrt(1 + (3 / ((eff ** 2) * ((Ta_airport / W_zero_ret) ** 2))))
ROC_max_airport = (((W_zero_ret/S) * Z_fact_airport) / (3 * rho_airport * c_d_0)) ** 0.5 * ((Ta_airport / W_zero_ret) ** 1.5) * (1 - (Z_fact_airport / 6) - (3 / (2 * ((Ta_airport / W_zero_ret) ** 2) * (eff ** 2) * Z_fact_airport)))
Ta_cruise = Ta_airport*(rhocruise / rho_airport)  # Thrust available, max (cruise altitude) (N)
Z_fact_cruise = 1 + math.sqrt(1 + (3 / ((eff ** 2) * ((Ta_cruise / W_zero_ret) ** 2))))
ROC_max_cruise = (((W_zero_ret/S) * Z_fact_cruise) / (3 * rhocruise * c_d_0)) ** 0.5 * ((Ta_cruise / W_zero_ret) ** 1.5) * (1 - (Z_fact_cruise / 6) - (3 / (2 * ((Ta_cruise / W_zero_ret) ** 2) * (eff ** 2) * Z_fact_cruise)))

ROC_average = (ROC_max_airport + ROC_max_cruise) / 2

d_climb = (cruise_alt-airport_alt) / (math.tan(math.radians(takeoffclimbangle)))  # ground distance of climb, m
t_climb = d_climb / ROC_average  # time climb takes, s

m_fuelburn_climb = tsfc * ((Ta_airport + Ta_cruise) / 2) * t_climb  # mass of fuel used in climb, kg

print(f'ROC_average = {ROC_average} m/s')
print(f'd_climb = {d_climb / 1000} km')
print(f't_climb = {t_climb / 60} min')
print(f'm_fuelburn_climb = {m_fuelburn_climb} kg')

# CRUISE ANALYSIS
m0_cruise = m_zero_ret - m_fuelburn_climb  # current amount of fuel at beginning of cruise, kg
W0_cruise = m0_cruise*9.81
d_cruise = 5556000  # objective cruise distance, m. Equal to 3000 n mi
W_cruise_final = (((-d_cruise*(g/2)*tsfc) / (math.sqrt(2/(rhocruise*S))*eff_12)) + math.sqrt(W0_cruise))**2
# weight of aircraft after cruise
m_cruise_final = W_cruise_final / 9.81  # mass of aircraft after cruise

W_fuelburn_cruise = W0_cruise - W_cruise_final
m_fuelburn_cruise = W_fuelburn_cruise / 9.81

print(f'm_fuelburn_cruise = {m_fuelburn_cruise} kg')

