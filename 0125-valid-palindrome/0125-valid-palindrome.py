class Solution:
    def isPalindrome(self, s: str) -> bool:
        num = []
        for ch in s:
            if ch.isalnum():             # returns true when char is int or letter
                num.append(ch.lower())
        return num == num[::-1]