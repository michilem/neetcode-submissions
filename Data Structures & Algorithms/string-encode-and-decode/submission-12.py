class Solution:

    def encode(self, strs: List[str]) -> str:
        out  = ""
        sep = '#'
        for s in strs:
            out = out + str(len(s)) + sep + s
        return out

    def decode(self, s: str) -> List[str]:
       sep = '#'
       out = []
       i = 0
       l = ""
       while i < len(s):
           
            if s[i] == sep:
                out.append(s[i+1:i+1+int(l)])
                i = i + 1 + int(l)
                l = ""
            else:
                l = l + s[i]
                i += 1
         
       return out

