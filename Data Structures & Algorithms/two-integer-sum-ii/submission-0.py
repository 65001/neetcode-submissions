class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left , right = 0, len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            elif current > target:
                # We are larger than the target therfore we need to decrement the right pointer
                right = right - 1
            else:
                left = left + 1
        

        