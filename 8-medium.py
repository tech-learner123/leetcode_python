class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        res = 0

        # Edge cases: 1. string not exists
        if not s:
            return 0
        # Edge cases: if alpha first
        s = s.strip()
        # Edge cases: if " "
        if not s or s[0].isalpha():
            return 0

        int_max = pow(2, 31) - 1
        int_min = - pow(2, 31)
        # edge cases: '+- 12' -> not valid
        if s[0] == "+":
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]
            negative = True

        for letter in s:
            if letter.isdigit():
                res = res * 10 + int(letter)
            else:
                break
        if negative:
            res = res * (-1)
        # edge case: out of boundary
        if res > int_max:
            return int_max

        if res < int_min:
            return int_min

        return res
    # did't pass
#         str = s
#         if not str or len(str) < 1:
#             return 0
#         i = 0
#         while str[i] == ' ':
#             i += 1
#         str = str[i:]
#         j = 0
#         sign = '+'
#         if str[0] == '-':
#             sign = '-'
#             j += 1
#         elif str[0] == '+':
#             j += 1

#         result = 0
#         while len(str) > j and str[j] >= '0' and str[j] <= '9':
#             result = result * 10 + (ord(str[j]) - ord('0'))
#             j += 1
#         if sign == '-':
#             result = -result
#         if result > 2147483647:
#             return 2147483647
#         elif result < -2147483648:
#             return -2147483648
#         else:
#             return result