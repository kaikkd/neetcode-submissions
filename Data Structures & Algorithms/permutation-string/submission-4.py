class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        
        if not s2 or len(s1) > len(s2):
            return False
        
        count_s1, count_s2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(len(s1), len(s2)):
            if count_s1 == count_s2:
                return True
            
            count_s2[ord(s2[i]) - ord('a')] += 1
            count_s2[ord(s2[i - len(s1)]) - ord('a')] -= 1
        
        return count_s1 == count_s2