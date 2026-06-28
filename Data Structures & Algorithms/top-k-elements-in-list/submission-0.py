from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        for num, freq in cnt.items():
            bucket[freq].append(num)
        
        ans = []
        for freq in range(n, 0, -1):
            if k - len(bucket[freq]) < 0:
                ans.extend(bucket[freq][:k])
                return ans
            else:
                ans.extend(bucket[freq])
                k -= len(bucket[freq])
        return ans