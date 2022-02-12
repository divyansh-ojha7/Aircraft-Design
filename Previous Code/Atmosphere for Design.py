import numpy as np
from ADRpy import unitconversions as co
from ADRpy import atmospheres as at
import matplotlib.pyplot as plt
from ADRpy import mtools4acdc as actools

"""Temperature profile"""

def isatemp_k(altitude_m=0, offset_deg=0):

    # Level altitudes in m
    level1 = 11000; level2 = 20000; level3 = 32000; level4 = 47000

    # Base temperatures (in K) and lapse rates (degrees per meter)
    # for each level
    a1 = 288.15; b1 = -6.5e-3
    a2 = 216.65; b2 = 0
    a3 = 196.65; b3 = 1e-3
    a4 = 139.05; b4 = 2.8e-3
    a5 = 270.65; b5 = 0

    alt_it = np.nditer([altitude_m, None])

    for alt, t_k in alt_it:
        if alt < level1: # Troposphere, linear lapse
            t_k[...] = a1 + b1 * alt
        elif alt < level2: # Lower stratopshere, constant
            t_k[...] = a2 + b2 * alt
        elif alt < level3: # Upper stratopshere, linear rise
            t_k[...] = a3 + b3 * alt
        elif alt < level4: # Linear rise
            t_k[...] = a4 + b4 * alt
        else: # Linear rise
            t_k[...] = a5 + b5 * alt
        t_k[...] = t_k[...] + offset_deg
    return alt_it.operands[1]



altitude_ft = 41000
offset_deg = 9.4

altitude_m = co.feet2m(altitude_ft)

temp_k = isatemp_k(altitude_m, offset_deg)
temp_c = co.k2c(temp_k)

print(temp_c, "C")



"""A more generic implementation: the Atmosphere class"""


isa = at.Atmosphere()

altitude_m = 1000

press_pa = isa.airpress_pa(altitude_m)
press_mbar = co.pa2mbar(press_pa)

print(press_mbar)


altaxis_m  = np.arange(0, 50000, 500)
altaxis_ft = co.m2feet(altaxis_m)

t_isa_c = isa.airtemp_c(altaxis_m)
vs_isa_mps = isa.vsound_mps(altaxis_m)
p_isa_mbar = isa.airpress_mbar(altaxis_m)
rho_isa_kgpm3 = isa.airdens_kgpm3(altaxis_m)

use_tex = False

f, axes = actools.panelplot_with_shared_y(
    altaxis_ft, [t_isa_c, vs_isa_mps, p_isa_mbar, rho_isa_kgpm3],
    [[-80,16], [275, 345], [-50,1050], [-0.05,1.75]],
    vlabel = 'Altitude (feet)',
    hlabels = ['Temperature ($^\circ$C)',
               'Speed of sound (m/s)',
               'Pressure (mbar)', 'Density (kgm$^{-3}$)'],
    hlines=[36089, 164042], hlinecols=['red', 'red'],
    figpar=[10, 6, 300], tex=use_tex, fam='sans-serif')

plt.show()


"""Airspeeds"""

isa = at.Atmosphere()
altitude_m = co.feet2m(25000)

KEAS = 292

KTAS = isa.eas2tas(KEAS, altitude_m)

print(KTAS)

M = isa.mach(co.kts2mps(KTAS),altitude_m)
print(M)

KEASvec = np.arange(0, 800, 1)

ISA = at.Atmosphere()

altrange_m = co.feet2m(np.arange(0, 60000, 5000))

M1KCAS = []
M1DVc  = []

for alt_m in altrange_m:
    KCASvec, machvec = ISA.keas2kcas(KEASvec, alt_m)
    Delta_Vc = KCASvec - KEASvec
    machvec_truncated = [x for x in machvec if x <= 1.0] # Trim each curve at Mach 1.0
    M1length = len(machvec_truncated)
    plt.plot(KCASvec[0:M1length], Delta_Vc[0:M1length], label = str(int(co.m2feet(alt_m))) + 'ft')
    M1KCAS.append(KCASvec[M1length])
    M1DVc.append(Delta_Vc[M1length])

plt.plot(M1KCAS, M1DVc, linestyle = 'dotted', label = 'Mach 1.0')

# Decorating the plot
plt.xlabel('KCAS')
plt.ylabel('$\Delta V_C$')
plt.title('$\Delta V_C = $' + 'KCAS - KEAS, standard day')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid()
plt.show()



