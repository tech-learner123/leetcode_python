# backtracking.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s='', left=0, right=0):
            # think what is the return condition
            if len(s) == 2 * n:
                ans.append(s)
                return
            # think: how to add element
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack()

        return ans
