class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        minNum = self.getMin()
        if minNum is None or val < minNum:
            minNum = val
        self.stack.append((val, minNum))

    def pop(self) -> None:
        self.stack.pop() if self.stack else None
        
    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][-1] if self.stack else None
