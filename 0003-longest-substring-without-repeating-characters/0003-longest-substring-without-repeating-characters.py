class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 

        left = right = 0

        seen_window = set()

        n = len(s)

        while right < n:
            if s[right] not in seen_window:
                seen_window.add(s[right])
                right+=1
            else:
                seen_window.remove(s[left])
                left+=1
            
            longest = max(longest, right-left)

        return longest
        