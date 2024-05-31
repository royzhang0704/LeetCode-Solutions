class Solution:
    def isValid(self, s: str) -> bool:
        match={')':'(',']':'[','}':'{'}
        stack=[]
        for c in s:
            if c not in match:
                stack.append(c)
                continue
            if not stack or stack[-1] != match[c]:
                return False 
            stack.pop()
        return not stack
