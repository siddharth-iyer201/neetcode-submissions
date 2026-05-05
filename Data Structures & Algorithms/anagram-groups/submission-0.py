class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for word in strs:
            key = "".join(sorted(word))
            if key in result:
                result[key] += [word]
            else:
                result[key] = [word]
        return list(result.values())