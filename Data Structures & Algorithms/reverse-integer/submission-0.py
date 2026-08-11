class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        MAX = (1 << 31) - 1
        MIN = -(1 << 31)

        sign = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:
            digit = x % 10
            x //= 10
            if res > MAX / 10 or res < MIN / 10:
                return 0
            if res == MAX / 10 and digit > MAX % 10:
                return 0
            if res == MIN / 10 and digit < MIN / 10:
                return 0
            res = res * 10 + digit

        res *= sign
        return res