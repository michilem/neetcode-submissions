class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_s = sorted(nums)
        i = 0
        out = []
        while i < len(nums)-2:
            l, r = i+1, len(nums)-1
            target = -nums_s[i]
            while l < r:
                lv, rv = nums_s[l], nums_s[r]
                if (lv + rv) < target:
                    l += 1
                elif (lv + rv) > target:
                    r -= 1
                else:
                    out.append([-target, lv, rv])
                    l += 1
                    r -= 1
                    while l < r and nums_s[l] == lv:
                        l += 1
                    while r > l and nums_s[r] == rv:
                        r -= 1
            i += 1
            while i < len(nums)-2 and nums_s[i] == -target:
                i += 1
        return out