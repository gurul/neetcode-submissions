class Solution:
    def isValid(self, s: str) -> bool:

      if len(s) < 2: return False

      stack = []
      brackets = {')':'(', '}':'{', ']':'['}

      for i in range(len(s)):
        if stack and s[i] in brackets:
            b = stack.pop()
            if b != brackets[s[i]]: return False
        elif s[i] in brackets and not stack:
            return False
        else:
            stack.append(s[i])
    
      return not stack



