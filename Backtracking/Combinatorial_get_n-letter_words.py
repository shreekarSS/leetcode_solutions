from typing import List

def letter_combination(n: int) -> List[str]:

    def dfs(index,path):
        if index == n:
            res.append(''.join(path))
            return 

        for letter in ['a','b']:
            path.append(letter)
            dfs(index+1, path)
            path.pop()
    res = []

    dfs(0, [])

    return res