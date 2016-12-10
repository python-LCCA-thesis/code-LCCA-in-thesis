import numpy as np
import random
'''
    t = time_design
    n1s = vehicle_design_traffic
    ADTT = numbers_single_axis_first_year
    n = numbers_single_axle_in_3000
    ps = axle_load_standards (kN)
    gr = growth_rate
    dc = distribution_coefficient
    pi = percent_axle
    ne = vehicle_total
    kpi = convesion_coefficient
    nsa []
    
'''
    
def calculate_n1s(PI,pi,ADTT,n):
    ps = 100
    kpi = [(i/ps)**16 for i in PI]
    kpi = np.array(kpi)
    pi = np.array(pi)
    tmp_sum = sum( kpi * pi)
    return ADTT * (n / 3000) * tmp_sum
    
# dummy data ##########
PI = [100,200,300]    #
pi = [0.45,0.3,0.25]  #
ADTT = 2.8 * 10 ** 3  #
n = 500               #
#######################
n1s = calculate_n1s(PI,pi,ADTT,n)
print(n1s)
######################
def ne(n1s,gr,t,dc):
    ne = ((n1s * ((1 + gr)** t - 1) * 365) * dc) / gr
    return ne

# dummy data ########
gr = 0.012
t = 30
dc = random.uniform(0.17,0.22)
print(ne(n1s,gr,t,dc))