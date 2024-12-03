def maxWidthOfVerticalArea(points):
    xes = [points[x][0] for x in range (len(points))]
    xes.sort()
    m = 0
    for i in range(len(xes) - 1):
        if xes[i + 1] - xes[i] > m:
            m = xes[i + 1] - xes[i]
    return m

print(maxWidthOfVerticalArea([[1,9],[1,8],[3,4],[8,1]]))