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

starting_fuel = 10372.1712538  # kg of starting fuel
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
print(f'v_cruise = {v_cruise} m/s')

# CRUISE ANALYSIS
m0_cruise = m_zero_ret - m_fuelburn_climb  # current amount of fuel at beginning of cruise, kg
W0_cruise = m0_cruise*9.81
d_cruise = 3546967  # objective cruise distance, m.
W_cruise_final = (((-d_cruise*(g/2)*tsfc) / (math.sqrt(2/(rhocruise*S))*eff_12)) + math.sqrt(W0_cruise))**2
# weight of aircraft after cruise
m_cruise_final = W_cruise_final / 9.81  # mass of aircraft after cruise

W_fuelburn_cruise = W0_cruise - W_cruise_final
m_fuelburn_cruise = W_fuelburn_cruise / 9.81

print(f'm_fuelburn_cruise = {m_fuelburn_cruise} kg')

#  DESCENT ANALYSIS

theta_approach = 3  # 3 degree slope for descent
v_approach = 1.3*v_stall  # approach velocity, m/s
v_loiter = math.sqrt((2/rhocruise)*(W_cruise_final/S)*math.sqrt(k/c_d_0))

T_req_top_descent = 0.5*rhocruise*(v_loiter**2)*S*c_d_0 + (k*W_cruise_final)/(0.5*rhocruise*(v_loiter**2)*S)
P_req_top_descent = T_req_top_descent*v_loiter

T_req_approach = 0.5*rhocruise*(v_approach**2)*S*c_d_0 + (k*W_cruise_final)/(0.5*rhocruise*(v_approach**2)*S)
P_req_approach = T_req_approach*v_loiter

T1 = W_cruise_final*math.sin(math.radians(theta_approach)) + T_req_top_descent
T2 = W_cruise_final*math.sin(math.radians(theta_approach)) + T_req_approach
fuel_flowrate_descent = ((T1+T2)/2)*tsfc

t_descent = cruise_alt / (v_loiter*math.sin(math.radians(theta_approach)))
m_fuelburn_descent = fuel_flowrate_descent*t_descent

d_descent = cruise_alt / math.tan(math.radians(3))  # distance of descent on ground, m

print(f'fuel_flowrate_descent = {fuel_flowrate_descent} kg')
print(f'v_loiter = {v_loiter} m/s')
print(f'd_descent = {d_descent / 1000} km')
print(f't_descent = {t_descent / 60} min')
print(f'm_fuelburn_descent = {m_fuelburn_descent} kg')

m_fuelburn_total_ferry = m_fuelburn_climb + m_fuelburn_cruise + m_fuelburn_descent

print(f'm_fuelburn_total_ferry = {m_fuelburn_total_ferry} kg for a ferry mission of {(d_climb + d_cruise + d_descent) / 1000} km')

fuel_remaining = starting_fuel - m_fuelburn_total_ferry
print(f'fuel_remaining = {fuel_remaining: .8g} kg, which is {(fuel_remaining / starting_fuel)*100: .8g}% of starting fuel')

# Notes
# 5398900 m cruise distance for 3000 n mi total ferry distance
# 3546967 m cruise distance for 2000 n mi total ferry distance
# 1694699 m cruise distance for 1000 n mi total ferry distance


# DESIGN MISSION
m_retardant = 39846.493059  # kg of retardant
n_drops = 4  # number of drops
drop_amount = m_retardant / n_drops  # amount of retardant dropped per drop, kg
print(f'n_drops = {n_drops}')

# Climb Analysis
Z_fact_airport_des = 1 + math.sqrt(1 + (3 / ((eff ** 2) * ((Ta_airport / W) ** 2))))
ROC_max_airport_des = (((W/S) * Z_fact_airport_des) / (3 * rho_airport * c_d_0)) ** 0.5 * ((Ta_airport / W) ** 1.5) * (1 - (Z_fact_airport_des / 6) - (3 / (2 * ((Ta_airport / W) ** 2) * (eff ** 2) * Z_fact_airport_des)))
Ta_cruise = Ta_airport*(rhocruise / rho_airport)  # Thrust available, max (cruise altitude) (N)
Z_fact_cruise_des = 1 + math.sqrt(1 + (3 / ((eff ** 2) * ((Ta_cruise / W) ** 2))))
ROC_max_cruise_des = (((W/S) * Z_fact_cruise_des) / (3 * rhocruise * c_d_0)) ** 0.5 * ((Ta_cruise / W) ** 1.5) * (1 - (Z_fact_cruise_des / 6) - (3 / (2 * ((Ta_cruise / W) ** 2) * (eff ** 2) * Z_fact_cruise_des)))

