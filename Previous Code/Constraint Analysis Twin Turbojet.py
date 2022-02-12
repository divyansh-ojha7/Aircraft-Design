import numpy as np
import matplotlib.pyplot as plt
from ADRpy import unitconversions as co
from ADRpy import constraintanalysis as ca
from ADRpy import atmospheres as at

"""Constraint Analysis -- a Single Engine Piston Prop"""


designbrief = {'rwyelevation_m':0, 'groundrun_m':313,                                   # <- Take-off requirements
               'stloadfactor': 1.5, 'turnalt_m': 1000, 'turnspeed_ktas': 100,           # <- Turn requirements
               'climbalt_m': 0, 'climbspeed_kias': 101, 'climbrate_fpm': 1398,          # <- Climb requirements
               'cruisealt_m': 3048, 'cruisespeed_ktas': 182, 'cruisethrustfact': 1.0,   # <- Cruise requirements
               'servceil_m': 6580, 'secclimbspd_kias': 92,                              # <- Service ceiling requirements
               'vstallclean_kcas': 69}                                                  # <- Required clean stall speed

designatm = at.Atmosphere()

# current take-off weight estimate
TOW_kg = 1542.0

# Basic design parameters
designdefinition = {'aspectratio':10.12, 'sweep_le_deg':2, 'sweep_mt_deg':0,
                    'weightfractions': {'turn': 1.0, 'climb': 1.0, 'cruise': 0.853, 'servceil': 1.0},
                    'weight_n': co.kg2n(TOW_kg)}

designpropulsion = "piston"

# design performance estimates
designperformance = {'CDTO': 0.0414, 'CLTO': 0.59, 'CLmaxTO': 1.69, 'CLmaxclean': 1.45, 'mu_R': 0.02,
                    'CDminclean': 0.0254,
                    'etaprop': {'take-off': 0.65, 'climb': 0.8, 'cruise': 0.85, 'turn': 0.85, 'servceil': 0.8}}

concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm, designpropulsion)


# Plotting the constraint diagram - quickest way
wslist_pa = np.arange(700, 1600, 2.5)

# graph in terms of power required and wing area
a = concept.propulsionsensitivity_monothetic(wingloading_pa=wslist_pa, show='combined', y_var='p_hp', x_var='s_m2', y_lim=600)

# graph in terms of thrust to weight ratio and wing loading
a = concept.propulsionsensitivity_monothetic(wingloading_pa=wslist_pa, show='combined', y_var='tw', x_var='ws_pa', y_lim=0.4)


# Plotting the constraint diagram - flexible way
preq = concept.powerrequired(wslist_pa, TOW_kg)

Smin_m2 = concept.smincleanstall_m2(TOW_kg)


wingarea_m2 = co.kg2n(TOW_kg) / wslist_pa # x axis

plt.rcParams["figure.figsize"] = [8,6]
plt.rcParams['figure.dpi'] = 160

plt.plot(wingarea_m2, preq['take-off'],  label = 'Take-off')
plt.plot(wingarea_m2, preq['turn'], label = 'Turn')
plt.plot(wingarea_m2, preq['climb'], label = 'Climb')
plt.plot(wingarea_m2, preq['cruise'], label = 'Cruise')
plt.plot(wingarea_m2, preq['servceil'], label = 'Service ceiling')

combplot = plt.plot(wingarea_m2, preq['combined'], label = 'Combined')

plt.setp(combplot, linewidth=4)

stall_label = 'Clean stall at ' + str(designbrief['vstallclean_kcas']) + 'KCAS'

plt.plot([Smin_m2, Smin_m2], [0, 1500], label = stall_label)

legend = plt.legend(loc='upper left')

plt.ylabel("Power required (HP)")
plt.xlabel("S (m$^2$)")
plt.title("Minimum SL power required (MTOW = " + str(round(TOW_kg)) + "kg)")
plt.xlim(min(wingarea_m2), max(wingarea_m2))
plt.ylim(0, max(preq['combined']) * 1.1)
plt.grid(True)
plt.show()


# Constraint sensitivity analysis
designbrief = {'rwyelevation_m': 0, 'groundrun_m': 313,
                'stloadfactor': [1.5, 1.65], 'turnalt_m': [1000, 1075], 'turnspeed_ktas': [100, 110],
                'climbalt_m': 0, 'climbspeed_kias': 101, 'climbrate_fpm': 1398,
                'cruisealt_m': [2600, 3200], 'cruisespeed_ktas': [170, 175], 'cruisethrustfact': 1.0,
                'servceil_m': [6500, 6650], 'secclimbspd_kias': 92,
                'vstallclean_kcas': 69}

designdefinition = {'aspectratio': [10, 11], 'sweep_le_deg': 2, 'sweep_25_deg': 0, 'bpr': -1,
                    'weight_n': 15000,
                    'weightfractions': {'turn': 1.0, 'climb': 1.0, 'cruise': 0.853, 'servceil': 1.0}}

designperformance = {'CDTO': 0.0414, 'CLTO': 0.59, 'CLmaxTO': 1.69, 'CLmaxclean': 1.45, 'mu_R': 0.02,
                    'CDminclean': [0.0254, 0.026],
                    'etaprop': {'take-off': 0.65, 'climb': 0.8, 'cruise': 0.85, 'turn': 0.85, 'servceil': 0.8}}

designatm = at.Atmosphere()

designpropulsion = "piston"


concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, designatm, designpropulsion)
wslist_pa = np.arange(700, 2500, 2.5)

concept.propulsionsensitivity_monothetic(wingloading_pa=wslist_pa, show=True, y_var='p_hp', x_var='s_m2', y_lim=700)


concept.propulsionsensitivity_monothetic(wingloading_pa=wslist_pa, show='cruise', y_var='p_hp', x_var='s_m2', maskbool=False)
