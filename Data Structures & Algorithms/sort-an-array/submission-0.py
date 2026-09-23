class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def partition(left, right):
            mid = (left + right)//2
            pivot = nums[mid]
            swap(mid, right)
            i = left - 1
            for j in range(left, right):
                if nums[j] <= pivot:
                    i = i + 1
                    swap(i, j)
            swap(i + 1, right)
            return i + 1

        def quicksort(left, right):
            if left >= right:
                return
            p = partition(left, right)
            quicksort(left, p - 1)
            quicksort(p + 1, right)

        quicksort(0, len(nums) - 1)
        return nums