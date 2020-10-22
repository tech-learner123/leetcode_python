class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = float(inf)

    def push(self, x: int) -> None:
        self.minimum = min(self.minimum, x)
        self.stack.append([x, self.minimum])

    def pop(self) -> None:
        # Corner case: remember to update the minimum value.
        self.stack.pop()
        if self.stack:
            self.minimum = self.stack[-1][1]
        else:
            self.minimum = float(inf)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()