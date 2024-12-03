def find_less(arr:list, n:int):
    arr.sort()
    begin = 0
    end = len(arr)-1
    while begin <= end:
        mid = (begin+end)//2
        midval = arr[mid]

        if midval==n:
            i = mid
            while arr[i] == midval:
                i+=1
            else:
                return i

        if midval < n:
            begin = mid+1

        else:
            end = mid - 1


print(find_less([0,1,1,1,2,2,2,2,2,2,2,2,3,4,5,6,7,8,7,7,7,7,7,7],2))