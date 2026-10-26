class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0
        for num in nums_set:
            curr_len = 0
            
            if num-1 not in nums_set:
                curr_num = num
                curr_l = 1
                while curr_num+1 in nums_set:
                    curr_l += 1
                    curr_num += 1
                if curr_l > longest:
                    longest = curr_l
            else: continue
        return longest