"""

The idea of GetRandom is to choose a random index and then to retrieve an element with that index.
There is no indexes in hashmap,
and hence to get true random value, one has first to convert hashmap keys in a list,
that would take linear time.
The solution here is to build a list of keys aside and to use this list to compute GetRandom in constant time.

"""
from random import choice


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []
        self.index = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False

        self.dict[val] = self.index
        self.list.append(val)
        self.index += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict:
            return False
        val_index = self.dict[val]
        # corner case when the remove one is itself
        if val_index != (len(self.list) - 1):
            self.list[-1], self.list[val_index] = self.list[val_index], self.list[-1]
            self.dict[self.list[val_index]] = val_index
        self.list.pop()
        self.index -= 1
        # update the dictionary
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
