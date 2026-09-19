class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 1

        l, r = 0, 1
        while r <= len(s) - 1:
            if s[r] not in s[l : r]:
                r += 1
                res = max(res, len(s[l : r]))
            else:
                l += 1
        
        return res