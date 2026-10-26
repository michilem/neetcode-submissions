class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack = list()
        for c in s:
            if c in bracket_map:
                if not stack or stack.pop() != bracket_map[c]:
                    return False
            else:
                stack.append(c)
        
        return not stack