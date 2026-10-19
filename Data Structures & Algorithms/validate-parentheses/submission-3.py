class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        s_dict = {'}':'{', ')':'(', ']':'['}

        for c in s:
            if c in s_dict:
                if  res and s_dict[c] == res[-1]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)
        return True if not res else False