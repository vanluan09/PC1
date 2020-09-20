import math
import numpy as np
def nCk(N, k) : 
    return np.prod( [(N-k+i)/i for i in range(1, k+1)] )
    
def prob(k, p, r) : 
    '''p(k)'''
    return nCk(k, k-r+1) * (p**r) * ((1-p)**(k-r))

def sumProb(N, p, r) : 
    ''' sumProb function: tổng xác suất của tất cả các ký hiệu từ 1 đến N '''
    return sum( prob(k, p, r) for k in range(1,N+1) )

def infoMeasure(k, p, r) :
    ''' infoMeasure function: lượng thông tin mà ký hiệu k mang '''
    return -math.log2( prob(k, p, r) )

def approxEntropy(N, p, r) : 
    return sum( prob(k, p, r) * infoMeasure(k, p, r) for k in range(1,N+1) )

