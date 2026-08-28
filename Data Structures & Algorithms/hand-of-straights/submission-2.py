class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = {}
        for val in hand:
            if val in freq:
                freq[val] += 1
            else:
                freq[val] = 1
        
        hand.sort()

        n = len(hand)
        if n % groupSize != 0:
            return False
        num = n // groupSize

        while num > 0:
            x = min(freq.keys())
            for val in range(x, x + groupSize):
                if val not in freq or freq[val] == 0:
                    return False
                else:
                    freq[val] -= 1
                    if freq[val] == 0:
                        del freq[val]
            num -= 1
        return True
