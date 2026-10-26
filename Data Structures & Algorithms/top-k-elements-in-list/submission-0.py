class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = freq.setdefault(num, 0) + 1
        sorted_elements = sorted(freq.items(), key= lambda item: item[1], reverse=True)


        return [key for key, _ in sorted_elements[:k]]