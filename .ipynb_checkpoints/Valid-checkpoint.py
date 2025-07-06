"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
}"""

class Solution(object):
    def isValid(self, s):
        close_open = { ")" : "(",
         "]" : "[",
         "}" : "{" }
        stack = []
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

