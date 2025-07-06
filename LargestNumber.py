"""Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"""

from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        conv_To_string = list(map(str,nums))

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        
                
        nums = sorted(conv_To_string, key=cmp_to_key(compare))
        return str(int("".join(nums)))
        


nums = [3,30,34,5,9]
Result = Solution()
Final = Result.largestNumber(nums)

print(Final)

nums = [3,30,34,5,9]
Result = Solution()
Final = Result.largestNumber(nums)

print(Final)