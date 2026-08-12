class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        def dfs(n):
            if n == 0:
                return 1

            temp = dfs(n // 2)
            if n % 2 == 1:
                return  temp * temp * x
            else:
                return temp * temp

        return dfs(n)