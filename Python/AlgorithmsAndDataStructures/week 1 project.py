def if_prime(n):
    if n == 1:
        return False
    for i in range (2,int(n**0.5+1)):
        if n%i ==0:
            return False
    return True
# O(n) = sqrt(n)
def intAsPrimeSum(n):
    for i in range (n,2,-1):
        if if_prime(i) and if_prime(n-i):
            return [n-i,i]
#O(n) = n
import time
t1 = time.time()
print(intAsPrimeSum(12400000000000000000))
print(time.time()-t1)
#O(n) = sqrt(n) + n