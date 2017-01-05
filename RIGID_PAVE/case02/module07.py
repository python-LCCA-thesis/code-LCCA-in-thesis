
'''
    yr = reliability_coefficient
    Xtmax = max_tension_stresses_between_edge_slab_by_thermal_fatigue (MPa)
    Xpmax = max_tension_stresses_between_edge_slab_by_pmax (MPa)
    Xpr = fatigue_stresses_between_edge_slab (MPa)
    Xtr = tension_stresses_between_edge_slab_by_thermal_fatigue (MPa)
    fr = bending_tensile_strength_design (MPa)
'''
def tension_stresses_between_edge_slab_by_thermal_fatigue(kt,Xtmax):
    Xtr = kt * Xtmax
    return kt * Xtmax

# dummy data ####################
# kt, Xtmax from mod6           #
Xtmax = 1.282                   #
kt = 0.357                      #
#################################

Xtr = tension_stresses_between_edge_slab_by_thermal_fatigue(kt,Xtmax)
print(Xtr)

# dummy data ####################
# Xpr from mod5                 #
Xpr = 3.282                     #
Xpmax = 2.681                   #
# Xtmax from mod6               #
Xtmax = 1.282                   #
# yr from example1 in QĐ3230    #
yr = 1.04                       #
fr = 4.5                        #
#################################

if yr * ( Xpmax + Xtmax ) <= fr and yr * ( Xpr + Xtr ) <= fr:
    print("satisfactory")
    if yr * ( Xpmax + Xtmax ) > fr or yr * ( Xpr + Xtr ) > fr:
        print ('unsatisfactory')
        
    