class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "".join(s.lower())
        
        lp = 0
        rp = len(s)-1
        while lp < rp:
            if not s[lp].lower().isalnum():
                lp += 1
                continue
            if not s[rp].lower().isalnum():
                rp -= 1
                continue
            if s[lp].lower() == s[rp].lower():
                lp += 1
                rp -= 1
            else:
                return False
        return True
