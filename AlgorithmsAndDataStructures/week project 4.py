def threeSumClosest(a, b):
    min_delta = 9999999
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if b - a[i] - a[j] - a[k] == 0:
                    return b
                summ = a[i] + a[j] + a[k]
                if max(summ,b) - min(summ,b) < min_delta:
                    min_delta = max(summ,b) - min(summ,b)
                    min_sum = summ
    return min_sum


print(threeSumClosest([-10,-10,-10],-5))