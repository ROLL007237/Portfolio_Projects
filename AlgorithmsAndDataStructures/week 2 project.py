def summ(nums, k):
    cnt = 0
    num_count = {}
    for i in nums:
        if i + k in num_count:
            cnt+=num_count[i+k]
        if i-k in num_count:
            cnt+=num_count[i-k]
        if i not in num_count:
            num_count[i] = 0
        num_count[i] += 1
    return cnt
