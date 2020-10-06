class Solution:
    def isValid(self, s: str) -> bool:
        left_dict = {')': '(', ']': '[', '}': '{'}
        stack = []
        for l in s:
            if l in left_dict:
                if stack and left_dict[l] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)
        if stack:
            return False
        return True
