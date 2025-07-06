"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""
"""Example 1:

Input: nums = [1,2,3,1]

Output: true
"""

class Solution(object):
    def containsDuplicate(self, nums):
        Duplicated = []
        Count = []
        for i in range(0, len(nums)):
            for j in range(0 , len(nums)):
                if i != j and nums[i] == nums[j]:
                    if nums[i] not in Duplicated:
                        Duplicated.append(nums[i])
                        count = nums.count(nums[j])
                        Count.append(count)

        return Duplicated  # You can return Count too if needed

nums = [1, 2, 3, 1]   
result = Solution()
Final = result.containsDuplicate(nums)
print(Final)
     
                


