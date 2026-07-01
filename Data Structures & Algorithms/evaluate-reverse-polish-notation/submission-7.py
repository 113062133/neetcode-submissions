class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                
                if t == '+':
                    res = op1 + op2
                elif t == '-':
                    res = op1 - op2
                elif t == '*':
                    res = op1 * op2
                else:
                    res = (int)(op1 / op2)
                stack.append(res)
        return stack[0]