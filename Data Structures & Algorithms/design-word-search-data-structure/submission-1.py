class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def bfs(idx, root):
            for i in range(idx, len(word)):
                c = word[i]
                if c == '.':
                    for child in root.children.values():
                        if bfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in root.children:
                        return False
                    root = root.children[c]
            return root.word
        return bfs(0, self.root)
