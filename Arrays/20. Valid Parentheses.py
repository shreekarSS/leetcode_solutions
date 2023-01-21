class Solution:
    def isValid(self, s: str) -> bool:
         # case ()

        stack = []

        closeToOpen = {')':'(', ']':'[','}':'{'}

        for b in stack:
            if b not in closeToOpen:
                 stack.append(b)
            else:
                if stack and stack[-1] == closeToOpen.get(b):
                    stack.pop()
                else:
                    return False


        return True if not stack else False