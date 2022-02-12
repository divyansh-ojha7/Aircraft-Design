from ADRpy import propulsion as decks
import numpy as np
import matplotlib.pyplot as plt
import ADRpy.atmospheres as atm


"""Turboprop Deck"""

decks.local_data("turboprop")

turbo = decks.TurbopropDeck("Tyne_RTy11")  # Selects data for Rolls Royce Tyne.
mach = np.linspace(0, 1, 100)  # Creates array for mach data.
altitude = np.linspace(0, 10000, 5)  # Creates an array for altitude data.
fig, ax1 = plt.subplots(figsize=(10, 10))  # Creates figure to plot.
fig.subplots_adjust(right=0.75)
ax2 = ax1.twinx()  # shares x axis with ax1
ax3 = ax1.twinx()  # shares x axis with ax1
ax3.spines["right"].set_position(("axes", 1.2))  # Moves the legend
# Plots a line for each altitude
for alt in altitude:
    # Calculates Thrust
    # Plots power (W)
    ax1.plot(mach, turbo.shaftpower(mach, alt), label="Thrust (N) at " + str(alt) + " m")
    # Plots TSFC g/(kNs)
    ax2.plot(mach, turbo.bsfc(mach, alt), "--", label="BSFC (g/(kWh) at " + str(alt) + " m")
    # Plots Thrust (N)
    ax3.plot(mach, turbo.hotthrust(mach, alt), ":", label="Hot Thrust (N) at " + str(alt) + " m")
fig.legend(loc="center", bbox_to_anchor=(1.15, 0.9))  # Plots the legend
fig.tight_layout()  # Fits subplot in figure area.
ax1.set_title("Hot Thrust, Power and BSFC for Mach Number and Altitude")  # Sets Title
ax1.set_xlabel("Mach Number")  # Sets x label
ax1.set_ylabel("Power (W)")  # Sets left hand y label
ax2.set_ylabel("TSFC (g/(kNs)")  # Sets right hand y label
ax3.set_ylabel("Hot Thrust (N)")  # Sets right hand y label
None


"""Demo Plots"""

turbo.demoplot_thrust()
turbo.demoplot_shaftpower()
turbo.demoplot_bsfc()



"""Jet Deck"""

decks.local_data("jet")

jet = decks.JetDeck("JT8D-9")  # Selects data for JT8D-9.
mach = np.linspace(0, 1, 100)  # Creates array for mach data.
altitude = np.linspace(0, 10000, 5)  # Creates an array for altitude data.
fig, ax1 = plt.subplots(figsize=(10, 10))  # Creates figure to plot.
ax2 = ax1.twinx()  # shares x axis with ax1
# Plots a line for each altitude
for alt in altitude:
    # Calculates Thrust
    thrust = jet.thrust(mach, alt)
    # Plots Thrust (N)
    ax1.plot(mach, thrust, label="Thrust (N) at " + str(alt) + " m")
    # Plots TSFC g/(kNs)
    ax2.plot(mach, jet.tsfc(mach, thrust), "--", label="TSFC (g/(kNs) at " + str(alt) + " m")
fig.legend(loc="center", bbox_to_anchor=(1.15, 0.9))  # Plots the legend
fig.tight_layout()  # Fits subplot in figure area.
ax1.set_title("Thrust and TSFC for Mach Number and Altitude")  # Sets Title
ax1.set_xlabel("Mach Number")  # Sets x label
ax1.set_ylabel("Thrust (N)")  # Sets left hand y label
ax2.set_ylabel("TSFC (g/(kNs)")  # Sets right hand y label
None

# Jet Polynomials
print(jet.sl_thrust(0.4), "N Thrust\n", jet.sl_take_off_thrust(0.4), "N Thrust")

"""Demo Plots"""

jet.demoplot_thrust()
jet.demoplot_tsfc()



"""Mattingly Comparison"""

isa_atm = atm.Atmosphere()

engine = "JT9D-3"
turbofan = decks.JetDeck(engine)
zerothrust = 155000 # Sets zero altitude and mach thrust
isa_alt = np.linspace(0, 15000, 11)  # ISA Altitude data (m)
mach_no = np.linspace(0, 1, 100)  # Mach number data
isa_temp = isa_atm.airtemp_c(isa_alt) # Temperatures for ISA standard atmosphere.
isa_press = isa_atm.airpress_pa(isa_alt)  # Pressure for ISA standard atmosphere.
plt.figure(figsize=(10, 10))  # Creates figure and sets size
# Creates thrust curve for each altitude
for index, altitude in enumerate(isa_alt):
    # Plots interpolated data
    thrust = turbofan.thrust(mach_no, altitude)
    plt.plot(mach_no, thrust, color="C" + str(index)[-1], ls="--",
             label = str(round(altitude, 2)) + " Altitude (m) for " + engine)
    for index, value in enumerate(thrust):
        type(np.isnan(value))
        if np.isnan(value) == False:
            plt.text(mach_no[index], thrust[index], str(round(altitude, 2)) + " m")
            break
