import math
def sum_of_multiples(limit, multiples):
    return sum({i*j for i in multiples if i!=0 for j in range(1,math.floor((limit-1)/i)+1)})
