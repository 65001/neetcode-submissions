class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in dictionary:
                return [dictionary[complement], index]
            else:
                dictionary[number] = index

