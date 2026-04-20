class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for c in s:
            if c.isalnum():
                result += c.lower()
        s = result
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]: return False
            i+=1
            j-=1
        
        return True
        