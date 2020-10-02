class Solution:
    def calculate(self, s: str) -> int:

        if not s:
            return "0"
        stack, num, sign = [], 0, "+"
        for i, l in enumerate(s):

            if l.isdigit():
                # Corner case: multi-digit number
                num = num * 10 + ord(s[i]) - ord("0")
            # Corner case: 1. the last string 2. empty space.
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                # think: the sign here is the previous sign
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    # Corner case: when the negative case: 14 - 3/2
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                sign = l
                num = 0
        return sum(stack)