class Solution:
    def checkValidString(self, s: str) -> bool:
        l, r = 0, 0
        for c in s:
            if c == "(":
                l += 1
                r += 1
            elif c == ")":
                l -= 1
                r -= 1
            elif c == "*":
                l -= 1
                r += 1
            if l < 0:
                l = 0
            if r < 0:
                return False
        
        return l == 0