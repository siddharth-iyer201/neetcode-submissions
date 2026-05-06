class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            addPair = target - num
            if addPair in numbers:
                return [i + 1, numbers.index(addPair) + 1]