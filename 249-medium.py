from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        bucket = defaultdict(list)

        # find the bucket for the string. 
        for string in strings:
            # convert from string to number
            # number = [ord(l) - ord('a') for l in string]
            # normalization, corner case: mod 26, because the number is cycling 
            number = tuple((ord(string[i]) - ord(string[0])) % 26 for i in range(len(string)))
            # return as tuple.
            bucket[number].append(string)
        return [i for i in bucket.values()]

