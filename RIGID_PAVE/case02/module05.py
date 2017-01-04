'''
    Xps = tension_stresses_between_edge_slab (MPa)
    Xpr = fatigue_stresses_between_edge_slab (MPa)
    Xpm = tension_stresses_between_edge_slab_by_pmax (MPa)
    Xpmax = max_tension_stresses_between_edge_slab_by_pmax (MPa)
    kr = tension_diminished_coefficient
    kf = fatigue_coefficient
    Ne = vehicle_total
    A = 0.057 if_base_is_crushed_aggregate
    A = 0.065 if_base_is_roller_compacted_concre
    kc = synthetic_coefficient
    highway express => kc = 1.15
'''
def fatigue_coefficient(A):
    Ne = 2.8 * (10 ** 4)
    return Ne ** A
    
# dummy data ################
#Xps from result mod4       #
Xps = 1.831                 #
#Xpm from result mod4       #
Xpm = 2.681                 #
#Ne from example1 in QĐ3230 #
Ne = 2.8 * (10 ** 4)        #
A = 0.057                   #
kr = 1                      #
kc = 1.0                    #
#############################

kf = Ne ** A
print (kf)

def fatigue_stresses_between_edge_slab(A,Xps,Ne):
    kr = 1
    kf = Ne ** A
    kc = 1.0
    return kr * kf * kc * Xps
    
def max_tension_stresses_between_edge_slab(Xpm):
    Xpmax = kr * kc * Xpm
    return kr *kc *Xpm

Xpr = kr * kf * kc * Xps
Xpmax = kr *kc * Xpm

print(Xpr)
print(Xpmax)
