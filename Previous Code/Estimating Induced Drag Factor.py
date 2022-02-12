import math

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from ADRpy import constraintanalysis as ca

"""Estimating the Induced Drag Factor"""

"""Leading Edge 2 Degrees"""

matplotlib.rcParams['figure.dpi'] = 160

# Aspect ratio (AR) range to be swept
ar_range = np.arange(2,35,0.1)
e1 = []; e2 = []; e4 = []; e24 = []
k1 = []; k2 = []; k4 = []; k24 = []
for ar in ar_range:
    # Gently swept wing
    exdesign = {'aspectratio':ar, 'sweep_le_deg': 2, 'sweep_mt_deg': 1}
    exconcept = ca.AircraftConcept(brief={}, design=exdesign, performance={}, designatm={})
    k1.append(exconcept.induceddragfact(1))
    k2.append(exconcept.induceddragfact(2))
    k4.append(exconcept.induceddragfact(4, mach_inf=0.3))
    k24.append(exconcept.induceddragfact(24, mach_inf=0.3))
    e1.append(exconcept.oswaldspaneff1())
    e2.append(exconcept.oswaldspaneff2())
    e4.append(exconcept.oswaldspaneff4(mach_inf=0.3))
    e24.append((e2[-1] + e4[-1]) / 2.0)

fig, axs = plt.subplots(2, 1, sharex='all', gridspec_kw={'hspace': 0.4})
fig.suptitle("Calculated $K$ from $e_0$ estimates, $\Lambda_{LE}=$"+str(exdesign['sweep_le_deg'])+"$^{\circ}$")

axs[0].plot(ar_range, e1, label='[1] Raymer straight', c='red')
axs[0].plot(ar_range, e2, label='[2] Brandt swept', c='blue')
axs[0].plot(ar_range, e4, label='[4] Nita, Scholz', c='orange')
axs[0].plot(ar_range, e24, label='[24] Average', lw=2, c='purple', ls='--')
axs[0].grid(True)
axs[0].set(xlabel='AR', ylabel='$e_0$')
axs[0].set_ylim(0, 1)
axs[0].legend(title='whichoswald', loc='center left', bbox_to_anchor=(1, 0.5))

