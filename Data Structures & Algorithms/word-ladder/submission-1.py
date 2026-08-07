class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        m = len(beginWord)
        vis = set()
        child = {}

        for word in wordList:
            for i in range(m):
                pattern = word[:i] + '*' + word[i + 1:]
                if pattern in child:
                    child[pattern].append(word)
                else:
                    child[pattern] = [word]

        q = deque()
        q.append((beginWord, 1))

        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            
            for i in range(m):
                pattern = word[:i] + '*' + word[i + 1:]
                if pattern in child:
                    for c in child[pattern]:
                        if c not in vis:
                            q.append((c, step + 1))
                            vis.add(c)
        return 0