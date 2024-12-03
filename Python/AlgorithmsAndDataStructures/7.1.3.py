def in_matrix(mtrx, key):

    begin = 0
    end = len(mtrx) - 1

    while end >= begin:
        mid = (begin + end) // 2
        print(mtrx[mid])

        if mtrx[mid][0] <= key <= mtrx[mid][-1]:

            if mtrx[mid][0] or mtrx[mid][-1] == key:
                return 1

            row = mtrx[mid]
            beg1 = 0
            end1 = len(row) - 1

            while beg1 <= end1:
                mid1 = (beg1 + end1) // 2
                midval = row[mid1]
                if midval == key:
                    return 1
                if midval < key:
                    beg1 = mid1 + 1
                if midval > key:
                    end1 = mid1 - 1

        if mtrx[mid][0]>key:
            end = mid-1
        if mtrx[mid][-1]<key:
            begin = mid+1

    return 0

print(in_matrix([[1, 1, 2, 2,3], [3, 4, 4, 5,3], [7, 10, 12, 14], [15, 20, 40, 42]], 43765636546353764))
