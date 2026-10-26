class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        idx = (l) // 2
        if nums[0] > target or nums[l-1] < target:
            return -1
        if nums[idx] == target:
            return idx
        elif nums[idx] < target:
            i = self.search(nums[idx:], target)
            return i if i == -1 else i + idx
        elif nums[idx] > target:
            return self.search(nums[:idx], target)