ROC_average_des = (ROC_max_airport_des + ROC_max_cruise_des) / 2

d_climb_des = (cruise_alt-airport_alt) / (math.tan(math.radians(takeoffclimbangle)))  # ground distance of climb, m
t_climb_des = d_climb_des / ROC_average_des  # time climb takes, s

m_fuelburn_climb_des = tsfc * ((Ta_airport + Ta_cruise) / 2) * t_climb_des  # mass of fuel used in climb, kg

print(f'm_fuelburn_climb_des = {m_fuelburn_climb_des} kg')

# Cruise Analysis
m0_cruise_des = m_takeoff - m_fuelburn_climb_des  # current amount of fuel at beginning of cruise, kg
W0_cruise_des = m0_cruise_des*9.81
d_cruise_des = 740800  # objective cruise distance, m. 400 Nautical Miles
W_cruise_final_des = (((-d_cruise_des*(g/2)*tsfc) / (math.sqrt(2/(rhocruise*S))*eff_12)) + math.sqrt(W0_cruise_des))**2
# weight of aircraft after cruise
m_cruise_final_des = W_cruise_final_des / 9.81  # mass of aircraft after cruise

W_fuelburn_cruise_des = W0_cruise_des - W_cruise_final_des
m_fuelburn_cruise_des = W_fuelburn_cruise_des / 9.81

print(f'm_fuelburn_cruise_des = {m_fuelburn_cruise_des} kg')

# Descent Analysis

v_loiter_des = math.sqrt((2/rhocruise)*(W_cruise_final_des/S)*math.sqrt(k/c_d_0))

T_req_top_descent_des = 0.5*rhocruise*(v_loiter_des**2)*S*c_d_0 + (k*W_cruise_final_des)/(0.5*rhocruise*(v_loiter_des**2)*S)

T_req_approach_des = 0.5*rhocruise*(v_approach**2)*S*c_d_0 + (k*W_cruise_final_des)/(0.5*rhocruise*(v_approach**2)*S)

T1_des = W_cruise_final_des*math.sin(math.radians(theta_approach)) + T_req_top_descent_des
T2_des = W_cruise_final_des*math.sin(math.radians(theta_approach)) + T_req_approach_des
fuel_flowrate_descent_des = ((T1_des+T2_des)/2)*tsfc

t_descent = cruise_alt / (v_loiter*math.sin(math.radians(theta_approach)))
m_fuelburn_descent_des = fuel_flowrate_descent_des*t_descent

print(f'm_fuelburn_descent_des = {m_fuelburn_descent_des} kg')

# Retardant Dropping Phase
m_descent_final_des = m_takeoff - m_fuelburn_climb_des - m_fuelburn_cruise_des - m_fuelburn_descent_des
W_descent_final_des = m_descent_final_des * 9.81

m_current = m_descent_final_des
for i in range(1, n_drops+1):
    m_after_drop = m_current - drop_amount
    W_after_drop = m_after_drop * 9.81

    # Quick Loiter
    d_loiter = 1852  # objective cruise distance, m. 1 Nautical Mile
    W_loiter_final = (((-d_loiter * (g / 2) * tsfc) / (math.sqrt(2 / (rhocruise * S)) * eff_12)) + math.sqrt(
        W_after_drop)) ** 2
    # weight of aircraft after cruise
    m_loiter_final = W_loiter_final / 9.81  # mass of aircraft after cruise

    W_fuelburn_loiter = W_after_drop - W_loiter_final
    m_fuelburn_loiter = W_fuelburn_loiter / 9.81

    m_current = m_loiter_final - m_fuelburn_loiter

m_after_all_drops = m_current
W_after_all_drops = m_current * 9.81

m_fuelburn_drops = m_descent_final_des - m_after_all_drops - m_retardant

print(f'm_fuelburn_drops = {m_fuelburn_drops} kg')

