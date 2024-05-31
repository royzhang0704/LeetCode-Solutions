class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack)==1:
            self.min_stack.append(val)

        else:
            self.min_stack.append(min(self.min_stack[-1],val))

    def pop(self) -> None:
        if len(self.stack)!=0:
            self.stack.pop(-1)
            self.min_stack.pop(-1)
        else:
            return 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
