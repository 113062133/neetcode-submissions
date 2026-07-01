class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif (stack[-1] == '(' and c == ')') or (stack[-1] == '[' and c == ']') or (stack[-1] == '{' and c == '}'):
                stack.pop()
            else:
                stack.append(c)
        return not stack