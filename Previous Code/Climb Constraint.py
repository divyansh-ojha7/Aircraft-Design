import numpy as np
import matplotlib.pyplot as plt
from ADRpy import unitconversions as co
from ADRpy import constraintanalysis as ca
from ADRpy import atmospheres as at


"""Scaling an aircraft concept - the climb constraint"""

# climb performance of a business jet

designbrief = {'climbalt_m': 1000, 'climbspeed_kias': 250, 'climbrate_fpm': 1000, \
               'cruisealt_m': 15000, 'cruisespeed_ktas': 445}
designdefinition = {'aspectratio':7.3, 'sweep_le_deg':10, 'sweep_mt_deg':8, 'bpr':3.9, 'tr':1.05}
designperformance = {'CDTO':0.04, 'CLTO':0.9, 'CLmaxTO':1.6, 'mu_R':0.02, 'CDminclean':0.02}

designatm = at.Atmosphere()

concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm, "jet")

wingloadinglist_pa = np.arange(2000, 5000, 10)

twratio = concept.twrequired_clm(wingloadinglist_pa)

plt.plot(wingloadinglist_pa, twratio)
plt.ylabel("T/W ( )")
plt.xlabel("W/S (N/m$^2$)")
plt.title("Minimum thrust to weight ratio required")
plt.grid(True)
plt.show()

"""Quantifying uncertainties in climb calculations"""

designbrief = {'rwyelevation_m': 1000, 'groundrun_m': 1200, \
               'stloadfactor': 2, 'turnalt_m': 5000, 'turnspeed_ktas': 300, \
               'climbalt_m': 1000, 'climbspeed_kias': 250, 'climbrate_fpm': 1000, \
               'cruisealt_m': 15000, 'cruisespeed_ktas': 445}

twmatrix = []
wingloadinglist_pa = np.arange(2000, 5000, 10)
mc_samplesize = 5000

for i in range(1, mc_samplesize):

    ar = np.random.uniform(6.5, 9)
    bpr = max(5, np.random.normal(8, 1))
    tr = np.random.uniform(1.04, 1.08)

    sle_deg = np.random.normal(17, 3)
    smt_deg = sle_deg - np.random.normal(7, 3)

    offs_deg = np.random.normal(15, 15)

    cdmin = np.random.normal(0.02, 0.002)

    designdefinition = {'aspectratio': ar, 'sweep_le_deg': sle_deg, 'sweep_mt_deg': smt_deg, 'bpr': bpr, 'tr': tr}
    designperformance = {'CDminclean': cdmin}
    designatm = at.Atmosphere(offset_deg=offs_deg, profile=None)

    concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm, "jet")
    tw_sl = concept.twrequired_clm(wingloadinglist_pa)

    if np.size(twmatrix) > 0:
        twmatrix = np.vstack((twmatrix, tw_sl))
    else:
        twmatrix = tw_sl

for feasible_percentile in [50, 60, 70, 80, 90, 95, 99]:
    percentile_tw = np.percentile(twmatrix, feasible_percentile, axis=0)
    plt.plot(wingloadinglist_pa, percentile_tw, label = str(feasible_percentile)+' percentile')

legend = plt.legend(loc='upper left')
plt.ylabel("T/W ( )")
plt.xlabel("W/S (N/m$^2$)")
plt.title("Minimum thrust to weight ratio required")
plt.grid(True)
plt.show()

