def merge(A, B):
    arr = []
    l = len(A) + len(B)
    i=0
    j=0
    while len(arr) != l:
        if A[i] < B[j]:
            arr.append(A[i])
            i+=1
        else:
            arr.append(B[j])
            j+=1

    return arr,A,B

print(merge([ -4, 3 ],[ -2, -2 ]))