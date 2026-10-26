class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            i = 0
            
            if num-1 in nums_set:
                continue
            
            while num+i in nums_set:
                i += 1
            longest = max(longest, i)
        return longest
