import math
def prob(n, p) :
    ''' prob function: xác xuất sau n lần thử
                    p: xác xuất thành công sau 1 lần thử
                    n: số lần thử
    '''
    return p*((1-p)**(n-1))
def sumProb(N, p) :
    ''' sumProb function: tổng xác suất của tất cả các ký hiệu từ 1 đến N
                ví dụ: p = 0.5
                    sumProb(10, 0.5) = 0.9990234375
                    sumProb(50, 0.5) = 0.9999999999999991
        Vậy nếu N -> ∞ thì sumProb(N, 0.5) -> 1
    '''
    return sum(prob(syb, p) for syb in range(1,N+1))

def infoMeasure(n, p) :
    ''' infoMeasure function: lượng thông tin mà ký hiệu x mang theo '''
    return -math.log2(prob(n, p))
def approxEntropy(N,p) :
    ''' approxEntropy function: nguồn thông tin có sẵn của tất cả các ký hiệu từ 1 đến N
                ví dụ: p = 0.5
                    approxEntropy(10,0.5) = 1.98828125
                    approxEntropy(50,0.5) = 1.9999999999999538

            Vậy nếu N -> ∞ thì
            approxEntropy(N, 0.5) -> 2 ~ Entropy of geometric infomation source với p = 0.5
    '''
    return sum(prob(isr, p) * infoMeasure(isr, p) for isr in range(1,N+1))