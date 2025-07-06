"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for index, word in enumerate(strs): #word = nat
            sorted_word = ''.join.sorted(word) #sorted = ant
            if result[sorted_word] not in result:
                result[sorted_word] = [word]  #result[ant] = nat
            else:
                result[sorted_word].append(word)
        return result.values()
        
        
print("---Notes ----")
"""🔍 Example Step-by-Step
Let’s say we're looping through strs = ["eat", "tea", "tan", "ate"].

First Word: "eat"
Sorted → "aet"

Not in dictionary → create:
{"aet": ["eat"]}

Second Word: "tea"
Sorted → "aet"

Already in dictionary!

else: → we do:
result["aet"].append("tea") → Now:
{"aet": ["eat", "tea"]}🔍 Example Step-by-Step
Let’s say we're looping through strs = ["eat", "tea", "tan", "ate"].

First Word: "eat"
Sorted → "aet"

Not in dictionary → create:
{"aet": ["eat"]}

Second Word: "tea"
Sorted → "aet"

Already in dictionary!

else: → we do:
result["aet"].append("tea") → Now:
{"aet": ["eat", "tea"]}"""