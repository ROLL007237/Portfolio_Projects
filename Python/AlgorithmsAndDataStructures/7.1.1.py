def binary_search(list,key):
    begin = 0
    end = len(list) - 1
    maxx = int

    while begin <= end:
        mid = (begin+end)//2
        midval = list[mid]

        if midval>list[mid+1] and midval > list[mid-1]:
            maxx = mid

        if midval < list[mid+1]:
            begin = mid+1

        if midval > list[mid+1]:
            end = mid - 1

    list1 = list[:maxx-+1]
    list2 = list[maxx:]

    begin = 0
    end = len(list1)-1

    while begin <= end:
        mid = (begin+end)//2
        midval = list1[mid]

        if midval==key:
            return mid

        if midval < key:
            begin = mid+1

        else:
            end = mid - 1

    begin = 0
    end = len(list2) - 1

    while begin <= end:
        mid = (begin + end) // 2
        midval = list2[mid]

        if midval == key:
            return mid+len(list1)+1

        if midval > key:
            begin = mid + 1

        else:
            end = mid - 1

print(binary_search([0,2,4,5,6,3,1],3))