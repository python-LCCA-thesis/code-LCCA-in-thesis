import numpy as np
import random
'''
    t = time_design (years)
    n1s = vehicle_design_traffic
    ADTT = numbers_single_axis_first_year
    n = numbers_single_axle_in_3000
    ps = axle_load_standards (kN)
    gr = growth_rate (%)
    dc = distribution_coefficient
    pi = percent_axle (%)
    Ne = vehicle_total
    kpi = convesion_coefficient
    PI = heavy_load_axle (KN)   
'''
    
def calculate_n1s(PI,pi,ADTT,n):
    ps = 100
    kpi = [(i/ps)**16 for i in PI]
    kpi = np.array(kpi)
    pi = np.array(pi)
    tmp_sum = sum( kpi * pi)
    return ADTT * (n / 3000.0) * tmp_sum
<<<<<<< HEAD
'''    
=======
    
>>>>>>> 013cc39d199e2ba4deb41f35b7e755cb360473f9
# dummy data ##########
PI = [100,200,300]    #
pi = [0.45,0.3,0.25]  #
ADTT = 2.8 * 10 ** 3  #
n = 500               #
#######################
n1s = calculate_n1s(PI,pi,ADTT,n)
print(n1s)
######################
<<<<<<< HEAD
'''
def ne(n1s,gr,t):
    dc = random.uniform(0.17,0.22)
    Ne = ((n1s * ((1 + gr)** t - 1) * 365) * dc) / gr
    return Ne
'''
# dummy data ########
gr = 0.012
t = 30
print(ne(n1s,gr,t,dc))
'''
=======
def ne(n1s,gr,t,dc):
    Ne = ((n1s * ((1 + gr)** t - 1) * 365) * dc) / gr
    return Ne

# dummy data ########
gr = 0.012
t = 30
dc = random.uniform(0.17,0.22)
print(ne(n1s,gr,t,dc))
>>>>>>> 013cc39d199e2ba4deb41f35b7e755cb360473f9
