class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = ''
        for c in s:
            if c.isalnum():
                result += c
        return result == result[::-1]