class Solution:
    def romanToInt(self, s: str) -> int:
        #         symbol_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        #         if not s:
        #             return s
        #         res = 0
        #         if len(s) < 2:
        #             return symbol_value[s[0]]

        #         for index in range(len(s) - 1):

        #             cur_value = symbol_value[s[index]]
        #             next_value = symbol_value[s[index + 1]]
        #             if cur_value >= next_value:
        #                 res += cur_value
        #             else:
        #                 res += -cur_value

        #         res += symbol_value[s[-1]]
        #         return res

        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += values[s[i]]
                i += 1
        return total