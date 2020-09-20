import math
import numpy as np
def nCk(n, k) : 
    return np.prod( [(N-k+i)/i for i in range(1, k+1)] )

def prob(k, p, N) : 
    '''p(k)'''
    return nCk(N, k)*(p**k)*((1-p)**(N-k))

def sumProb(N, p) : 
    ''' sumProb function: tổng xác suất của tất cả các ký hiệu từ 1 đến N '''
    return sum( prob(k, p, N) for k in range(1,N+1) )

def infoMeasure(k, p, N) :
    ''' infoMeasure function: lượng thông tin mà ký hiệu k mang '''
    return -math.log2( prob(k, p, N) )

def approxEntropy(N,p) : 
    return sum( prob(k, p, N) * infoMeasure(k, p, N) for k in range(1,N+1) )


