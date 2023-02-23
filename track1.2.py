ls=[-2,1,-3,4,-1,2,1,-5,4]
def maxSubarray(nums):
    max=sum(nums)
    for i in range(len(nums)):
            for j in range(len(nums)):
                if sum(nums[i:j])>max:
                    print(nums[i:j])
    return max
print(maxSubarray(ls))
