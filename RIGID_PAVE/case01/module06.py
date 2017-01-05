import numpy as np
import math

'''
    hc = pave_thickness (m)
    Ec = pave_elastic_module (MPa)
    Tg = max_temperature_gradient (0C/m)
    Bl = thermal_tension_synthesis_coefficient
    Cl = bending_tension_coefficient
    L = slab_length (m)
    r1 = relative_stiffness_radius (m)
    ac = expansion_coefficien (10^-6/0C)
    Xtmax = max_tension_stresses_between_edge_slab_by_thermal_fatigue (MPa)
    kt = bending_tensile_stress_thermal_fatigue_coefficient 
    fr = bending_tensile_strength_design (MPa)
    highway express: fr >= 5.0 MPa 
'''
 
def bending_tension_coefficient(L,r1):
    t = L / ( 3 * r1 )
    Cht = (( np.e ** t ) + ( np.e ** -t )) / 2
    Sht = (( np.e ** t ) - ( np.e ** -t )) / 2
    return 1 - (( Sht * math.cos(t) + Cht * math.sin(t) ) / ( math.cos(t) * math.sin(t) + Sht * Cht))

# dummy data ####################
# L from example1 in QĐ3230     #
L = 4.5                         #
# r1 from result mod4           #
r1 = 0.818                      #
# hc from result mod3           #
hc = 0.23                       #
#################################

Cl = bending_tension_coefficient(L,r1)
print(Cl)

#################################

def thermal_tension_synthesis_coefficient(hc):
    Bl = 1.77 * ( np.e ** (-4.48 * hc) ) * Cl - 0.131 * ( 1 - Cl )
    return 1.77 * ( np.e ** (-4.48 * hc) ) * Cl - 0.131 * ( 1 - Cl )
    
Bl = thermal_tension_synthesis_coefficient(hc)
print(Bl)

# dummy data ####################
# Ec from example1 in QĐ3230    #
Ec = 29000                      #
# Tg from example1 in QĐ3230    #
Tg = 86                         #
# ac from example1 in QĐ3230    #
ac = 10**-5                     #
#################################

def max_tension_stresses_between_edge_slab_by_thermal_fatigue(Tg):
    Xtmax = ( ac * hc * Ec * Tg / 2 ) * Bl
    return ( ac * hc * Ec * Tg / 2 ) * Bl

Xtmax = max_tension_stresses_between_edge_slab_by_thermal_fatigue(Tg)
print(Xtmax)

#################################

def bending_tensile_stress_thermal_fatigue_coefficient_1(fr,at1,bt1,ct1):
    kt1 = ( fr / Xtmax ) * ( at1 * ( ( Xtmax / fr ) ** bt1 ) - ct1)
    return ( fr / Xtmax ) * ( at1 * ( ( Xtmax / fr ) ** bt1 ) - ct1)

def bending_tensile_stress_thermal_fatigue_coefficient_2(fr,at2,bt2,ct2):
    kt2 = ( fr / Xtmax ) * ( at2 * ( ( Xtmax / fr ) ** bt2 ) - ct2)
    return ( fr / Xtmax ) * ( at2 * ( ( Xtmax / fr ) ** bt2 ) - ct2)

# dummy data ####################
# fr from example1 in QĐ3230    #
fr = 4.5                        #
at1 = 0.841                     #
bt1 = 1.323                     #
ct1 = 0.058                     #
at2 = 0.871                     #
bt2 = 1.287                     #
ct2 = 0.071                     #
#################################

kt1 = bending_tensile_stress_thermal_fatigue_coefficient_1(fr,at1,bt1,ct1)
kt2 = bending_tensile_stress_thermal_fatigue_coefficient_2(fr,at2,bt2,ct2)

print(kt1)
print(kt2)

list1 = [kt1, kt2]
for i in list1:
    kt = max(list1)
print(kt)