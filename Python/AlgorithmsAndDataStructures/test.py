def subset(array: list, k):
    array.sort()
    indexmax = 0
    for i in range(len(array), -1):
        if k - array[i] < 0:
            break
        if k - array[i] == 0:
            return True
        else:
            indexmax = i
    array = array[:indexmax]
