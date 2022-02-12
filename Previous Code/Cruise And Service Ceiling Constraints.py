import numpy as np
import matplotlib.pyplot as plt
from ADRpy import unitconversions as co
from ADRpy import constraintanalysis as ca
from ADRpy import atmospheres as at

"""THE CRUISE SPEED CONSTRAINT"""


designbrief = {'rwyelevation_m':1000, 'groundrun_m':1200, \
               'stloadfactor': 2, 'turnalt_m': 5000, 'turnspeed_ktas': 300, \
               'climbalt_m': 1000, 'climbspeed_ktas': 250, 'climbrate_fpm': 1000, \
               'cruisealt_m': 15000, 'cruisespeed_ktas': 445}

wfract = {'turn': 1.0, 'climb': 1.0, 'cruise': 0.85, 'servceil': 0.85}

designdefinition = {'aspectratio':7.3, 'sweep_le_deg':10, 'sweep_mt_deg':8, 'bpr':3.9, 'tr':1.05, 'weightfractions':wfract}

designperformance = {'CDTO':0.04, 'CLTO':0.9, 'CLmaxTO':1.6, 'mu_R':0.02, 'CDminclean':0.02}
designatm = at.Atmosphere()

concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm, "piston")

cruisemach = designatm.mach(co.kts2mps(designbrief['cruisespeed_ktas']), designbrief['cruisealt_m'])
print(cruisemach)

wingloadinglist_pa = np.arange(2000, 5000, 10)
twratio = concept.twrequired_crs(wingloadinglist_pa)

plt.plot(wingloadinglist_pa, twratio)
plt.ylabel("T/W ( )")
plt.xlabel("W/S (N/m$^2$)")
plt.title("Minimum thrust to weight ratio required")
plt.grid(True)
plt.show()


"""THE SERVICE CEILING CONSTRAINT"""

designbrief = {}
designdefinition = {'aspectratio':10, 'sweep_le_deg':0, 'sweep_mt_deg':0}
designperformance = {'CDminclean':0.02541}

weight_N = co.lbf2n(3400)
wingarea_m2 = co.feet22m2(144.9)
wingloading_pa = weight_N / wingarea_m2

altitude0_m = 0
altitude10k_m = co.feet2m(10000)

designatm = at.Atmosphere()
concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm, "piston")

bestclspeedSL_mps = concept.bestclimbspeedprop(wingloading_pa, altitude0_m)
bestclspeed10k_mps = concept.bestclimbspeedprop(wingloading_pa, altitude10k_m)

bestclspeedSL_KTAS = co.mps2kts(bestclspeedSL_mps)
bestclspeed10k_KTAS = co.mps2kts(bestclspeed10k_mps)

print("SL: " + str(bestclspeedSL_KTAS) + " KTAS")
print("10,000 feet: " + str(bestclspeed10k_KTAS) + " KTAS")


bestclspeed10k_KIAS = designatm.tas2eas(co.mps2kts(bestclspeed10k_mps), altitude10k_m)
print("10,000 feet: " + str(bestclspeed10k_KIAS) + " KIAS")


"""Adapting the rate of climb constraint"""

designbrief = {'rwyelevation_m':1000, 'groundrun_m':1200, \
               'stloadfactor': 2, 'turnalt_m': 5000, 'turnspeed_ktas': 300, \
               'climbalt_m': 1000, 'climbspeed_ktas': 250, 'climbrate_fpm': 1000, \
               'cruisealt_m': 15000, 'cruisespeed_ktas': 445,
               'servceil_m': 16000, 'secclimbspd_kias': 250}
designdefinition = {'aspectratio':7.3, 'sweep_le_deg':10, 'sweep_mt_deg':8, 'bpr':3.9, 'tr':1.05}
designperformance = {'CDTO':0.04, 'CLTO':0.9, 'CLmaxTO':1.6, 'mu_R':0.02, 'CDminclean':0.02}
designatm = at.Atmosphere()

concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm, "piston")

wingloadinglist_pa = np.arange(2000, 5000, 10)
twratio = concept.twrequired_sec(wingloadinglist_pa)

plt.plot(wingloadinglist_pa, twratio)
plt.ylabel("T/W ( )")
plt.xlabel("W/S (N/m$^2$)")
plt.title("Minimum thrust to weight ratio required")
plt.grid(True)
plt.show()


