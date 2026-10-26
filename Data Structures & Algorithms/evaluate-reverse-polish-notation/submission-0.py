class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        stack = list()
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                if t == "+":
                    res = stack.pop() + stack.pop()
                elif t == "-":
                    res = - stack.pop() + stack.pop()
                elif t == "*":
                    res = stack.pop() * stack.pop()
                else:
                    den = stack.pop()
                    res = int(stack.pop() / den)
                stack.append(res)
        return stack.pop()
