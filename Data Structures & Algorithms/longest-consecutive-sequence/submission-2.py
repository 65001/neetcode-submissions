class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # Deduplicate the numbers hehe
        nums = list(set(nums))
        # Sort the numbers
        nums.sort()
        print(nums)
        longestSequence = 0
        currentSequence = 1
        previousNumber = nums[0]
        indexes = range(1, len(nums))
        for i in indexes:
            if previousNumber + 1 != nums[i]:
                longestSequence = max(longestSequence, currentSequence)
                currentSequence = 1
            else:
                currentSequence = currentSequence + 1
            previousNumber = nums[i]
        return max(longestSequence, currentSequence)


        
        