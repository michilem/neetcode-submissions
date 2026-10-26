class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        sep = "#"
        for s in strs:
            out += str(len(s)) + sep + s
        return out

    def decode(self, s: str) -> List[str]:
        sep = '#'
        i = 0
        l_str = ''
        out = []
        while i < len(s):
            if s[i] == sep:
                incr = int(l_str) + 1
                out.append(s[i+1:i + incr])
                i += incr
                l_str=''
            else:
                l_str += s[i]
                i += 1
        return out