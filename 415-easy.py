class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            # Convert string to int
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            # Convert string to int
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            sum_ = x1 + x2 + carry
            carry, value = divmod(sum_, 10)
            res.append(value)
            p1 -= 1
            p2 -= 1
        # if two numbers have different length of digits
        if carry:
            res.append(carry)

        # reverse the list order,
        return ''.join(str(x) for x in res[::-1])