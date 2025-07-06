"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true"""


class Solution(object):
    def isAnagram(self, s, t):
        updated_s = ""
        updated_t = ""
        for char1 in s:
            if char1.isalnum():
                updated_s = updated_s + char1.lower()
 
        for char2 in t:
            if char2.isalnum():
                updated_t = updated_t + char2.lower()
   
        # Convert to list after collecting all valid characters
        updated_s = list(updated_s)
        updated_t = list(updated_t)
        updated_s.sort()
        updated_t.sort()
        if updated_s == updated_t and len(updated_s) == len(updated_t):
            return True 
        else:
            return False
            

Final = Solution() 

Final_result = Final.isAnagram("race car", "rac ecar")
print(Final_result)