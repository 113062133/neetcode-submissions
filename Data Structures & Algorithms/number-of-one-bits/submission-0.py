class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for i in range(32):
            mask = 1 << i
            if mask & n > 0:
                cnt += 1
        return cnt