class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ans = defaultdict(list)
        for i, string in enumerate(strs):
            count = [0] * 26
            for j in string:
                count[ord(j) - ord('a')] += 1
            key = tuple(count)
            ans[key].append(string)
        return list(ans.values())
