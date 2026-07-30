class TrieNode:
    def __init__(self):
        self.c = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        n = len(word)
        cur = self.root
        for i in range(n):
            if word[i] not in cur.c:
                cur.c[word[i]] = TrieNode()
            if i == n - 1:
                    cur.c[word[i]].is_end = True
            cur = cur.c[word[i]]

    def search(self, word: str) -> bool:
        n = len(word)
        cur = self.root
        for i in range(n):
            if word[i] not in cur.c:
                return False
            if i == n - 1 and cur.c[word[i]].is_end == False:
                return False
            cur = cur.c[word[i]]
        return True

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        cur = self.root
        for i in range(n):
            if prefix[i] not in cur.c:
                return False
            cur = cur.c[prefix[i]]
        return True
        