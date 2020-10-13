class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        # negative value
        for op in ops:
            if op.isdigit() or (op[0] == '-' and op[1:].isdigit()):
                res.append(int(op))
            elif op == 'C':
                res.pop()
            elif op == 'D':
                res.append(res[-1] * 2)
            elif op == '+':
                res.append(res[-1] + res[-2])
        return sum(res)