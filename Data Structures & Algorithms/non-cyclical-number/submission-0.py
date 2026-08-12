class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set()

        def helper(n):
            res = 0
            while n > 0:
                digit = n % 10
                n //= 10
                res += digit ** 2

            n = res
            if n == 1:
                return True

            if n in vis:
                return False
            vis.add(n)
            return helper(n)

        return helper(n)