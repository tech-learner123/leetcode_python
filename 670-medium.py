class Solution:
    def maximumSwap(self, num: int) -> int:
        number = list(str(num))

        last = {int(x): i for i, x in enumerate(number)}
        # replace with the largest value.
        for i, x in enumerate(number):

            for d in range(9, int(x), -1):
                if last.get(d, 0) > i:
                    number[i], number[last[d]] = number[last[d]], number[i]
                    return int(''.join(number))
        return num