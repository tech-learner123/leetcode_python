class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # letter  index mapping
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            # very smart, use the max(j, last[c]) -> get the maximum index of the partition
            j = max(j, last[c])
            # if the i move to the maximum cursor than count the number of elemennt between i and anchor
            if i == j:
                ans.append(i-anchor + 1)
                anchor = i + 1
        return ans