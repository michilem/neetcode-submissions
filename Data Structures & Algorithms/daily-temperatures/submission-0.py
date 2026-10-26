class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decreas = list()
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while decreas and t > decreas[-1][0]:
                j = decreas.pop()[1]
                res[j] = i - j
            decreas.append((t, i))

        return res
