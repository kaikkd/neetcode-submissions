class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_l = 0
        set_s = set()

        while r < len(s):
            while s[r] in set_s:
                set_s.remove(s[l])
                l += 1
            set_s.add(s[r])
            max_l = max(max_l, r-l+1)
            r += 1
        
        return max_l