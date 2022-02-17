"""
Intermediate Values
2/12/22
"""

from Wing_Sizing import *

# 2D Analysis
a0 = avscl_data[0]
alpha_l0 = avscl_data[1]

# 3D Analysis
a = a0 / (1 + ((57.3*a0) / (math.pi * e * AR)))
Cl_3D = [a * (x - alpha_l0) for x in alpha]
Cd_3D = [c_d_0 + k*(x**2) for x in Cl_3D]

print(f'a0 = {a0}')
print(f'alpha_l0 = {alpha_l0} deg')
print(f'a = {a}')
print(f'k = {k}')
print(f'cl_max = {cl_max}')
print(f'c_d_0 = {c_d_0}')


plt.plot(alpha,Cl_3D,label='$C_L$ (3D)')
plt.plot(alpha,Cl,label='$C_l$ (2D)')
plt.xlabel('Alpha')
plt.ylabel('$C_L$ (3D) and $C_l$ (2D)')
plt.title('Alpha vs $C_L$ (3D) and $C_l$ (2D)')
plt.legend()
plt.show()

# Efficiency Ratios

eff_32 = 3**(3/4) / (4*c_d_0**(1/4)*k**(3/4))  # 3/2 Efficiency Ratio
eff = math.sqrt(1 / (4*k*c_d_0))  # Cl/Cd Efficiency Ratio
eff_12 = 0.75 * (1 / 3*k*(c_d_0**3))**(1/4)  # 1/2 Efficiency Ratio

v_max_end = math.sqrt((2*(m_takeoff*g) / (rho_0*S_to) * math.sqrt(k / c_d_0)))
v_max_range = math.sqrt((2*(m_takeoff*g) / (rho_0*S_to) * math.sqrt((3*k) / c_d_0)))

# Other Values
W = m_takeoff*9.81
v_stall = math.sqrt((2*W) / (rho_0 * S_to * cl_max))

print(f'm_takeoff = {m_takeoff} kg')
print(f'm_landing = {m_landing} kg')
print(f'v_stall = {v_stall} m/s')

# Range and Endurance
tsfc = 5.4*10**-5  # g/(N*s)
endur_max = (1 / (tsfc*g)) * eff * math.log(m_takeoff / m_landing)
range_max = (2 / g) * (math.sqrt(2 / (rho_0 * S_to))) * (1 / tsfc) * eff_12 * (math.sqrt(m_takeoff * g) - math.sqrt(m_landing * g))

print(f'endur_max = {endur_max} s, or {endur_max / (60*60)} hours')
print(f'range_max = {range_max} m')