# https://leetcode.com/problems/nested-list-weight-sum-ii/discuss/83643/Python-solution-with-detailed-explanation


class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        total_sum, level_sum = 0, 0
        while len(nestedList):
            next_level_list = []
            for x in nestedList:
                if x.isInteger():
                    level_sum += x.getInteger()
                else:
                    for y in x.getList():
                        next_level_list.append(y)
            total_sum += level_sum
            nestedList = next_level_list
        return total_sum