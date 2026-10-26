class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for s in strs:
            freq_arr = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                freq_arr[idx] += 1
            freq_key = tuple(freq_arr)
            if freq_key in out:
                out[freq_key].append(s)
            else:
                out[freq_key] = [s]
        return list(out.values())
        