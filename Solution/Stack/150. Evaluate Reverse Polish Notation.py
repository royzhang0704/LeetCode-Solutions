from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = ["+", "-", "*", "/"]
        
        for i in tokens:
            if i not in operand:
                stack.append(int(i))
            else:
                y = stack.pop()
                x = stack.pop()
                
                if i == "+":
                    stack.append(x + y)
                elif i == "-":
                    stack.append(x - y)
                elif i == "*":
                    stack.append(x * y)
                else:
                    stack.append(int(x / y))
        
        return stack[0]
