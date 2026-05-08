class MinStack:

    def __init__(self):
        self.stack = []
        self.minNum = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minNum or val <= self.minNum[-1]:
            self.minNum.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minNum[-1]:
            self.minNum.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minNum[-1]
