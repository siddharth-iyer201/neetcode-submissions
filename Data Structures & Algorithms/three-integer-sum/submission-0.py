class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums)):
            a = nums[i]
            seen = set()
            for j in range(i + 1, len(nums)):
                b = nums[j]
                c = -(a + b)
                if c in seen:
                    triplet = tuple(sorted([a, b, c]))
                    result.add(triplet)
                seen.add(b)
        result = list(result)
        return [list(elem) for elem in result]