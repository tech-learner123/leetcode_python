from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pushqueue = deque([])
        self.popqueue = deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.pushqueue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        idx = 0
        while idx != len(self.pushqueue) - 1:
            self.popqueue.append(self.pushqueue.popleft())
        value = self.pushqueue.popleft()
        self.pushqueue = self.popqueue
        self.popqueue = deque([])
        return value

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.pushqueue:
            return self.pushqueue[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.pushqueue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()