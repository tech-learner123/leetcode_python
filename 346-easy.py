from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.list = deque([])
        self.sum = 0

    def next(self, val: int) -> float:
        self.list.append(val)
        self.sum += val
        if len(self.list) > self.size:
            value = self.list.popleft()
            self.sum -= value
        return self.sum / len(self.list)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)