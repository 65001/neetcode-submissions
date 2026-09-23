class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasSeen = {}
        for x in nums:
            if hasSeen.get(x) is None:
                hasSeen[x] = True
            else:
                return True
        return False