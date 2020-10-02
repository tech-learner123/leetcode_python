from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_need_to_remove = []
        stack = deque([])

        for index, l in enumerate(s):
            if l == '(':
                stack.append(index)
            elif l == ')':
                if stack:
                    stack.pop()
                else:
                    index_need_to_remove.append(index)
        if stack:
            index_need_to_remove.extend(stack)
        res = ''
        for index, l in enumerate(s):
            if index not in index_need_to_remove:
                res += l
        return res