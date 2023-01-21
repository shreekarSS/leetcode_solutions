class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        # store char and its count
        # if count  == k : pop the stack ele increment the counter for the char

        for char in stack:
            if stack and stack[-1][0] == char:
                stack[-1][1]+=1

            else:
                stack.append([char,1])

            if stack[-1][1] == k:
                stack.pop()

        res = ""
        for char, count in stack:
            res += char*count

        return res