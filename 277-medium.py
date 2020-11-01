# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:

        celebrity = 0
        for p in range(n):

            if knows(celebrity, p):
                celebrity = p
        # Corner case. don't forget to add this part.
        for i in range(celebrity):
            if knows(celebrity, i):
                return -1

        for p in range(n):
            if not knows(p, celebrity):
                return -1
        return celebrity
