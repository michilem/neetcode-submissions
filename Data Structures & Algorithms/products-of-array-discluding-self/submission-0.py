class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        out = list()
        zero_idx = list()
        for i, num in enumerate(nums):
            if num:
                product *= num
                out.append(1/num)
            else:
                out.append(1)
                zero_idx.append(i)
            
        if not zero_idx:
            return [int(x * product) for x in out]
        else:
            if len(zero_idx) == 1:
                out = [0] * len(nums)
                out[zero_idx[0]] = product
                return out
            else:
                return [0] * len(nums)