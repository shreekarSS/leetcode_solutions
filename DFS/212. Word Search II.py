# create Trie tree strc
from typing import List


class  TrieNode():
    def __int__(self):
        self.children = {}
        self.isWord = False

    def addword(self, word):
        cur = self

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()

            cur = cur.children[w]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result, visit = set(), set()
        row,col = len(board), len(board[0])

        root = TrieNode()

        for word in words:
            root.addword(word)

        def dfs(r,c, root,word):
            if r in range(row) and c in range(col) and ((r,c)) not in visit and board[r][c] in root.children:
                visit.add(r,c)
                root = root.children[ board[r][c]]
                word+= board[r][c]
                if root.isWord:
                    result.add(word)

                dfs(r-1,c,root,word)
                dfs(r+1,c,root,word)
                dfs(r,c-1,root,word)
                dfs(r,c+1,root,word)

                visit.remove((r,c))



        for r in range(row):
            for c in range(col):
                dfs(r,c,root,"")
        return list(result)