import pandas as pd

import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
import numpy as np

df_NACA0014 = pd.read_csv("NACA0014_XFLR5.csv")
alpha_NACA0014 = df_NACA0014["alpha"]
CL_NACA0014 = df_NACA0014["CL"]
CD_NACA0014 = df_NACA0014["CD"]
CM_NACA0014 = df_NACA0014["Cm"]

df_NACA4415 = pd.read_csv("NACA4415_XFLR5.csv")
alpha_NACA4415 = df_NACA4415["alpha"]
CL_NACA4415 = df_NACA4415["CL"]
CD_NACA4415 = df_NACA4415["CD"]
CM_NACA4415 = df_NACA4415["Cm"]

df_NACA4417 = pd.read_csv("NACA4417_XFLR5.csv")
alpha_NACA4417 = df_NACA4417["alpha"]
CL_NACA4417 = df_NACA4417["CL"]
CD_NACA4417 = df_NACA4417["CD"]
CM_NACA4417 = df_NACA4417["Cm"]

df_NACA2411 = pd.read_csv("NACA2411_XFLR5.csv")
alpha_NACA2411 = df_NACA2411["alpha"]
CL_NACA2411 = df_NACA2411["CL"]
CD_NACA2411 = df_NACA2411["CD"]
CM_NACA2411 = df_NACA2411["Cm"]

df_NACA4424 = pd.read_csv("NACA4424_XFLR5.csv")
alpha_NACA4424 = df_NACA4424["alpha"]
CL_NACA4424 = df_NACA4424["CL"]
CD_NACA4424 = df_NACA4424["CD"]
CM_NACA4424 = df_NACA4424["Cm"]

df_NACA6412 = pd.read_csv("NACA6412_XFLR5.csv")
alpha_NACA6412 = df_NACA6412["alpha"]
CL_NACA6412 = df_NACA6412["CL"]
CD_NACA6412 = df_NACA6412["CD"]
CM_NACA6412 = df_NACA6412["Cm"]

plt.plot(alpha_NACA0014, CL_NACA0014, label='NACA 0014')
plt.plot(alpha_NACA4415, CL_NACA4415, label='NACA 4415')
plt.plot(alpha_NACA4417, CL_NACA4417, label='NACA 4417')
plt.plot(alpha_NACA2411, CL_NACA2411, label='NACA 2411')
plt.plot(alpha_NACA4424, CL_NACA4424, label='NACA 4424')
plt.plot(alpha_NACA6412, CL_NACA6412, label='NACA 6412')
plt.title('$C_L$ vs Alpha')
plt.xlabel('Alpha')
plt.ylabel('$C_L$')
plt.legend()
plt.grid()
plt.show()

plt.plot(CD_NACA0014, CL_NACA0014, label='NACA 0014')
plt.plot(CD_NACA4415, CL_NACA4415, label='NACA 4415')
plt.plot(CD_NACA4417, CL_NACA4417, label='NACA 4417')
plt.plot(CD_NACA2411, CL_NACA2411, label='NACA 2411')
plt.plot(CD_NACA4424, CL_NACA4424, label='NACA 4424')
plt.plot(CD_NACA6412, CL_NACA6412, label='NACA 6412')
plt.title('$C_L$ vs $C_D$')
plt.xlabel('$C_D$')
plt.ylabel('$C_L$')
plt.legend(loc='lower right')
plt.grid()
plt.show()

plt.plot(alpha_NACA0014, CM_NACA0014, label='NACA 0014')
plt.plot(alpha_NACA4415, CM_NACA4415, label='NACA 4415')
plt.plot(alpha_NACA4417, CM_NACA4417, label='NACA 4417')
plt.plot(alpha_NACA2411, CM_NACA2411, label='NACA 2411')
plt.plot(alpha_NACA4424, CM_NACA4424, label='NACA 4424')
plt.plot(alpha_NACA6412, CM_NACA6412, label='NACA 6412')
plt.title('Cm vs Alpha')
plt.xlabel('Alpha')
plt.ylabel('Cm')
plt.legend()
plt.grid()
plt.show()

CLD_NACA0014 = CL_NACA0014 / CD_NACA0014
CLD_NACA4415 = CL_NACA4415 / CD_NACA4415
CLD_NACA4417 = CL_NACA4417 / CD_NACA4417
CLD_NACA2411 = CL_NACA2411 / CD_NACA2411
CLD_NACA4424 = CL_NACA4424 / CD_NACA4424
CLD_NACA6412 = CL_NACA6412 / CD_NACA6412

plt.plot(alpha_NACA0014, CLD_NACA0014, label='NACA 0014')
plt.plot(alpha_NACA4415, CLD_NACA4415, label='NACA 4415')
plt.plot(alpha_NACA4417, CLD_NACA4417, label='NACA 4417')
plt.plot(alpha_NACA2411, CLD_NACA2411, label='NACA 2411')
plt.plot(alpha_NACA4424, CLD_NACA4424, label='NACA 4424')
plt.plot(alpha_NACA6412, CLD_NACA6412, label='NACA 6412')
plt.title('$C_L$/$C_D$ vs Alpha')
plt.xlabel('Alpha')
plt.ylabel('$C_L$/$C_D$')
plt.legend()
plt.grid()
plt.show()