isa = at.Atmosphere()

keas = np.array([100, 200, 300])
altitude_m = co.feet2m(40000)

kcas, mach = isa.keas2kcas(keas, altitude_m)

print(kcas)


"""Non-ISA atmospheres"""

resolution_m = 100

isa = at.Atmosphere()

altaxis_m  = np.arange(0, 50000, resolution_m)
altaxis_ft = co.m2feet(altaxis_m)

t_isa_c = isa.airtemp_c(altaxis_m)
vs_isa_mps = isa.vsound_mps(altaxis_m)
p_isa_mbar = isa.airpress_mbar(altaxis_m)
rho_isa_kgpm3 = isa.airdens_kgpm3(altaxis_m)

low5profile1pct, low5profile10pct = at.mil_hdbk_310('low', 'temp', 5)

atm5kcold1pct = at.Atmosphere(profile=low5profile1pct)

atm5kcold10pct = at.Atmosphere(profile=low5profile10pct)

high5profile1pct, high5profile10pct = at.mil_hdbk_310('high', 'temp', 5)

atm5kwarm1pct = at.Atmosphere(profile=high5profile1pct)

atm5kwarm10pct = at.Atmosphere(profile=high5profile10pct)


t5kcold1pct_c = atm5kcold1pct.airtemp_c(altaxis_m)
vs5kcold1pct_mps = atm5kcold1pct.vsound_mps(altaxis_m)
p5kcold1pct_mbar = atm5kcold1pct.airpress_mbar(altaxis_m)
rho5kcold1pct_kgpm3 = atm5kcold1pct.airdens_kgpm3(altaxis_m)

t5kwarm1pct_c = atm5kwarm1pct.airtemp_c(altaxis_m)
vs5kwarm1pct_mps = atm5kwarm1pct.vsound_mps(altaxis_m)
p5kwarm1pct_mbar = atm5kwarm1pct.airpress_mbar(altaxis_m)
rho5kwarm1pct_kgpm3 = atm5kwarm1pct.airdens_kgpm3(altaxis_m)

t5kcold10pct_c = atm5kcold10pct.airtemp_c(altaxis_m)
vs5kcold10pct_mps = atm5kcold10pct.vsound_mps(altaxis_m)
p5kcold10pct_mbar = atm5kcold10pct.airpress_mbar(altaxis_m)
rho5kcold10pct_kgpm3 = atm5kcold10pct.airdens_kgpm3(altaxis_m)

t5kwarm10pct_c = atm5kwarm10pct.airtemp_c(altaxis_m)
vs5kwarm10pct_mps = atm5kwarm10pct.vsound_mps(altaxis_m)
p5kwarm10pct_mbar = atm5kwarm10pct.airpress_mbar(altaxis_m)
rho5kwarm10pct_kgpm3 = atm5kwarm10pct.airdens_kgpm3(altaxis_m)

f, axes = actools.panelplot_with_shared_y(
    altaxis_ft, [t_isa_c, vs_isa_mps, p_isa_mbar, rho_isa_kgpm3],
    [[-85,25], [275, 345], [-50,1050], [-0.05,1.75]],
    vlabel = 'Altitude (feet)',
    hlabels = ['Temperature ($^\circ$C)',
               'Speed of sound (m/s)',
               'Pressure (mbar)', 'Density (kg/m^3)'],
    hlines=[36089, 164042], hlinecols=['red', 'red'], figpar=[10, 6, 400],
    tex=use_tex, fam='sans-serif')


# 1 percentile cold at 5km
axes[0].plot(t5kcold1pct_c,altaxis_ft,'green')
axes[1].plot(vs5kcold1pct_mps,altaxis_ft,'green')
axes[2].plot(p5kcold1pct_mbar,altaxis_ft,'green')
axes[3].plot(rho5kcold1pct_kgpm3,altaxis_ft,'green', label = '1\% cold at 5km')

# 10 percentile cold at 5km
axes[0].plot(t5kcold10pct_c,altaxis_ft,'yellow')
axes[1].plot(vs5kcold10pct_mps,altaxis_ft,'yellow')
axes[2].plot(p5kcold10pct_mbar,altaxis_ft,'yellow')
axes[3].plot(rho5kcold10pct_kgpm3,altaxis_ft,'yellow', label = '10\% cold at 5km')

