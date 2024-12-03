import time
c = time.time()
def factorial(n):
    out = 1
    for i in range(2,n+1):
        out*=i
    return out


def beautiful_points(n,k):
    f_n = factorial(n)
    f_k = factorial(k)
    return int(abs(f_n/f_k - (n-1)*(f_n/(f_k*factorial(n-k)))))

print(beautiful_points(10,10),time.time()-c)