# Climb analysis
Z_fact_after_drops = 1 + math.sqrt(1 + (3 / ((eff ** 2) * ((Ta_airport / W_after_all_drops) ** 2))))
ROC_max_after_drops = (((W_after_all_drops/S) * Z_fact_after_drops) / (3 * rho_airport * c_d_0)) ** 0.5 * ((Ta_airport / W_after_all_drops) ** 1.5) * (1 - (Z_fact_after_drops / 6) - (3 / (2 * ((Ta_airport / W_after_all_drops) ** 2) * (eff ** 2) * Z_fact_after_drops)))
Ta_cruise = Ta_airport*(rhocruise / rho_airport)  # Thrust available, max (cruise altitude) (N)
Z_fact_cruise_afterdrops = 1 + math.sqrt(1 + (3 / ((eff ** 2) * ((Ta_cruise / W_after_all_drops) ** 2))))
ROC_max_cruise_afterdrops = (((W_after_all_drops/S) * Z_fact_cruise_afterdrops) / (3 * rhocruise * c_d_0)) ** 0.5 * ((Ta_cruise / W_after_all_drops) ** 1.5) * (1 - (Z_fact_cruise_afterdrops / 6) - (3 / (2 * ((Ta_cruise / W_after_all_drops) ** 2) * (eff ** 2) * Z_fact_cruise_afterdrops)))

ROC_average_afterdrops = (ROC_max_after_drops + ROC_max_cruise_afterdrops) / 2

d_climb_afterdrops = (cruise_alt-airport_alt) / (math.tan(math.radians(takeoffclimbangle)))  # ground distance of climb, m
t_climb_afterdrops = d_climb_afterdrops / ROC_average_afterdrops  # time climb takes, s

m_fuelburn_climb_afterdrops = tsfc * ((Ta_airport + Ta_cruise) / 2) * t_climb_afterdrops  # mass of fuel used in climb, kg

print(f'm_fuelburn_climb_afterdrops = {m_fuelburn_climb_afterdrops} kg')

# Cruise Analysis
m0_cruise_afterdrops = m_after_all_drops - m_fuelburn_climb_afterdrops  # current amount of fuel at beginning of cruise, kg
W0_cruise_afterdrops = m0_cruise_afterdrops*9.81
d_cruise_afterdrops = 740800  # objective cruise distance, m. 400 Nautical Miles
W_cruise_final_afterdrops = (((-d_cruise_afterdrops*(g/2)*tsfc) / (math.sqrt(2/(rhocruise*S))*eff_12)) + math.sqrt(W0_cruise_afterdrops))**2
# weight of aircraft after cruise
m_cruise_final_afterdrops = W_cruise_final_afterdrops / 9.81  # mass of aircraft after cruise

W_fuelburn_cruise_afterdrops = W0_cruise_afterdrops - W_cruise_final_afterdrops
m_fuelburn_cruise_afterdrops = W_fuelburn_cruise_afterdrops / 9.81

print(f'm_fuelburn_cruise_afterdrops = {m_fuelburn_cruise_afterdrops} kg')

# Descent Analysis
v_loiter_afterdrops = math.sqrt((2/rhocruise)*(W_cruise_final_afterdrops/S)*math.sqrt(k/c_d_0))

T_req_top_descent_afterdrops = 0.5*rhocruise*(v_loiter_afterdrops**2)*S*c_d_0 + (k*W_cruise_final_afterdrops)/(0.5*rhocruise*(v_loiter_afterdrops**2)*S)

T_req_approach_afterdrops = 0.5*rhocruise*(v_approach**2)*S*c_d_0 + (k*W_cruise_final_afterdrops)/(0.5*rhocruise*(v_approach**2)*S)

T1_afterdrops = W_cruise_final_afterdrops*math.sin(math.radians(theta_approach)) + T_req_top_descent_afterdrops
T2_afterdrops = W_cruise_final_des*math.sin(math.radians(theta_approach)) + T_req_approach_afterdrops
fuel_flowrate_descent_afterdrops = ((T1_afterdrops+T2_afterdrops)/2)*tsfc

t_descent = cruise_alt / (v_loiter*math.sin(math.radians(theta_approach)))
m_fuelburn_descent_afterdrops = fuel_flowrate_descent_afterdrops*t_descent

print(f'm_fuelburn_descent_afterdrops = {m_fuelburn_descent_afterdrops} kg')

# SUMMING TOTAL AND DATA ANALYSIS FOR DESIGN MISSION
print(f'n_drops = {n_drops}')
total_fuelburn_des = m_fuelburn_climb_des + m_fuelburn_cruise_des + m_fuelburn_descent_des + m_fuelburn_drops + m_fuelburn_climb_afterdrops + m_fuelburn_cruise_afterdrops
print(f'total_fuelburn_des = {total_fuelburn_des} kg')
print(f'Fuel remaining after design mission with {n_drops} drops: {starting_fuel - total_fuelburn_des} kg')
print(f'Percent fuel remaining after design mission with {n_drops} drops: {((starting_fuel - total_fuelburn_des) / starting_fuel)*100}%')