axs[1].plot(ar_range, k1, label='[1] Raymer straight', c='red')
axs[1].plot(ar_range, k2, label='[2] Brandt swept', c='blue')
axs[1].plot(ar_range, k4, label='[4] Nita, Scholz', c='orange')
axs[1].plot(ar_range, k24, label='[24] Average', lw=2, c='purple', ls='--')
axs[1].grid(True)
axs[1].set(xlabel='AR', ylabel='$K$')
axs[1].set_ylim(0, 0.2)
axs[1].legend(title='whichoswald', loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()

fig.clear()
plt.close(fig=fig)

"""Leading Edge 60 Degrees"""

# Aspect ratio (AR) range to be swept
ar_range = np.arange(1.8,8,0.1)
e2 = []; e3 = []; e4 = []; e234 = []
k2 = []; k3 = []; k4 = []; k234 = []
for ar in ar_range:
    # Highly swept wing
    exdesign = {'aspectratio':ar, 'sweep_le_deg': 60, 'sweep_mt_deg': 36}
    exconcept = ca.AircraftConcept(brief={}, design=exdesign, performance={}, designatm={})
    k2.append(exconcept.induceddragfact(2))
    k3.append(exconcept.induceddragfact(3))
    k4.append(exconcept.induceddragfact(4, mach_inf=0.3))
    k234.append(exconcept.induceddragfact(234, mach_inf=0.3))
    e2.append(exconcept.oswaldspaneff2())
    e3.append(exconcept.oswaldspaneff3())
    e4.append(exconcept.oswaldspaneff4(mach_inf=0.3))
    e234.append((e2[-1] + e3[-1] + e4[-1]) / 3.0)

fig, axs = plt.subplots(2, 1, sharex='all', gridspec_kw={'hspace': 0.4})
fig.suptitle("Calculated $K$ from $e_0$ estimates, $\Lambda_{LE}=$"+str(exdesign['sweep_le_deg'])+"$^{\circ}$")

axs[0].plot(ar_range, e2, label='[2] Brandt swept', c='blue')
axs[0].plot(ar_range, e3, label='[3] Raymer swept', c='skyblue')
axs[0].plot(ar_range, e4, label='[4] Nita, Scholz', c='orange')
axs[0].plot(ar_range, e234, label='[234] Average', lw = 2, c='purple', ls='--')
axs[0].grid(True)
axs[0].set(xlabel='AR', ylabel='$e_0$')
axs[0].set_ylim(0, 1)
axs[0].legend(title='whichoswald', loc='center left', bbox_to_anchor=(1, 0.5))

axs[1].plot(ar_range, k2, label='[2] Brandt swept', c='blue')
axs[1].plot(ar_range, k3, label='[3] Raymer swept', c='skyblue')
axs[1].plot(ar_range, k4, label='[4] Nita, Scholz', c='orange')
axs[1].plot(ar_range, k234, label='[234] Average', lw = 2, c='purple', ls='--')
axs[1].grid(True)
axs[1].set(xlabel='AR', ylabel='$K$')
axs[1].set_ylim(0, 0.3)
axs[1].legend(title='whichoswald', loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()

fig.clear()
plt.close(fig=fig)


"""Finding K (Mach Dependent)"""

# Warning(s) are thrown on purpose, to inform the designer that it may not be possible for the aircraft concept to fly at the desired Mach.

matplotlib.rcParams['figure.dpi'] = 160

# Gently swept wing
exdesign = {'aspectratio':8, 'sweep_le_deg': 2, 'sweep_mt_deg': 1}
exconcept = ca.AircraftConcept(brief={}, design=exdesign, performance={}, designatm={})

# Mach (M) range to be swept
mach_range = np.arange(0,0.9,0.01)
e4 = []; k4 = []
for mach in mach_range:
    # Note how both oswaldspaneff4 and induceddragfact methods can take a Mach number argument
    e4.append(exconcept.oswaldspaneff4(mach_inf=mach))
    k4.append(exconcept.induceddragfact(whichoswald=4, mach_inf=mach))

fig, axs = plt.subplots(2, 1, sharex='all', gridspec_kw={'hspace': 0.4})
fig.suptitle("Calculated $K = f(Mach)$ from $e_0$ estimates, $\Lambda_{LE}=$"+str(exdesign['sweep_le_deg'])+"$^{\circ}$")

axs[0].plot(mach_range, e4, label='[4] Nita, Scholz', c='orange')
axs[0].grid(True)
axs[0].set(xlabel='Mach', ylabel='$e_0$')
axs[0].set_ylim(0, 1)
axs[0].legend(title='whichoswald', loc='center left', bbox_to_anchor=(1, 0.5))

axs[1].plot(mach_range, k4, label='[4] Nita, Scholz', c='orange')
axs[1].grid(True)
axs[1].set(xlabel='Mach', ylabel='$K$')
axs[1].set_ylim(0, 0.6)
axs[1].legend(title='whichoswald', loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()

fig.clear()
plt.close(fig=fig)


"""Estimating 'K' for Supersonic Aircraft: Leading-Edge Suction Method"""

matplotlib.rcParams['figure.dpi'] = 160

# List of actual CL demanded in flight along the x-axis
cl_achieved = np.arange(-1, 2, 0.01)

# List of original design CL
cl_cruise_array = np.array([.0, .1, .3, .4, .5, .6, .8])


# Suction model
def y_suction(cl_delta, cl_crs, a, c, r):
    k = (-0.5 * cl_crs ** 2) - (0.25 * cl_crs) -0.22
    b = 1 + r * k
    x = cl_delta
    y = a * (x - b) * np.exp(-c * (x - 0.1)) * -np.tan(0.1 * (x - k))
    return y

# Sample suction curves
y_03 = y_suction(cl_delta=cl_achieved, cl_crs=0.3, a=22.5, c=1.95, r=0)
y_08 = y_suction(cl_delta=cl_achieved, cl_crs=0.8, a=5.77, c=1, r=-1.29)

# In the ADRpy constraints module, each cl_cruise is used to find a weighted average of the sample curves:
# weight = np.interp(cl_cruise, [0.3, 0.8], [1, 0])
# y_0x = weight * y_03 + (1 - weight) * y_08

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

# Create predictions of new suction curves by weighting the sample curves
for cl_cruise in cl_cruise_array:
    weight = np.interp(cl_cruise, [0.3, 0.8], [1, 0])
    y_0x = weight * y_03 + (1 - weight) * y_08
    ax.plot((cl_achieved+cl_cruise), y_0x, label = str(cl_cruise))

handles, labels = ax.get_legend_handles_labels()
ax.legend(reversed(handles), reversed(labels), title='$C_{L, cruise}$', loc='center left', bbox_to_anchor=(1, 0.5))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title('ADRpy Suction Model for Supersonic Aircraft')
ax.set(xlabel='$C_L$ achieved', ylabel='Suction Factor $S$')
ax.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

fig.clear()
plt.close(fig=fig)


"""Change of K bounding cases with Mach"""

matplotlib.rcParams['figure.dpi'] = 160

mach_array = np.arange(0, 2, 0.001)

exconcept = ca.AircraftConcept(brief={}, design={}, performance={}, designatm={})

slopeslist = []
for mach_number in mach_array:
    slopeslist.append(exconcept.liftslope_prad(mach_number))

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

ax.plot(mach_array, slopeslist)
ax.fill([0.6, 0.6, 1.4, 1.4], [0, 14, 14, 0], color='green', alpha=0.1, label='$C_{L_{\\alpha}}$ = $f($Interpolation$)$')

ax.set_xlim(0, 2)
ax.set_ylim(0, 14)
ax.set_title('ADRpy Lift-slope vs Mach Model')
ax.set(xlabel='Mach Number', ylabel='Lift-slope $C_{L_{\\alpha}}$ [rad$^{-1}$]')
ax.legend()
ax.grid(True)
plt.show()

fig.clear()
plt.close(fig=fig)


"""Prediction of K"""

matplotlib.rcParams['figure.dpi'] = 160

mach_array = np.arange(0, 2, 0.001)

exbrief = {'cruisealt_m': 12000, 'cruisespeed_ktas': 570}
exdef = {'aspectratio': 4, 'sweep_le_deg': 27, 'sweep_25_deg': 20, 'wingarea_m2': 38, 'weight_n': 23541 * 9.81}
exconcept = ca.AircraftConcept(brief=exbrief, design=exdef, performance={}, designatm={})

klist = []
k0list = []
k100list = [1.0 / (math.pi * exconcept.aspectratio)] * 2
for mach_number in mach_array:
    klist.append(exconcept.induceddragfact_lesm(mach_inf=mach_number, cl_real=0.455))
    k0list.append(1 / exconcept.liftslope_prad(mach_inf=mach_number))

machstar_le = 1 / math.cos(math.radians(exconcept.sweep_le_deg))

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

ax.plot(mach_array, k0list, label="$K_0 = C_{L_{\\alpha}}^{-1}$", lw=2.5, color='royalblue')
ax.plot(np.array([0, 1]), np.array(k100list), label="$K_{100} = \\pi AR^{-1}$", lw=2.5, color='magenta')
ax.plot(np.array([1, 2]), np.array(k100list), alpha=0.2, lw=2.5, ls='--', color='magenta')
ax.plot(mach_array, klist, label="$K$", color='limegreen')

ax.plot(np.array([machstar_le, machstar_le]), np.array([0, 1]), color='k', ls='--')

ax.set_xlim(0, 2)
ax.set_ylim(0, 1.05 * max(k0list))
ax.set_title('ADRpy Induced Drag Factor $K$ vs Mach Model')
ax.set(xlabel='Mach Number', ylabel='Induced Drag Factor $K$')
ax.grid(True)
ax.legend(loc='best', ncol=3)
plt.show()

fig.clear()
plt.close(fig=fig)




"""Oswald"""

elist = []

for kfactor in klist:
    elist.append(1 / (math.pi * exconcept.aspectratio * kfactor))

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

ax.plot(mach_array, elist, label='LESM', c='purple')
ax.plot(mach_range, e4, label='[4] Nita, Scholz', c='orange')
ax.grid(True)
ax.set_title('ADRpy Oswald Efficiency Factor $e_0$ vs Mach Model')
ax.set(xlabel='Mach', ylabel='$e_0$')
ax.set_xlim(0, 2)
ax.set_ylim(0, 1)
ax.legend(title='Oswald Method', loc='best')
plt.show()

fig.clear()
plt.close(fig=fig)