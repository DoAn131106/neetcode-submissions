class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        prefix[0] = 1
        suffix = [1] * len(nums)
        suffix[len(nums) - 1] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        ret = []
        for j in range(len(nums) - 2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j + 1]
        for k in range(len(nums)):
            ret.append(prefix[k] * suffix[k])
        return ret
        