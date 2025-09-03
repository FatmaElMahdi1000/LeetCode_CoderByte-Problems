class Solution(object):
    def fib_seq(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib_seq(n-1) + self.fib_seq(n-2)

result = Solution()
print(result.fib_seq(4))