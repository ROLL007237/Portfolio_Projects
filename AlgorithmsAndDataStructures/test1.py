def isSubsetSum(arr, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if arr[n-1] > sum:
        return isSubsetSum(arr, n-1, sum)
    return isSubsetSum(arr, n-1, sum) or isSubsetSum(arr, n-1, sum-arr[n-1])


def delta(arr):

    s = sum(arr)
    if isSubsetSum(arr, len(arr), s//2) and s%2 == 0:
        return 0
    if isSubsetSum(arr, len(arr), s//2) and s%2 == 1:
        return 1

    out = []

    min_delta = 9999
    for i in range(s):
        if isSubsetSum(arr,len(arr),i):
            out.append(i)

    for i in out:
        if abs(s//2-i)<min_delta:
            min_delta=abs(s//2-i)

    if s%2 == 0:
        return min_delta
    if s%2 == 1:
        return min_delta+1
