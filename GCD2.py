class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # base case: if concatenation doesn't match, no gcd
        if str1 + str2 != str2 + str1:
            return ""
        
        # recursive Euclidean-style gcd, but on lengths
        return str1[:self.gcd(len(str1), len(str2))]
    
    def gcd(self, a, b):
        if b == 0: #base case 
            return a
        return self.gcd(b, a % b)


# Tests
s = Solution()
print(s.gcdOfStrings("ABCABC", "ABC"))    # "ABC"
print(s.gcdOfStrings("ABABAB", "ABAB"))   # "AB"
print(s.gcdOfStrings("ABCDEF", "ABC"))    # ""
print(s.gcdOfStrings("TAUXX"*5, "TAUXX"*9))  # "TAUXX"