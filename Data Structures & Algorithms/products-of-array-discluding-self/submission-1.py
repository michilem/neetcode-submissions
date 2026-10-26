class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [1], [1]
        l, r = 1, len(nums)-2
        while l < len(nums):
            pre.append(nums[l-1] * pre[l-1])
            post.append(nums[-(l)] * post[l-1])
            l += 1
            r -= 1
        i = 0
        out = list()
        while i < len(pre):
            out.append(pre[i] * post[-(i+1)])
            i += 1
        return out
