#Given an array of integers nums and an integer target, 
#return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution,
#and you may not use the same element twice.
def twoSum(self, nums, target):
        result = []
        i = 0
        while i != len(nums):
            j = len(nums) - 1
            while j > i:
                if (nums[i] + nums[j]) == target:
                    result.append(i)
                    result.append(j)
                j -= 1
            i += 1
        
        return result
