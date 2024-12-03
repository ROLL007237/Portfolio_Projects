import numpy as np


def n1():
    return(np.array([0]*10))

def n2():
    return(np.array([5]*10))

def n3():
    return np.arange(10,51)

def n4():
    return np.arange(10,51,2)

def n5():
    return np.arange(0,9).reshape(3,3)

def n6():
    return np.eye(3,dtype='i')

def n7():
    return np.random.randint(0,2)

def n8():
    return np.random.standard_normal(25)

def n9():
    return np.linspace(0,1)

def n10(arr):
    return arr.reshape(3,2)

def n11(m1,m2):
    m1 = m1.reshape(5,3)
    m2 = m2.reshape(3,2)
    return np.matmul(m1,m2)

def n12(arr=np.arange(1,11)):
    pass