throttleratio = 0.85
# Creates curve using Mattingly method in ADRpy.
for index, altitude in enumerate(isa_alt):
    # scales zerothrust so that for any throttle ratio, the data fits
    zerothrust2 = zerothrust/atm.turbofanthrustfactor(isa_temp[0], isa_press[0], 0,throttleratio, ptype = "highbpr")
    data_list = []
    for mach in mach_no:
        data_list.append(zerothrust2 * atm.turbofanthrustfactor(isa_temp[index], isa_press[index], mach,
                                                               throttleratio, ptype = "highbpr"))
    plt.plot(mach_no, data_list, color="C" + str(index)[-1], ls="-", label = str(round(altitude, 2)) +
             " Altitude (m) for " + engine)
    plt.text(mach_no[0], data_list[0], str(round(altitude, 2)) + " m")
plt.title(engine + " data (dashed) against Mattingly data (solid). Altitude for an ISA standard atmosphere labelled on chart")
plt.xlabel("Mach Number")  # Plots x label
plt.ylabel("Thrust N")  # Plots y label
plt.show()  # Shows plot


"""Piston Decks"""

decks.local_data("piston")

piston = decks.PistonDeck("IO-540")  # Selects data for the IO-540
engine_speed = np.linspace(2000, 3000, 100)  # Creates array for mach data.
altitude = np.linspace(0, 6000, 5)  # Creates an array for altitude data.
fig, ax1 = plt.subplots(figsize=(10, 10))  # Creates figure to plot.
ax2 = ax1.twinx()  # shares x axis with ax1
ax3 = ax1.twinx()  # shares x axis with ax1
# Plots a line for each altitude
for alt in altitude:
    power = piston.shaftpower(engine_speed, alt)
    # Plots Thrust (N)
    ax1.plot(engine_speed, power, label="Thrust (N) at " + str(alt) + " m")
    # Plots TSFC g/(kNs)
    ax2.plot(engine_speed, piston.bsfc(engine_speed, power), "--", label="BSFC (g/(kWh) at " + str(alt) + " m")
    ax3.plot(engine_speed, piston.bsfc(engine_speed, power, best="economy"), ":", label="BSFC (g/(kWh) at " + str(alt) + " m")
fig.legend(loc="center", bbox_to_anchor=(1.15, 0.9))  # Plots the legend
fig.tight_layout()  # Fits subplot in figure area.
ax2.set_ylim(bottom=275, top=425)  # Sets limits for y axis
ax3.set_ylim(bottom=275, top=425)  # Sets limits for y axis
ax3.axis("off")  # Turns off axis
ax1.set_title("Power and BSFC for Engine Speed and Altitude")  # Sets Title
ax1.set_xlabel("Engine Speed (RPM)")  # Sets x label
ax1.set_ylabel("Power (W)")  # Sets left hand y label
ax2.set_ylabel("BSFC (g/(kWh)")  # Sets right hand y label
None


"""Demo Plots"""

piston.demoplot_shaftpower()
piston.demoplot_bsfc(best="power")
piston.demoplot_bsfc(best="economy")  # Default



"""Electric Deck"""

decks.local_data("electric")

electric = decks.ElectricDeck("JMX57")  # Selects data for JMX57
engine_speed = np.linspace(0, 3000, 100)  # Creates array for engine speed
torque = np.linspace(0, 500, 9)  # Creates an array for torque
fig, ax1 = plt.subplots(figsize=(10, 10))  # Creates figure to plot.
# Plots a line for each altitude
for torq in torque:
    # Plots efficiency
    ax1.plot(engine_speed, electric.efficiency(engine_speed, torq), label="Efficiency at " + str(torq) + " Nm")
fig.legend(loc="center", bbox_to_anchor=(1.15, 0.9))  # Plots the legend
fig.tight_layout()  # Fits subplot in figure area.
ax1.set_title("Efficiency for Engine Speed and Torque")  # Sets Title
ax1.set_xlabel("Engine Speed (RPM)")  # Sets x label
ax1.set_ylabel("Torque (Nm)")  # Sets y label
None


"""Demo Plots"""
electric.demoplot_efficiency()


"""Propeller Deck"""

propeller_spec = {'diameter_m': 3, 'bladecount': 2, 'bladeactivityfact': 150,
                 'solidity': False, 'idesign_cl': 0.15}

#Instantiate an object of the PropellerDeck class
testpropeller = decks.PropellerDeck(propeller_spec)

etaprop = testpropeller.efficiency(mach=0.6, altitude_m=3000, shaftpower_w=522000, prop_rpm=2000)

print("Propeller efficiency:", etaprop)

#Instantiate an object of the PropellerDeck class
ansatzpropeller = decks.PropellerDeck()

ansatzpropeller.ansatzprop(mach=0.6, altitude_m=3000, prop_rpm=2000, shaftpower_w=522000)

etaprop = ansatzpropeller.efficiency(mach=0.6, altitude_m=3000, prop_rpm=2000, shaftpower_w=522000)

print("Propeller efficiency:", etaprop)