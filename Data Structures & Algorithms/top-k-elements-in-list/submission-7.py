class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        for n in nums:
            if n in f:
                f[n] += 1
            else:
                f[n] = 1
        f_buckets = [[] for _  in range(len(nums) + 1)]
        for key, v in f.items():
            f_buckets[v].append(key)

        out = []
        for i in range(len(f_buckets) - 1, 0, -1):
            for num in f_buckets[i]:
                out.append(num)
                if len(out) == k: return out
        