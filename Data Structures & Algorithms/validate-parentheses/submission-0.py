class Solution:
    """
    (){}
    """
    
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False
        
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        
        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack or brackets[stack[-1]] != char:
                    return False
                stack.pop()
        
        return len(stack) == 0


