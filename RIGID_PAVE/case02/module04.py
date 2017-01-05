
'''
    Dc = section_bending_stiffness (MN.m)
    Db = base_bending_stiffness (MN.m)
    r1 = relative_stiffness_radius (m)
    hc = pave_thickness (m)
    hb = base_thickness (m)
    Ec = pave_elastic_module (MPa)
    Eb = base_elastic_module (MPa)
    Et = elastic_module_platform_subbase (MPa)
    uc = pave_poisson_coefficient (uc = 0.15) 
    ps = axle_load_standards (kN)
    pm = max_axle_load_standards (kN)
    Xps = tension_stresses_between_edge_slab (MPa)
    Xpm = tension_stresses_between_edge_slab_by_pmax (MPa)
'''
def section_bending_stiffness(Ec,hc):
    uc1 = 0.15
    Dc = ( Ec * hc**3 ) / ( 12 * (1 - uc1**2) )
    return ( Ec * hc**3 ) / ( 12 * (1 - uc1**2) )
    
def base_bending_stiffness(Eb,hb):
    uc2 = 0.2
    Db = ( Eb * hb**3 ) / ( 12 * (1 - uc2**2) )
    return ( Eb * hb**3 ) / ( 12 * (1 - uc2**2) )

def relative_stiffness_radius(Et):
    r1 = 1.21 * ((( Dc + Db ) / Et ) ** ( 1 / 3 ))
    return 1.21 * ((( Dc + Db ) / Et ) ** ( 1 / 3 ))

def tensile_stresses_edge_slab():
    ps = 100
    Xps = ( 1.45 * (10 ** -3) / ( 1 + Db / Dc ) ) * r1 ** 0.65 * ( hc ** -2 ) * ( ps ** 0.94 )
    return ( 1.45 * (10 ** -3) / ( 1 + Db / Dc ) ) * r1 ** 0.65 * ( hc ** -2 ) * ( ps ** 0.94 )
    
def max_tension_stresses_between_edge_slab():
    pm = 180
    Xpm = ( 1.45 * (10 ** -3) / ( 1 + Db / Dc ) ) * r1 ** 0.65 * ( hc ** -2 ) * ( pm ** 0.94 )
    return ( 1.45 * (10 ** -3) / ( 1 + Db / Dc ) ) * r1 ** 0.65 * ( hc ** -2 ) * ( pm ** 0.94 )
    
#############################
# from example 01 in QD3230 #
uc1 = 0.15                  #
uc2 = 0.2                   #
Ec = 31000                  #
Eb = 1300                   #
hc = 0.26                   #
hb = 0.2                    #
ps = 100                    #
pm = 180                    #
# Et from result mod3       #
Et = 98.7                   #
#############################

Dc = section_bending_stiffness(Ec,hc)
Db = base_bending_stiffness(Eb,hb)
r1 = relative_stiffness_radius(Et)
Xps = tensile_stresses_edge_slab()
Xpm = max_tension_stresses_between_edge_slab()

print(Dc)
print(Db)
print(r1)
print(Xps)
print(Xpm)