import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as patheffects
from ADRpy import unitconversions as co
from ADRpy import constraintanalysis as ca
from ADRpy import atmospheres as at

"""A Constraint Analysis Case Study: G-OUAV"""

designatm = at.Atmosphere()

designbrief = {'rwyelevation_m':co.feet2m(295), 'groundrun_m':90,                   # <- Take-off requirements
               'stloadfactor': 2.5, 'turnalt_m': 1000, 'turnspeed_ktas': 70,        # <- Turn requirements
               'climbalt_m': 1500, 'climbspeed_kias': 50, 'climbrate_fpm': 1000,    # <- Climb requirements
               'cruisealt_m': 0, 'cruisespeed_ktas': 110, 'cruisethrustfact': 1.0,  # <- Cruise requirements
               'servceil_m': 15000, 'secclimbspd_kias': 50,                         # <- Service ceiling requirements
               'vstallclean_kcas': 38}                                              # <- Required clean stall speed

TOW_kg = 450

designdefinition = {'aspectratio':7.43, 'sweep_le_deg':0, 'sweep_mt_deg':0,
                    'weightfractions': {'turn': 1.0, 'climb': 1.0, 'cruise': 1.0, 'servceil': 1.0},
                    'weight_n': co.kg2n(TOW_kg)}

designpropulsion = "piston"

designperformance = {'CDTO': 0.05, 'CLTO': 0.6, 'CLmaxTO': 1.6, 'CLmaxclean': 1.8, 'mu_R': 0.02,
                    'CDminclean': 0.04,
                    'etaprop': {'take-off': 0.6, 'climb': 0.6, 'cruise': 0.75, 'turn': 0.75, 'servceil': 0.75}}

concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm, designpropulsion)

wslist_pa = np.arange(300, 800, 2.5)

a = concept.propulsionsensitivity_monothetic(wingloading_pa=wslist_pa, show='combined', y_var='p_hp', x_var='s_m2', y_lim=150)


preq = concept.powerrequired(wslist_pa, TOW_kg)

Smin_m2 = concept.smincleanstall_m2(TOW_kg)

wingarea_m2 = co.kg2n(TOW_kg) / wslist_pa # x axis

plt.rcParams["figure.figsize"] = [8,6]
plt.rcParams['figure.dpi'] = 160

barbs = [patheffects.withTickedStroke()]

plt.plot(wingarea_m2, preq['take-off'],  label = 'Take-off', path_effects=barbs)
plt.plot(wingarea_m2, preq['turn'], label = 'Turn', path_effects=barbs)
plt.plot(wingarea_m2, preq['climb'], label = 'Climb', path_effects=barbs)
plt.plot(wingarea_m2, preq['cruise'], label = 'Cruise', path_effects=barbs)

combplot = plt.plot(wingarea_m2, preq['combined'], label = 'Combined front up to turn stall')

plt.setp(combplot, linewidth=4)

stall_label = 'Clean stall at ' + str(designbrief['vstallclean_kcas']) + 'KCAS'

plt.plot([Smin_m2, Smin_m2], [0, 1500], label = stall_label, path_effects=barbs)

legend = plt.legend(loc='lower right')

plt.ylabel("Power required (HP)")
plt.xlabel("Wing area (m$^2$)")

plt.title("Minimum SL power required (MTOW = " + str(round(TOW_kg)) + "kg)")

plt.xlim(min(wingarea_m2), max(wingarea_m2))
plt.ylim(0, max(preq['combined']) * 1.1)

plt.grid(True)
plt.show()

