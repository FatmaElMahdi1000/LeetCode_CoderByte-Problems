class Solution(object):
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def trailingZeroes(self, n):
        fact = self.factorial(n)   # compute factorial
        fact_str = str(fact)       # convert to string
        zero_count = 0
        # count trailing zeros only
        for char in reversed(fact_str):
            if char == '0':
                zero_count += 1
            else:
                break
        return zero_count

# Example
result = Solution()
print(result.trailingZeroes(5))   # Output: 2


                
