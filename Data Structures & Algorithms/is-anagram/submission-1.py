class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1 = collections.Counter(s)
        dict2 = collections.Counter(t)
        for a,b in zip(s,t):
            dict1[a] = dict1.get(a, 0) + 1
            dict2[b] = dict2.get(b, 0) + 1
        
        return dict1 == dict2