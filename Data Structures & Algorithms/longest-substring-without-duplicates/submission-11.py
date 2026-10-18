class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_l = 0
        s_set = set()
        while r < len(s):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(s[r])
            max_l = max(max_l, r - l + 1)
            r += 1
        return max_l