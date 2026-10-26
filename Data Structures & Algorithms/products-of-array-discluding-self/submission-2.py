class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [1] * len(nums), [1] * len(nums)
        for i in range(len(nums)):
            if i == 0: continue
            else:
                pre[i] = pre[i-1] * nums[i-1]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1: continue
            else:
                post[i] = post[i+1] * nums[i+1]

        return [x * y for x, y in zip(pre, post)]

            

