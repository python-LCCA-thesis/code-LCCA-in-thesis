import numpy as np
import math

'''
    Et = elastic_module_platform_subbase (MPa)
    E0 = elastic_module_platform (MPa)
    Ei = elastic_module_layer_i (MPa)
    Ex = elastic_module_equivalent (MPa)
    hi = thickness_layer_i (m)
    hx = total_thickness_layers (m)
    a = regression_coefficient
    n = number_of_layers
'''

def total_thickness_layers(hi):
    hx = sum (hi)
    return hx

def regression_coefficient(hi):
    hx = sum (hi)
    a = 0.86 + 0.26 * math.log(hx, np.e)
    return a

def elastic_module_platform_subbase(hi,Ei,hx):
    a = 0.86 + 0.26 * math.log(hx, np.e)
    E0 = 40
    Ei = np.array(Ei)
    hi = np.array(hi)
    Ex = (sum ( hi ** 2 ) * Ei) / (sum (hi ** 2))
    return ((Ex / E0) ** a) * E0

'''
# dummy data ########################
# hi & Ei from example1 in QĐ3230   #
hi = [0.2]                          #
Ei = [300]                          #
#####################################
'''

a = regression_coefficient(hi)
hx = total_thickness_layers(hi)
Et = elastic_module_platform_subbase(hi,Ei,hx)

print(a)
print(hx)
print(Et)
