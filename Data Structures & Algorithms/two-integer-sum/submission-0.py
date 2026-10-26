class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {target - nums[0]: 0}
        for i in range(1, len(nums)):
            if nums[i] in diffs:
                return [diffs[nums[i]], i]
            diff = target - nums[i]
            
            diffs[diff] = i