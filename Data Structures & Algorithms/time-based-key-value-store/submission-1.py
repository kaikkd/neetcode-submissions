class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.store.get(key):
            self.store[key] = []
        self.store[key].append([value, timestamp])
 
    def get(self, key: str, timestamp: int) -> str:
        if not self.store.get(key):
            return ''

        res = ''
        k_s = self.store.get(key)
        l, r = 0, len(k_s) - 1
        while l <= r:
            m = (l + r) // 2
            if k_s[m][-1] <= timestamp:
                res = k_s[m][0]
                l = m + 1
            else:
                r = m - 1

        return res       
