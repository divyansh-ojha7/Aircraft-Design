# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 16:43:48 2022


@author: ndenn
https://www.fzt.haw-hamburg.de/pers/Scholz/dimensionierung/start.htm
https://eng.libretexts.org/Bookshelves/Aerospace_Engineering/Aerodynamics_and_Aircraft_Performance_(Marchman)/09%3A_The_Role_of_Performance_in_Aircraft_Design-_Constraint_Analysis
"""
import math

from Design_Variables import *

# Range
m_mto_s_w = []
r = range(1, 2001)
for num in r:
    m_mto_s_w.append(num)

# Landing Field Length
lfl_factor = (k_l * (rho_airport / rho_0) * cl_max * s_lfl) / (m_landing / m_takeoff)

# Takeoff Field Length
tkff_fld_func = [(k_to * x) / (s_tofl * (rho_airport / rho_0) * cl_max) for x in m_mto_s_w]

# Climb
c_d = c_d_0 + c_d_flap + c_d_lgear + (cl_to ** 2 / (math.pi * AR * 0.85))
l_d = cl_to / c_d

clmb_factor = (n / (n - 1)) * ((1 / l_d) + math.sin(math.radians((theta_climb))))

# Missed Climb
msd_climb_factor = ((n / (n - 1)) * ((1 / l_d) + math.sin(math.radians((theta_climb))))) * (m_landing / m_takeoff)

# Cruise
q_inf = 0.5 * rho_0 * (v_cruise ** 2)
k = 1 / (math.pi * e * AR)
cruise_func = [(((q_inf * c_d_0) / x) + ((k / q_inf) * x)) for x in m_mto_s_w]

# Plot
plt.plot(m_mto_s_w, tkff_fld_func, label='Takeoff', color='orange')
plt.plot(m_mto_s_w, cruise_func, label='Cruise', color='black')

plt.axvline(x=lfl_factor, label='Landing', color='green')
plt.axhline(y=clmb_factor, label='Climb', color='purple')
plt.axhline(y=msd_climb_factor, label='Missed Climb', color='#25C2DE')

# Find where they intersect
y_int = lfl_factor
#for val in range(1, 2000):
    #if lfl_factor - cruise_func[val] < 0.00001:
        #y_int = val

plt.plot(lfl_factor, cruise_func[math.floor(lfl_factor)], 'o', markersize=10, color='red', label='Design Point')

# Formatting
plt.title('Wing Loading vs. Thrust to Weight Ratio')
plt.xlabel('$\dfrac{W}{S}$ $\: (\dfrac{kg}{m^2})$')
# $\dfrac{m_{MTO}}{S_W}$
plt.ylabel('$\dfrac{T}{W}$ $\: (\dfrac{N}{kg})$')
# $\dfrac{T_{TO}}{m_{MTO}*g}$
plt.legend(framealpha=1, loc='upper right')

ax = plt.gca()
ax.set_ylim([0, 1])
ax.set_xlim([0, 1500])

# Wing area
S = m_takeoff / lfl_factor  # Wing area using takeoff mass
S_la = m_landing / lfl_factor  # Wing area using landing mass
S_average = ((m_takeoff + m_landing) / 2) / lfl_factor

# Wing span
b = math.sqrt(AR * S)

# Print results
print(f'\nlfl_factor = {lfl_factor}, which is ideal wing loading')
print(f'S = {S} m^2')
print(f'b = {b} m')
if show_graphs == 'Y':
    plt.show()