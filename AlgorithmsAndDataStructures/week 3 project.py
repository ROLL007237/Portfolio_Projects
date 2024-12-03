def check(A):
    ones = []
    zeroes = []
    cnt = 0
    for i in range(len(A)):
        if A[i] == 1:
            cnt+=1
        else:
            if cnt != 0:
                ones.append((cnt,i-1))
            cnt = 0
    for i in range(len(ones)-1):
        zeroes.append((ones[i][1]+1, ones[i+1][1]-ones[i+1][0]))
    return ones,zeroes

variants =[]

def shit(A,B):
    ones,zeroes = map(list, check(A))
    for i in zeroes:
        if i[0]+i[1]+1 <= B:

print(check((0,0,1,1,1,0,1,1,0,0,1,1,0,0)))