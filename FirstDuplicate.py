"""Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and using only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2"""

class Solution(object):
    def findDuplicate(self, nums):
        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                if nums[i] == nums[j]:
                    return nums[i]

# Input
nums = [1, 3, 4, 2, 2]

# Create Solution object and call the method
result = Solution()
repeated_num = result.findDuplicate(nums)
print(repeated_num) 