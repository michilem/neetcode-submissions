class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.lower())
        
        lp = 0
        rp = len(s)-1
        while lp < rp:
            if not s[lp].isalnum():
                lp += 1
                continue
            if not s[rp].isalnum():
                rp -= 1
                continue
            if s[lp] == s[rp]:
                lp += 1
                rp -= 1
            else:
                return False
        return True
