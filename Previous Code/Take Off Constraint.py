from ADRpy import atmospheres as at
from ADRpy import constraintanalysis as ca
import numpy as np
import matplotlib.pyplot as plt
from ADRpy import unitconversions as co
import pickle
import random
import os
import ADRpy

designatm = at.Atmosphere()

designbrief = {'groundrun_m':60}
designdefinition = {'aspectratio':9, 'bpr':-1}
designperformance = {'CDTO':0.0898, 'CLTO':0.97, 'CLmaxTO':1.7, 'mu_R':0.08}

concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm)

wingloadinglist_pa = np.arange(80, 250, 1)

twratio, liftoffspeed_mps = concept.thrusttoweight_takeoff(wingloadinglist_pa)

plt.plot(wingloadinglist_pa, twratio)
plt.ylabel("T/W ( )")
plt.xlabel("W/S (N/m$^2$)")
plt.title("Minimum thrust to weight ratio required")
plt.grid(True)
plt.show()


plt.plot(wingloadinglist_pa, liftoffspeed_mps)
plt.ylabel("$V_\mathrm{L}$ (m/s)")
plt.xlabel("W/S (N/m$^2$)")
plt.title("Lift-off speed as a function of wing loading")
plt.grid(True)
plt.show()


"""Sensitivity analysis"""

for groundrun_m in [20, 30, 40, 50, 60, 70, 80, 90]:
    designbrief = {'groundrun_m':groundrun_m}
    concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm)
    twratio, liftoffspeed_mps = concept.thrusttoweight_takeoff(wingloadinglist_pa)
    plt.plot(wingloadinglist_pa, twratio, label = str(groundrun_m)+'m')

legend = plt.legend(loc='upper right', fontsize='medium')
plt.ylabel("T/W (  )")
plt.xlabel("W/S (N/m$^2$)")
plt.grid(True)
plt.title("Sensitivity of minimum T/W to required take-off roll")
plt.show()



designbrief = {'groundrun_m': 30}

for elevation_ft in [0, 1000, 2000, 3000, 4000, 5000]:
    designbrief = {'groundrun_m': 30, 'rwyelevation_m': co.feet2m(elevation_ft)}
    concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm)
    twratio, liftoffspeed_mps = concept.thrusttoweight_takeoff(wingloadinglist_pa)
    plt.plot(wingloadinglist_pa, twratio, label=str(elevation_ft) + 'ft')

legend = plt.legend(loc='lower right', fontsize='medium')
plt.ylabel("T/W (  )")
plt.xlabel("W/S (N/m$^2$)")
plt.grid(True)
plt.title("Sensitivity of minimum T/W to runway elevation")
plt.show()

designbrief = {'groundrun_m': 30, 'rwyelevation_m': 0}

for temp_offset_deg in [-20, -10, 0, 10, 20, 30, 40]:

    designatm = at.Atmosphere(offset_deg=temp_offset_deg)
    concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm)
    twratio, liftoffspeed_mps = concept.thrusttoweight_takeoff(wingloadinglist_pa)

    if temp_offset_deg < 0:  # Generating the labels needs a bit of care here
        plt.plot(wingloadinglist_pa, twratio, label='ISA ' + str(temp_offset_deg) + '$^o$C')
    else:
        plt.plot(wingloadinglist_pa, twratio, label='ISA +' + str(temp_offset_deg) + '$^o$C')

legend = plt.legend(loc='lower right', fontsize='medium')
plt.ylabel("T/W (  )")
plt.xlabel("W/S (N/m$^2$)")
plt.grid(True)
plt.title("Sensitivity of minimum T/W to ambient temperature")
plt.show()


"""Thrust mapping"""

designdefinition = {'aspectratio': 9, 'bpr': -1}

etap = {'take-off': 0.6, 'climb': 0.75, 'cruise': 0.85, 'turn': 0.85, 'servceil': 0.6}

designperformance = {'CDTO': 0.0898, 'CLTO': 0.97, 'CLmaxTO': 1.7, 'mu_R': 0.08, 'etaprop': etap}

designatm = at.Atmosphere()

for elevation_ft in [0, 1000, 2000, 3000, 4000, 5000]:
    designbrief = {'groundrun_m': 30, 'rwyelevation_m': co.feet2m(elevation_ft)}

    concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm)

    gffactor = at.pistonpowerfactor(designatm.airdens_kgpm3(co.feet2m(elevation_ft)))

    twratio, liftoffspeed_mps = concept.thrusttoweight_takeoff(wingloadinglist_pa)

    pwratio = (1 / gffactor) * ca.tw2pw(twratio, liftoffspeed_mps, etap['take-off'])

    plt.plot(wingloadinglist_pa, pwratio, label=str(elevation_ft) + 'ft')

legend = plt.legend(loc='lower right')
plt.ylabel("P/W (W/N)")
plt.xlabel("W/S (N/m$^2$)")
plt.grid(True)
plt.show()


"""A second example: take-off performance of a business jet"""

designbrief = {'rwyelevation_m':1000, 'groundrun_m':1200}
designdefinition = {'aspectratio':7.3, 'bpr':3.9, 'tr':1.05}
designperformance = {'CDTO':0.04, 'CLTO':0.9, 'CLmaxTO':1.6, 'mu_R':0.02}

wingloadinglist_pa = np.arange(2000, 5000, 10)

designatm = at.Atmosphere()
concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm)

twratio, liftoffspeed_mps = concept.thrusttoweight_takeoff(wingloadinglist_pa)

twratio1 = concept.map2static() * twratio

