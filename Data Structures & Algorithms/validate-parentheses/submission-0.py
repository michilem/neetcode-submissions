class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack = list()
        for c in s:
            if c in bracket_map:
                if stack:
                    if stack.pop() != bracket_map[c]:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False