class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for c in s:
            if c.isalnum():
                res.append(c.lower())
        res = ''.join(res)
        return res == res[::-1]