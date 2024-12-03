def remove_dupes(arr):
    k = max(arr)
    counts = {}
    out = arr.copy()
    for i in range(1, k+1): # does not count
        counts[i] = 0

    for i, v in enumerate(arr): #O(n) M(3n)       M = n(out) + 2n(counts)
        if counts[v] == 0:
            counts[v] = 1
        else:
            out.remove(v)
        print(i,v,arr,out)
    return out

def quad_root(n):
    for i in range (n//8+1):
        if i*i*i*i == n:
            return i
    return n**0.25
