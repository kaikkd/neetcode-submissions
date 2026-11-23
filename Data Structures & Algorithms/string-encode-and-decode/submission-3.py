class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''

        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append(",")
        res.append("#")

        res.extend(strs)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res, size, i = [], [], 0

        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            size.append(int(s[i : j]))
            i = j + 1
        
        i += 1
        for s_size in size:
            res.append(s[i : i+s_size])
            i += s_size
        
        return res