from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for j in string:
                count[ord(j) - ord('a')] += 1
            key = tuple(count)
            ans[key].append(string)
        return list(ans.values())
