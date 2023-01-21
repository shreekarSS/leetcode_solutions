class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        """
        longest = 0

        left = right = 0

        seen_window = set()

        while right < len(s):
            if s[right] not in seen_window:
                seen_window.add(s[right])
                right+=1

            else:
                seen_window.remove(s[left])
                left+=1

            longest = max(longest, right-left)

        return  longest