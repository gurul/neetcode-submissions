class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', '}': '{', ']':'['}
        stack = []
        for char in s:
            if char not in brackets:
                stack.append(char)
            else:
                if not stack or stack.pop() != brackets[char]:
                    return False
        
        return not stack
        