class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict()
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        result = []
        for key, value in frequency.items():
            result.append((value, key))
        result.sort(reverse = True)
        return [pair[1] for pair in result[:k]]