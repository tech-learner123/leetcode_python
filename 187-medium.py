class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
        """
         # Brute force approach: Linear-time slice using substring + hashset
        seen = set()
        res = set()
        for i in range(len(s) - 10 + 1):
            new = s[i: i+10]
            if new in seen:
                res.add(new)
            else:
                seen.add(new)
        return res
        """
        total_length = 10
        # rolling hash parameters: base is 4
        a = 4
        a_total_length = pow(a, total_length)

        # convert string to array of integers
        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int.get(l) for l in s]

        seen, output = set(), set()
        h = 0
        for start in range(len(s) - 10 + 1):
            if start != 0:
                # adding the new digit in and remove the previous digit.
                h = h * a - nums[start - 1] * a_total_length + nums[start + total_length - 1]
            else:
                for i in range(total_length):
                    h = h * a + nums[i]
            # update the output and hashset of seen sequence:
            if h in seen:
                output.add(s[start: start + total_length])
            else:
                seen.add(h)
        return output
