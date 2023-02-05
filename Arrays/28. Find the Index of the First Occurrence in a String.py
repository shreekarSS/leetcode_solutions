class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay = len(haystack)
        need = len(needle)

        for i in range(len(hay)):
            if haystack[i:i+need] == needle:
                return i

        return -1