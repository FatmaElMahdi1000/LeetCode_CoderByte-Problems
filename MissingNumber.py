"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Input: nums = [3,0,1]
Output: 2"""


class Solution(object):
    def missingNumber(self, nums):
        sorted_nums = sorted(nums)
        sorted_nums_length = len(sorted_nums)
        for i in range(sorted_nums_length - 1):
            if sorted_nums[i + 1] - sorted_nums[i] > 1:
                return sorted_nums[i] + 1
        if sorted_nums[0] != 0:
            return 0
        else:
             return sorted_list_length
            