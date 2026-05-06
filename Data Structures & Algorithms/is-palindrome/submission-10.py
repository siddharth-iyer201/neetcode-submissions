class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        for vidya in s:
            if vidya.isalnum():
                result += vidya.lower()
        return result == result[::-1]