# 1 percentile warm at 5km
axes[0].plot(t5kwarm1pct_c,altaxis_ft,'purple')
axes[1].plot(vs5kwarm1pct_mps,altaxis_ft,'purple')
axes[2].plot(p5kwarm1pct_mbar,altaxis_ft,'purple')
axes[3].plot(rho5kwarm1pct_kgpm3,altaxis_ft,'purple', label = '1\% warm at 5km')

# 10 percentile warm at 5km
axes[0].plot(t5kwarm10pct_c,altaxis_ft,'brown')
axes[1].plot(vs5kwarm10pct_mps,altaxis_ft,'brown')
axes[2].plot(p5kwarm10pct_mbar,altaxis_ft,'brown')
axes[3].plot(rho5kwarm10pct_kgpm3,altaxis_ft,'brown', label = '10\% warm at 5km')

legend = axes[3].legend(loc='best')

plt.show()


"""The variation of propulsion performance with altitude and Mach number"""

"""Turbojet"""

isa = at.Atmosphere()

altrange_m = np.arange(0, 16000, 2000)
machrange = np.arange(0, 1, 0.01)
throttleratio = 1.072

for alt_m in altrange_m:
    temp_c = isa.airtemp_c(alt_m)
    pressure_pa = isa.airpress_pa(alt_m)
    tflist = []
    for mach in np.arange(0, 1, 0.01):
        tf = at.turbojetthrustfactor(temp_c, pressure_pa, mach, throttleratio, True)
        tflist.append(tf)
    plt.plot(machrange, tflist, label = str(alt_m)+'m')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
if use_tex:
    plt.ylabel("$T/T_\mathrm{SL}$")
else:
    plt.ylabel("$T/T_{SL}$")
plt.xlabel("M")
plt.grid(True)
plt.show()

"""Turbofan"""

altrange_m = np.arange(0, 16000, 2000)
machrange = np.arange(0, 1, 0.01)
throttleratio = 1.072

for alt_m in altrange_m:
    temp_c = isa.airtemp_c(alt_m)
    pressure_pa = isa.airpress_pa(alt_m)
    tflist = []
    for mach in np.arange(0, 1, 0.01):
        tf = at.turbofanthrustfactor(temp_c, pressure_pa, mach, throttleratio, "highbpr")
        tflist.append(tf)
    plt.plot(machrange, tflist, label = str(alt_m)+'m')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
if use_tex:
    plt.ylabel("$T/T_\mathrm{SL}$")
else:
    plt.ylabel("$T/T_{SL}$")
plt.xlabel("M")
plt.grid(True)
plt.show()


"""Turboprop"""

altrange_ft = np.arange(0, 40000, 5000)
machrange = np.arange(0, 0.51, 0.01)

dens_SL_kpm3 = isa.airdens_kgpm3(0)

for alt_ft in altrange_ft:
    densratio = isa.airdens_kgpm3(co.feet2m(alt_ft)) / dens_SL_kpm3
    trlist = []
    for mach in machrange:
        tr = at.turbopropthrustfactor(densratio, mach)
        trlist.append(tr)
    plt.plot(machrange, trlist, label=str(alt_ft) + 'ft')

plt.legend()

if use_tex:
    plt.ylabel("$T/T_\mathrm{SL}$")
else:
    plt.ylabel("$T/T_{SL}$")

plt.xlabel("M")
plt.grid(True)
plt.show()

altrange_m = np.arange(0, 6000, 1500)
machrange = np.arange(0, 1, 0.01)
throttleratio = 1.072

for alt_m in altrange_m:
    temp_c = isa.airtemp_c(alt_m)
    pressure_pa = isa.airpress_pa(alt_m)
    tflist = []
    for mach in machrange:
        tf = at.turbopropthrustfactor_matt(temp_c, pressure_pa, mach, throttleratio)
        tflist.append(tf)
    plt.plot(machrange, tflist, label=str(alt_m) + 'm')

plt.legend()
if use_tex:
    plt.ylabel("$T/T_\mathrm{SL}$")
else:
    plt.ylabel("$T/T_{SL}$")
plt.xlabel("M")
plt.grid(True)
plt.show()

"""Normally aspirated piston engines"""

altrange_m = np.arange(0, 9000, 10)
densrange_kgpm3 = isa.airdens_kgpm3(altrange_m)
powerfactor = at.pistonpowerfactor(densrange_kgpm3)

plt.plot(altrange_m, powerfactor)
plt.ylabel("Power fraction available")
plt.xlabel("Altitude (m)")
plt.grid(True)
plt.show()
