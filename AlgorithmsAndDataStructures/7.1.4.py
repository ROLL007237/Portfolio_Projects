def find_range(arr,key):
    begin = 0
    end = len(arr)-1
    while end >= begin:
        mid = (begin+end)//2
        midval = arr[mid]
        if midval == key:
            return mid
        if midval<key:
            begin = mid+1
        else:
            end = mid-1
    return [-1,-1]



print(find_range([1,2,3,4,5,6,6,6,7,8,9,9,9,9,9,101,300],9))