class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(nums):
            addPair = target - num

            if addPair in seen:
                return [seen[addPair], i]
            seen[num] = i