class Solution:
    def isPalindrome(self, s: str) -> bool: 
        alphanum = ""
        for i in s:
            if i.isalnum():
                alphanum += i
        s = alphanum
        s = s.lower()
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True
        