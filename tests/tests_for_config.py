# -*- coding: utf-8 -*-



import sys
if "/home/peter/Programme/accobs_Projekt/accobs_repo/accobs" in sys.path:
    print("Schon da.")
else:
    sys.path.append("/home/peter/Programme/accobs_Projekt/accobs_repo/accobs")
    print("Hinzugefügt.")

# import base.SRS_string
import accobs.base.obs_sys_configuration as OSConfig


cf11 = OSConfig.Obs_Sys_Configuration("aabbaac", "DFRS")
cf12 = OSConfig.Obs_Sys_Configuration("aabbaac", "DFRS")
cf21 = OSConfig.Obs_Sys_Configuration("aabbaac", "DFRSD")
cf13 = OSConfig.Obs_Sys_Configuration("aabbaacd", "DFRS")
cf31 = OSConfig.Obs_Sys_Configuration("aabbaac", "CCCC")

print(cf11 == cf12)
print(cf11 == cf21)
print(cf11 == cf13)
print(cf11 == cf31)


print( "     Inequalities " )

print(cf11 < cf12)
print(cf11 < cf21)
print(cf11 < cf13)
print(cf11 > cf21)
print(cf11 > cf13)
print(cf11 < cf31)
print(cf11 > cf31)

sys.path.remove("/home/peter/Programme/accobs_Projekt/accobs_repo/accobs")

# print(sys.path)