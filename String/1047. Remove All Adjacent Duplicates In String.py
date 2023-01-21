class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Input: s = "abbaca"
        Output: "ca"
        Explanation:
        For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal,
        and this is the only possible move.
        The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
        """

        st = []
        for char in s:
            if st and st[-1] == char:
                st.pop()
            else:
                st.append(char)

        return "".join(st)