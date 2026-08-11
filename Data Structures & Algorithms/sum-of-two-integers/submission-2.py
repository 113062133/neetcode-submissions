class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0

        for i in range(32):
            bit1 = (a >> i) & 1
            bit2 = (b >> i) & 1

            res_bit = bit1 ^ bit2 ^ carry
            res = res | (res_bit << i)
            carry = (bit1 & bit2) | (bit2 & carry) | (bit1 & carry)
        
        if res > (1 << 31) - 1:
            res = ~(res ^ ((1 << 32) - 1))
        return res