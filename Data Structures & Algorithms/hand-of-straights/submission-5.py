class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counter = Counter(hand)
        for n in sorted(counter):
            while counter[n]:
                for i in range(n, n + groupSize):
                    if not counter[i]:
                        return False
                    counter[i] -= 1
        
        return True