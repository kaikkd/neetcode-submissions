class TreeNode:
    
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for s in word:
            if s not in cur.children:
                cur.children[s] = TreeNode()
            cur = cur.children[s]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for s in word:
            if s not in cur.children:
                return False
            cur = cur.children[s]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for s in prefix:
            if s not in cur.children:
                return False
            cur = cur.children[s]
        return True
        