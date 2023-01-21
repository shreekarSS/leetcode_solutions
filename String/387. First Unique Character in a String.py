class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}

        for char in s:
            if char not in seen:
                seen[char] = 1

            else:
                seen[char]+=1

        for char, count in seen.items():
            if count == 1:
                return s.index(char)

        return -1
    