temp_c = designatm.airtemp_c(designbrief['rwyelevation_m'])
pressure_pa = designatm.airpress_pa(designbrief['rwyelevation_m'])
mach = designatm.mach(liftoffspeed_mps, designbrief['rwyelevation_m'])

throttleratio = designdefinition['tr']

correctionvec = []
for i, tw in enumerate(twratio):
    twratio_altcorr = at.turbofanthrustfactor(temp_c, pressure_pa, mach[i], throttleratio, "lowbpr")
    correctionvec.append(twratio_altcorr)

twratio2 = twratio1 / twratio_altcorr

plt.plot(wingloadinglist_pa, twratio, label = '$\overline{T}/W$')
plt.plot(wingloadinglist_pa, twratio1, label = '$T_\mathrm{S}/W$')
plt.plot(wingloadinglist_pa, twratio2, label = '$T_\mathrm{S}/W$ (alt and Mach corrected)')

legend = plt.legend(loc='upper left')
plt.ylabel("T/W ( )")
plt.xlabel("W/S (N/m$^2$)")
plt.title("Minimum thrust to weight ratio required")
plt.grid(True)
plt.show()

"""Uncertainty quantification"""

_fstr = os.path.join(ADRpy.__path__[0], "data", "elev1200m.dat")

with open(_fstr, 'rb') as fp:
    rwy_elevation_lst_ft = pickle.load(fp)

rwy_elevation_lst_m = [co.feet2m(el) for el in rwy_elevation_lst_ft]

twmatrix = []
wingloadinglist_pa = np.arange(2000, 5000, 10)
mc_samplesize = 1000

for i in range(1, mc_samplesize):
    r_elev_m = max(0, random.choice(rwy_elevation_lst_m))
    gr_m = np.random.normal(1200, 100)
    ar = np.random.uniform(6.5, 9)
    bpr = np.random.normal(4, 1)
    tr = np.random.uniform(1.04, 1.08)
    CDTO = np.random.normal(0.04, 0.005)
    CLTO = np.random.normal(0.9, 0.1)
    CLmaxTO = np.random.normal(1.6, 0.2)
    mu_R = np.random.uniform(0.015, 0.025)
    offs_deg = np.random.normal(15, 15)

    designbrief = {'rwyelevation_m': r_elev_m, 'groundrun_m': gr_m}
    designdefinition = {'aspectratio': ar, 'bpr': bpr, 'tr': tr}
    designperformance = {'CDTO': CDTO, 'CLTO': CLTO, 'CLmaxTO': CLmaxTO, 'mu_R': mu_R}
    designatm = at.Atmosphere(offset_deg=offs_deg, profile=None)

    concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm, "jet")

    tw_sl, speed_mps, avspeed_mps = concept.twrequired_to(wingloadinglist_pa)

    if np.size(twmatrix) > 0:
        twmatrix = np.vstack((twmatrix, tw_sl))
    else:
        twmatrix = tw_sl

    # You can comment this plot out for large samples - it is included here just as a sanity check
    mcplot = plt.plot(wingloadinglist_pa, tw_sl, linewidth=0.1)

# A crude visualisation of the results - all of the constraint lines:
plt.ylabel("T/W ( )")
plt.xlabel("W/S (N/m$^2$)")
plt.title("Minimum thrust to weight ratio required")
plt.grid(True)
plt.show()

meantw = twmatrix.mean(axis=0)
stdtw = twmatrix.std(axis=0)


plt.plot(wingloadinglist_pa, meantw, label = '$\mu$')
plt.plot(wingloadinglist_pa, meantw+stdtw, label = '$\mu+\sigma$')
plt.plot(wingloadinglist_pa, meantw-stdtw, label = '$\mu-\sigma$')
legend = plt.legend(loc='upper left')
plt.ylabel("T/W ( )")
plt.xlabel("W/S (N/m$^2$)")
plt.title("Minimum thrust to weight ratio required, one std either side of mean")
plt.grid(True)
plt.show()



wheretoslice = 130
lear45tw = 0.325

plt.hist(twmatrix[:,wheretoslice], bins=np.arange(0,0.55,0.01))

# Vertical line representing the Learjet 45
plt.plot(lear45tw, 0, '|', markersize=50, color='red')

plt.title("Slice at $W/S = $ "+ str(wingloadinglist_pa[wheretoslice]) + " N/m$^2$")
plt.show()

np.percentile(twmatrix[:,150],50)

feasible_percentile = 70

np.percentile(twmatrix[:,150],feasible_percentile)


feasible_percentile = 70
percentile_tw = np.percentile(twmatrix, feasible_percentile, axis=0)
median_tw = np.percentile(twmatrix, 50, axis=0)
plt.plot(wingloadinglist_pa, meantw, label = '$\mu$')
plt.plot(wingloadinglist_pa, median_tw, label = 'median')
plt.plot(wingloadinglist_pa, percentile_tw, label = str(feasible_percentile)+' percentile')
legend = plt.legend(loc='upper left')
plt.ylabel("T/W ( )")
plt.xlabel("W/S (N/m$^2$)")
plt.title("Minimum thrust to weight ratio required")
plt.grid(True)
plt.show()


for feasible_percentile in [50, 60, 70, 80, 90, 95, 99]:
    percentile_tw = np.percentile(twmatrix, feasible_percentile, axis=0)
    plt.plot(wingloadinglist_pa, percentile_tw, label = str(feasible_percentile)+' percentile')

legend = plt.legend(loc='upper left')
plt.ylabel("T/W ( )")
plt.xlabel("W/S (N/m$^2$)")
plt.title("Minimum thrust to weight ratio required")
plt.grid(True)
plt.show()