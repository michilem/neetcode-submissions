class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        for n in nums:
            f[n] = f.setdefault(n, 0) + 1
        f_sort = sorted(f.items(), key = lambda item: item[1], reverse=True)

        return [key for key, _ in f_sort[:k]]