class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not(1 <= len(nums) <= 10):
            return "ERROR, Invalid list"
        
        result = [[]]
        for num in nums:
            new_subsets = []
            for curr in result:
                new_set = curr + [num]
                new_subsets.append(new_set)
            result += new_subsets
        return result
nums = [1, 2, 3]
final = Solution()
print(final.subsets(nums))