import numpy as np
import random
'''
    hl = heaviest_load
    t = time_design
    vdf = vehicle_design_traffic
    nsafy = numbers_single_axis_first_year
    n30 = numbers_single_axle_in_3000
    als = axle_load_standards (kN)
    gr = growth_rate
    dc = distribution_coefficient
    pa = percent_axle
    vfy = ADTT
    ne = vehicle_total
    cc = convesion_coefficient
    nsa []
    
    
    '''
    
def calculate_vdf(nsa,pa,nsafy,n30):
    als = 100
    cc = [(i/als)**16 for i in nsa]
    cc = np.array(cc)
    pa = np.array(pa)
    tmp_sum = sum( cc * pa)
    return nsafy * (n30 / 3000) * tmp_sum
    
# dummy data ##########
nsa = [100,200,300]   #
pa = [0.45,0.3,0.25]  #
nsafy = 2.8 * 10 ** 3 #
n30 = 500             #
#######################
vdf = calculate_vdf(nsa,pa,nsafy,n30)
print(vdf)
######################
def ne(vdf,gr,t,dc):
    ne = ((vdf * ((1 + gr)** t - 1) * 365) * dc) / gr
    return ne

# dummy data ########
gr = 0.012
t = 30
dc = random.uniform(0.17,0.22)
print(ne(vdf,gr,t,dc))