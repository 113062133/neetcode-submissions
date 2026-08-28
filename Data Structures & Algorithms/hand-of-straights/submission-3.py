class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = {}
        for val in hand:
            if val in freq:
                freq[val] += 1
            else:
                freq[val] = 1

        for x in sorted(freq):
            if freq[x] > 0:
                cnt = freq[x]
                for val in range(x, x + groupSize):
                    if val not in freq or freq[val] < cnt:
                        return False
                    else:
                        freq[val] -= cnt
        return True
