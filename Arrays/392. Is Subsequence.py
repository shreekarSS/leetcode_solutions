class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = right = 0
        first_bound, second_bound = len(s), len(t)
        while left < first_bound and right < second_bound:
            if s[left] == t[right]:
                left += 1
            right += 1
        return left == first_bound
