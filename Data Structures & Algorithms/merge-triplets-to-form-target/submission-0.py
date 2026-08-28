class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        flag = [False] * 3

        for t in triplets:
            invalid = False
            for i in range(3):
                if t[i] > target[i]:
                    invalid = True
            if invalid:
                continue

            for i in range(3):
                if t[i] == target[i]:
                    flag[i] = True
            
            if flag == [True] * 3:
                return True
        return False