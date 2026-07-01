class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        match = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c not in match:
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] != match[c]:
                    return False
                else:
                    stack.pop()
        return not stack