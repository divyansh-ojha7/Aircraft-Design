import matplotlib.pyplot as plt
from math import exp
import numpy as np
# values from book
g = 32.2
mu = .04
MTOW = 11905 #lb
v_max = 200  # KTAS
L_D = 10
v_stall = 60  # KEAS
v_to = 1.1 * v_stall
ROC = 3230/60  # fps
ROC_c = 100/60  # fps
S_to = 1200  # ft takeoff distance
S_ceiling = 35000  # ft
CL_max = 2.7
n_p = .6  # prop efficiency
n_p2 = .7
h = 550  # conversion factor to convert lb/(lb ft/sec) to lb/hp
h2 = 1.68781  # conversion factor knots to ft/sec
e = .85
AR = 8
K = 1/(np.pi*e*AR)
air_density_3000 = .002175  # slug/ft^3
air_density_30000 = .001066  # slug/ft^3 # 25, 000 ft
air_density_35000 = .000891 # slug/ft^3 # 30, 000 ft
air_density_0 = .002378   # slug/ft^3
sigma = air_density_30000/air_density_0
sigma_c = air_density_35000/air_density_0
CD_0 = .025
CL_c = .3
del_CL = .6
CL_TO = CL_c + del_CL
CD_0_LG = .009
CD_0_HLD_T0 = .005
CD_0_TO = CD_0 + CD_0_LG + CD_0_HLD_T0
CD_T0 = CD_0_TO + K*CL_TO**2
CL_R = CL_max/(1.1**2)
CD_g = (CD_0_TO - mu*CL_TO)

# Wing loading for stall speed is vertical line
w_s_stall = .5*air_density_0*(v_stall*h2)**2*CL_max
print(w_s_stall)

w_s = np.linspace(1, 100, 100)  # wing loading vector
# weight over power for max velocity
w_p_vmax = (n_p/((.5*air_density_0*(v_max*h2)**3*CD_0*(1/w_s)) + ((2*K/(air_density_30000*sigma*(v_max*h2)))*w_s))) * h
W_P_vmax = 385/(6129.7*(1/w_s) + .317*w_s)  # lb/hp

# weight over power for takeoff
w_p_sTO = []
W_P_sTO = []
for i in w_s:

    w_p_sTO.append((((1 - exp(.6*g*air_density_3000*CD_g*S_to*(1/i))) /
                     (mu-(mu + CD_g/CL_R)*(exp(.6*g*air_density_3000*CD_g*S_to * (1/i))))) * (n_p/(v_to*h2))) * h)
#W_P_sTO.append(((1-exp(1.426/i))/(.04-(.053*exp(1.426/i))))*(.0046*550))  # used to evaluate equation

# Weight over power for rate of climb
w_p_ROC = (1/((ROC/n_p2) + (((2/(air_density_0*((3*CD_0)/K)**.5))*w_s)**.5)*(1.155/(L_D*n_p))))*h
# W_P_ROC = (1*550)/(64.3 + ((540.7*w_s)**.5*.092))  # used to evaluate equation

# Weight over power for cruise
w_p_cruise = (sigma_c/(((ROC_c/n_p2) + (((2/(air_density_35000*((3*CD_0)/K)**.5))*w_s)**.5))*(1.155/(L_D*n_p2))))*h
# W_P_cruise = (170.5/(2.38 + ((1742.3 * w_s)**.5)*.092))  # used to evaluate equation

area = 4000/w_s_stall
for x in range(1, 11, 1):
    span1 = (x*area)**.5
    print(x)
    print(span1)
    chord = area / span1
    print(chord)

plt.xlim(0, 70)
plt.ylim(0,10)

plt.vlines(w_s_stall, 0, 40, 'b')
plt.plot(w_s, w_p_ROC, 'r')
plt.plot(w_s, w_p_sTO, 'y')
plt.plot(w_s, w_p_cruise, 'g')
plt.plot(w_s, w_p_vmax, 'k')
plt.show()