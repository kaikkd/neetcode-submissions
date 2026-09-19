class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.key_store.get(key):
            self.key_store[key] = []
        self.key_store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.key_store.get(key):
            return ''
        
        res = ''
        l, r = 0, len(self.key_store.get(key)) - 1
        stores = self.key_store.get(key)
        while l <= r:
            m = (l + r) // 2
            if stores[m][-1] <= timestamp:
                res = stores[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
