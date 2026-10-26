class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        d = {}
        for s in strs:
            f = [0] * 26
            for c in s:
                f[ord(c)-ord('a')] += 1
            if tuple(f) in d:
                d[tuple(f)].append(s)
            else:
                d[tuple(f)] = [s]

        
        return list(d.values())