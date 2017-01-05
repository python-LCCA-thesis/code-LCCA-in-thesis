
'''
    Dc = section_bending_stiffness (MN.m)
    r1 = relative_stiffness_radius (m)
    hc = pave_thickness (m)
    Ec = pave_elastic_module (MPa)
    Et = elastic_module_platform_subbase (MPa)
    uc = pave_poisson_coefficient (uc = 0.15) 
    ps = axle_load_standards (kN)
    pm = max_axle_load_standards (kN)
    Xps = tension_stresses_between_edge_slab (MPa)
    Xpm = tension_stresses_between_edge_slab_by_pmax (MPa)
'''
def section_bending_stiffness(Ec,hc):
    uc = 0.15
    Dc = ( Ec * hc**3 ) / ( 12 * (1 - uc**2) )
    return ( Ec * hc**3 ) / ( 12 * (1 - uc**2) )

def relative_stiffness_radius(Et):
    r1 = 1.12 * (( Dc / Et ) ** ( 1 / 3 ))
    return 1.21 * (( Dc / Et ) ** ( 1 / 3 ))

def tensile_stresses_edge_slab():
    ps = 100
    Xps = ( 1.47 * (10 ** -3) ) * r1 ** 0.7 * ( hc ** -2 ) * ( ps ** 0.94 )
    return ( 1.47 * (10 ** -3) ) * r1 ** 0.7 * ( hc ** -2 ) * ( ps ** 0.94 )
    
def max_tension_stresses_between_edge_slab():
    pm = 150
    Xpm = ( 1.47 * (10 ** -3) ) * r1 ** 0.7 * ( hc ** -2 ) * ( pm ** 0.94 )
    return ( 1.47 * (10 ** -3) ) * r1 ** 0.7 * ( hc ** -2 ) * ( pm ** 0.94 )
    
#############################
# from example 01 in QĐ3230 #
uc = 0.15                   #
Ec = 29000                  #
hc = 0.23                   #
ps = 100                    #
pm = 150                    #
# Et from result mod3       #
Et = 97.46                  #
#############################

Dc = ( Ec * hc**3 ) / ( 12 * (1 - uc**2) )
r1 = 1.21 * (( Dc / Et ) ** ( 1 / 3 ))
Xps = ( 1.47 * 10 ** -3 ) * r1 ** 0.7 * ( hc ** -2 ) * ( ps ** 0.94 )
Xpm = ( 1.47 * (10 ** -3) ) * r1 ** 0.7 * ( hc ** -2 ) * ( pm ** 0.94 )
print(Dc)
print(r1)
print(Xps)
print(Xpm)