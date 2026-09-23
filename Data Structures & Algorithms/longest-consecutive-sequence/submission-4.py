class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # Sort the numbers
        nums.sort()
        longestSequence = 0
        currentSequence = 1
        previousNumber = nums[0]
        indexes = range(1, len(nums))
        for i in indexes:
            if previousNumber == nums[i]:
                continue
            if previousNumber + 1 != nums[i]:
                longestSequence = max(longestSequence, currentSequence)
                currentSequence = 1
            else:
                currentSequence = currentSequence + 1
            previousNumber = nums[i]
        return max(longestSequence, currentSequence)


        
        