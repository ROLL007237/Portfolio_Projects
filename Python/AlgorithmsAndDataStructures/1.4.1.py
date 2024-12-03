def insert(intervals, new_interval):
    for i in range(len(intervals) - 1):
        if (intervals[i][1] == new_interval[0] or
                (new_interval[0] < intervals[i][1] <= new_interval[1])):

            if intervals[i + 1][0] <= new_interval[1]:

                if new_interval[1] < intervals[i + 1][1]:
                    intervals[i] = [intervals[i][0], intervals[i+1][1]]

                if new_interval[1] >= intervals[i + 1][1]:
                    intervals[i] = [intervals[i][0], new_interval[1]]
                intervals.pop(i + 1)

            return intervals


print(insert([[1, 4], [6, 8], [9, 10]], [6, 9]))
