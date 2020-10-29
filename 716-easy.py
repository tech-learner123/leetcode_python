class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max = - float('inf')

    def push(self, x: int) -> None:
        self.max = max(self.max, x)
        self.stack.append([x, self.max])

    def pop(self) -> int:
        # pop the stack
        last = self.stack.pop()
        if self.max == last[1]:
            # update the maximum value

            self.max = self.stack[-1][1] if self.stack else -float('inf')
        return last[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.max

    def popMax(self) -> int:
        temp = []
        # pop the value ahead to a temp list
        while self.stack[-1][0] != self.max:
            temp.append(self.stack.pop()[0])
        res = self.stack.pop()[0]
        # update the maximum value
        if self.stack:
            self.max = self.stack[-1][1]
        else:
            self.max = -float('inf')
        # push the value back to the list
        for i in reversed(temp):
            self.push(i)
        return res

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()