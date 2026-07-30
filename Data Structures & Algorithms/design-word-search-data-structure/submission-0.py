class TrieNode():
    def __init__(self):
        self.c = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
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
            if word[i] != '.':
                if word[i] not in cur.c:
                    return False
                if i == n - 1 and cur.c[word[i]].is_end == False:
                    return False
                cur = cur.c[word[i]]
            else:
                for ch in cur.c:
                    w = word[:i] + ch + word[i + 1:]
                    if self.search(w):
                        return True
                return False
        return  True