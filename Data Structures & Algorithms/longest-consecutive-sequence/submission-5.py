class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bestLength = 0
        currentLength = 0
        previousValue = None
        nums.sort()
        for currentValue in nums:
            if previousValue == None or currentValue == previousValue + 1:
                currentLength += 1
            elif currentValue == previousValue:
                continue
            elif currentValue != previousValue + 1:
                currentLength = 1
            if currentLength > bestLength:
                bestLength = currentLength
            previousValue = currentValue
        return bestLength