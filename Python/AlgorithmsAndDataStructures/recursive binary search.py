def binary_search(array,key,__flag=0):
    array.sort()
    begin = 0
    end = len(array)-1
    mid = (begin+end)//2
    midval=array[mid]

    if midval == key:
        return mid+__flag

    if midval>key:
        return binary_search(array[:mid], key, __flag+mid)
    else:
        return binary_search(array[mid+1:], key, __flag+mid)

print(binary_search([1,2,3,4,5,6,10,20,23,40,43,45,200],23))
