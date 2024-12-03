def numberGame(nums):
    nums = sorted(nums)
    output = []
    while bool(nums) == True:
        a,b = nums.pop(0),nums.pop(0)
        output.append(b)
        output.append(a)
    return output

print(numberGame([124,214,3,5346,34,64,36,23,66,32,1,0]))