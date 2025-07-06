class Solution(object):
    def isValid(self, s):
        close_open = { ")":"(", 
                      "]" : "[", 
                      "}": "{"}
        stack = [] #for storing opening brackets
        for char in s:
            if char in close_open:
                if not stack:
                    return False
                top = stack.pop()
                if close_open[char] != top:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        else:
            return True

string = Solution()
Result = string.isValid("([{}])")
print(Result)
                