import numpy as np
import math

'''
    hc = pave_thickness (m)
    Ec = pave_elastic_module (MPa)
    Tg = max_temperature_gradient (0C/m)
    Bl = thermal_tension_synthesis_coefficient
    Cl = bending_tension_coefficient
    C2 = two_layers_structural_slab_coefficient
    L = slab_length (m)
    r1 = relative_stiffness_radius (m)
    rb = exposure_coefficient (m)
    ac = expansion_coefficien (10^-6/0C)
    Xtmax = max_tension_stresses_between_edge_slab_by_thermal_fatigue (MPa)
    kt = bending_tensile_stress_thermal_fatigue_coefficient
    kn = vertically_contact_stiffness (Mpa/m)
    fr = bending_tensile_strength_design (MPa)
    highway express: fr >= 5.0 MPa 
'''
def vertically_contact_stiffness(hc,hb,Ec,Eb):
    kn = 1 / 2 * ( hc / Ec + hb / Eb ) ** -1
    return 1 / 2 * ( hc / Ec + hb / Eb ) ** -1
    
def exposure_coefficient(Dc,Db,kn):
    rb = ( ( Dc * Db ) / (( Dc + Db ) * kn ) ) ** ( 1 / 4 )
    return ( ( Dc * Db ) / (( Dc + Db ) * kn ) ) ** ( 1 / 4 )
    
def two_layers_structural_slab_coefficient(Dc,kn,r1,rb):
    C2 = [ ( ( kn * r1 ** 4 - Dc ) * ( rb ** 3 ) ) / ( ( kn * rb ** 4 - Dc ) * ( r1 ** 3 ) ) ] 
    return [ ( ( kn * r1 ** 4 - Dc ) * ( rb ** 3 ) ) / ( ( kn * rb ** 4 - Dc ) * ( r1 ** 3 ) ) ]

def bending_tension_coefficient(L,r1,C2):
    t = L / ( 3 * r1 )
    Cht = (( np.e ** t ) + ( np.e ** -t )) / 2
    Sht = (( np.e ** t ) - ( np.e ** -t )) / 2
    cos_t = math.cos(t)
    sin_t = math.sin(t)
    return 1 - ( 1 / ( 1 + C2 ) ) * (( Sht * cos_t + Cht * sin_t ) / ( cos_t * sin_t + Sht * Cht))

# dummy data ####################
L = 4.8                         #
r1 = 0.947                      #
hc = 0.26                       #
hb = 0.2                        #
Ec = 31000                      #
Eb = 1300                       #
Dc = 46.45                      #
Db = 0.903                      #
#################################

kn = vertically_contact_stiffness(hc,hb,Ec,Eb)
rb = exposure_coefficient(Dc,Db,kn)
C2 = two_layers_structural_slab_coefficient(Dc,kn,r1,rb)
Cl = bending_tension_coefficient(L,r1,C2)
print(kn)
print(rb)
print(C2)
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