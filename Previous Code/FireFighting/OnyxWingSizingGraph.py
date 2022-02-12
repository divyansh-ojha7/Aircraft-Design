# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 16:43:48 2022


@author: ndenn
https://www.fzt.haw-hamburg.de/pers/Scholz/HOOU/AircraftDesign_5_PreliminarySizing.pdf
"""
import math
import matplotlib.pyplot as plt
import numpy as np



#Design Variables
rho_0 = 1.225 #sea level air density
rho_airport = 1.2 #airport air density
k_l = 0.107 #kg/m^3
k_to = 2.34 #m^3/kg
cl_max = 1.8116 #from Onyx program
cl_to = 1.2872 #cl at takeoff, at whatever angle the wing is on the ground, estimated as 6 deg
c_d_0 = 0.00617941 #from Onyx Program
s_lfl = 1470 #landing field length,
s_tofl = 2336 #takeoff field length,
m_landing = 56898.427 #landing mass, 82% of takeoff mass
m_takeoff = 69388.326 #takeoff mass
c_d_flap = 0.02 #estimation
c_d_lgear = 0.015 #estimation
AR = 8.91 #aspect ratio, taken off of BAE-146
e = 0.85
n = 2 #number of engines
theta_climb = 12 #estimation
v_cruise = 222.626 #m/s taken from bae-146

#Range
m_mto_s_w = []
r = range(1, 2001)
for num in r:
    m_mto_s_w.append(num)

#Landing Field Length
lfl_factor = (k_l*(rho_airport/rho_0)*cl_max*s_lfl) / (m_landing/m_takeoff)

#Takeoff Field Length
tkff_fld_func = [(k_to*x)/(s_tofl*(rho_airport/rho_0)*cl_max) for x in m_mto_s_w]

#Climb
c_d = c_d_0 + c_d_flap + c_d_lgear + (cl_to**2 / (math.pi * AR * 0.85))
l_d = cl_to / c_d

clmb_factor = (n / (n-1)) * ((1 / l_d) + math.sin(math.radians((theta_climb))))

#Missed Climb
msd_climb_factor = ((n / (n-1)) * ((1 / l_d) + math.sin(math.radians((theta_climb))))) * (m_landing / m_takeoff)

#Cruise
q_inf = 0.5*rho_0*(v_cruise**2)
k = 1 / (math.pi*e*AR)
cruise_func = [(((q_inf*c_d_0)/x) + ((k/q_inf)*x)) for x in m_mto_s_w]

#Plot
plt.plot(m_mto_s_w, tkff_fld_func, label = 'Takeoff', color = 'orange')
plt.plot(m_mto_s_w, cruise_func, label = 'Cruise', color = 'black')

plt.axvline(x=lfl_factor, label = 'Landing', color = 'green')
plt.axhline(y=clmb_factor, label = 'Climb', color = 'purple')
plt.axhline(y=msd_climb_factor, label = 'Missed Climb', color = '#25C2DE')

#Find where they intersect
for val in range(1,2000):
    if clmb_factor - cruise_func[val] < 0.00001:
        x_int = val

plt.plot(x_int,cruise_func[x_int], '.', markersize=15, label = 'Design Point', color='red')

#Formatting
plt.title('Wing Loading vs. Thrust to Weight Ratio')
# plt.xlabel('$\dfrac{m_{MTO}}{S_W}$')
# plt.ylabel('$\dfrac{T_{TO}}{m_{MTO}*g}$')
plt.xlabel('$\dfrac{W}{S}$ $\: (\dfrac{kg}{m^2})$')
plt.ylabel('$\dfrac{T}{W}$ $\: (\dfrac{N}{kg})$')
plt.legend(framealpha = 1, loc = 'upper right')

ax = plt.gca()
ax.set_ylim([0, 1])
ax.set_xlim([0, 1500])
#Print results
print(f'The design point is at ({x_int}, {cruise_func[x_int]}).\nThe ideal wing loading is {x_int} m^2.')

test = []
for x in range(0, 2000):
    test.append(lfl_factor)
    # idx = np.argwhere(np.diff(np.sign(test[x] - cruise_func[x]))).flatten()

plt.show()

m_avg = (m_landing + m_takeoff) / 2


