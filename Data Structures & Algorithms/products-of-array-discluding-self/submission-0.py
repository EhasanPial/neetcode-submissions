class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        mul = 1
        suffix_mul = 1
        n = len(nums)
        for i, val in enumerate(nums):
            prefix[i] = mul
            mul *= val
            suffix[n-i-1] = suffix_mul
            suffix_mul *= nums[n-i-1]

        for i, val in enumerate(nums):
            if i == 0:
                nums[i] = suffix[i]
            elif i == n-1:
                nums[i] = prefix[i]
            else:
                nums[i] = prefix[i] * suffix[i]

        return nums