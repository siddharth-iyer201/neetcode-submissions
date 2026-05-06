import collections

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        bestLength = 0
        for num in numSet:
            if (num - 1) not in numSet:
                currentLength = 1
                while num + currentLength in numSet:
                    currentLength += 1
                bestLength = max(currentLength, bestLength)
        return bestLength