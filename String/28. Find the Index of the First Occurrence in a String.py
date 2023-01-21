class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Input: haystack = "sadbutsad", needle = "sad"
        Output: 0
        Explanation: "sad" occurs at index 0 and 6.
        The first occurrence is at index 0, so we return 0.
        """
        hay = len(haystack)
        need = len(needle)

        for i in range(hay):
            if haystack[i:i+need] == needle:
                return i

        return -1
