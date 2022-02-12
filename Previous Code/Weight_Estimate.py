import math

choice = float(input('choose a plane and input 1,2,or 3... 1 for single engine... 2 for twin engine... '
                     '3 for buisness jet: '))
rangecr = float(input('range of cruise: '))
warmup = None
taxi = None
takeoff = None
climb = None
descent = None
shutdown = None
cruise = None
loiterres=None
loiter=None
A=None
B=None


if choice == 1:
    A = -0.144
    B = 1.1162
    warmup = 0.995
    taxi = 0.997
    takeoff = 0.998
    climb = 0.992
    descent = 0.993
    shutdown = 0.993
    np = 0.8
    cp = 0.6
    ldcr = 9
    ldltr = 11
    npltr = 0.7
    cpltr = 0.6
    Vltr = float(input('loiter velocity in mph: '))
    Eltr = float(input('time of loiter: '))
    cruise = ((math.exp(rangecr / (375 * (np / cp) * ldcr))) ** -1)
    loiter = (math.exp(Eltr * Vltr / (ldltr * (375 * (npltr / cpltr)))) ** -1)
    loiterres = (math.exp(0.75 * Vltr / (ldltr * (375 * (npltr / cpltr)))) ** -1)

if choice == 2:
    A = 0.0966
    B = 1.0298
    warmup = 0.992
    taxi = 0.996
    takeoff = 0.996
    climb = 0.990
    descent = 0.992
    shutdown = 0.992
    np = 0.82
    cp = 0.6
    ldcr = 9
    ldltr = 10
    npltr = .72
    cpltr = .6
    Vltr = float(input('loiter velocity in mph: '))
    Eltr = float(input('time of loiter in hours: '))
    cruise = ((math.exp(rangecr / (375 * (np / cp) * ldcr))) ** -1)
    loiter = (math.exp(Eltr * Vltr / (ldltr * (375 * (npltr / cpltr)))) ** -1)
    loiterres = (math.exp(0.75 * Vltr / (ldltr * (375 * (npltr / cpltr)))) ** -1)

if choice == 3:
    A = 0.2678
    B = 0.9979
    warmup = 0.990
    taxi = 0.995
    takeoff = 0.995
    climb = 0.980
    descent = 0.990
    shutdown = 0.992
    cj = 0.7
    ldcr = 11
    ldltr = 13
    cjltr = 0.5
    Eltr = float(input('time of loiter in hours: '))
    vcr = float(input('velocity equals cruising speed in nm per hour: '))
    cruise = (math.exp(rangecr / (vcr / cj * ldcr)) ** -1)
    loiter = ((math.exp((cjltr * Eltr) / ldltr)) ** -1)
    loiterres = ((math.exp((cjltr * 0.75) / ldltr)) ** -1)

Wtoguess = float(input('enter weight of take off (a good weight estimate is ~4000): '))
# equation calculates weight of needed fuel
Wfused = (1 - warmup * taxi * takeoff * climb * descent * shutdown * loiter * cruise) * Wtoguess
Wres = (1 - climb * descent * loiterres * shutdown) * Wtoguess  # equation calculates weight of needed fuel reserves
Wcrew = 180
numpas = float(input('number of pasengers: '))
Wpl = numpas * 200  # as per regulations 175 per person 25 per bag
Wtf = 2 * 7.5 + 0.5 * 6  # 2 gallons at 7.5 lbs a gallon of oil and 1/2 a gallon of unusable gasoline
We = 10 ** ((math.log10(Wtoguess) - A) / B)  # equation gives a guess for empty weight
Woe = We + Wtf + Wcrew  # definition of empty weight
Wf = Wfused + Wres  # total Weight of fuel
Wto = Woe + Wf + Wpl  # Weight of take off based on empty wieght fuel weight and payload weight

print("Empty dry weight: " + str(We))
print("Empty weight: " + str(Woe))
print("Weight of fuel including reserves: " + str(Wf))
print("Total weight: " + str(Wto))
