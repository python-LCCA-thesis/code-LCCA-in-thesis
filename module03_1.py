import numpy as np
import math

'''
    Et = elastic_module_platform_subbase
    E0 = elastic_module_platform
    Ei = elastic_module_layer_i
    Ex = elastic_module_equivalent
    hi = thickness_layer_i
    hx = total_thickness_layers
    a = regression_coefficient
    n = number_of_layers
'''

def elastic_module_platform_subbase(hi,Ei,hx):
    a = 0.86 + 0.26 * math.log(hx, np.e)
    E0 = 45
    Ei = np.array(Ei)
    hi = np.array(hi)
    Ex = (sum ( hi ** 2 ) * Ei) / (sum (hi ** 2))
    return ((Ex / E0) ** a) * E0

#################
hi = [0.18]     #
Ei = [300]      #
hx = 0.18       #
#################

Et = elastic_module_platform_subbase(hi,Ei,hx)
print(Et)