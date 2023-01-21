class Trie:

    def __init__(self):
        self.children = {}
        self.isWord = False

    def insert(self, word: str) -> None:
        curr = self

        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self

        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]

        return True if curr.isWord else False

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for word in prefix:
            if word not in cur.children:
                return False
            cur = cur.children[word]
        return True