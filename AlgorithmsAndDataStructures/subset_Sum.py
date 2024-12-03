def getCombinationsUtil(a, sum, currIndex, result, curr):
    if sum == 0:
        result.append(list(curr))
        return
    elif sum &lt; 0 or currIndex == len(a):
        return
    else:
        curr.append(a[currIndex])
        getCombinationsUtil(a, sum - a[currIndex], currIndex, result, curr)
        curr.pop()
        getCombinationsUtil(a, sum, currIndex + 1, result, curr)


def getCombinations(a, sum):
    result = []
    curr = []
    index = 0
    getCombinationsUtil(a, sum, index, result, curr)
    return result