class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = float("inf")
        for token in tokens:
            if token in "+-*/":
                second, first = stack.pop(), stack.pop()
                # print(first, second)
                ans = int(eval(str(first) + token + str(second)))
                # print(ans)
                stack.append(ans)
            else:
                stack.append(token)
        return int(stack[0]) if ans==float('inf') else ans