class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        revHash = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in revHash:
                return [revHash[diff], i]
            revHash[n] = i
        return 