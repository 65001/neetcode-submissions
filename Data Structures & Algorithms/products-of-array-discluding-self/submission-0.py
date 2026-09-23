class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [0] * len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for index in range(1, len(nums)):
            prefix[index] = nums[index - 1] * prefix[index - 1]
        for index in range(len(nums) - 2, -1, -1):
            suffix[index] = nums[index + 1] * suffix[index + 1]

        for i in range(len(nums)):
            results[i] = prefix[i] * suffix[i]
        
        return results
        