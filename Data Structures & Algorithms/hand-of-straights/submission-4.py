class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        for n in sorted(count):
            while count[n] > 0:
                for i in range(n, n + groupSize):
                    if count[i] == 0:
                        return False
                    count[i] -= 1
        
        return True