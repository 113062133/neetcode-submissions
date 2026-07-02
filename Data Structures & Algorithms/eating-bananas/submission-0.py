import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        m = max(piles)
        left = 1
        right = m
        while (left <= right):
            mid = (left + right) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)

            if time <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left