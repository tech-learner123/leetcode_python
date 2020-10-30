class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sum = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.sum:
            self.sum[number] += 1
        else:
            self.sum[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """

        for num in self.sum.keys():
            comple = value - num
            # Corner case: the 2 - 1 = 1
            if num != comple:
                if comple in self.sum:
                    return True
            elif self.sum[comple] > 1:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)