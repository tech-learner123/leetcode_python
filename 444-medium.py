from collections import defaultdict, deque


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # topological sort, check how many unique zero_incoming_node, if less than 1 and

        if not seqs:
            return False
        # corner case: only one element in the input.
        if len(org) == 1:
            for seq in seqs:
                if seq != org:
                    return False
            return True

        graph = defaultdict(list)
        in_coming_degree = {}
        # more than 1 element in the list
        for seq in seqs:
            # corner case: check whether the value in the range or not.
            if len(seq) < 2 and seq[0] > len(org):
                return False
            for index in range(len(seq) - 1):
                first, second = seq[index], seq[index + 1]
                if first > n or second > n:
                    return False
                # build the graph
                graph[first].append(second)
                in_coming_degree[second] = in_coming_degree.get(second, 0) + 1

        zero_in_coming_degree = deque([i for i in range(1, len(org) + 1) if i not in in_coming_degree and i in graph])

        # print(zero_in_coming_degree)
        if len(zero_in_coming_degree) > 1:
            return False
        sort_list = []
        while zero_in_coming_degree:
            if len(zero_in_coming_degree) > 1:
                return False
            node = zero_in_coming_degree.popleft()
            sort_list.append(node)
            # question when would be the case where node not in graph -> when the node is the receiving end. [2, 3] 3 wil not be in the key.
            if node in graph:
                for n in graph[node]:
                    in_coming_degree[n] -= 1
                    if in_coming_degree[n] == 0:
                        zero_in_coming_degree.append(n)
        print(sort_list)
        return sort_list == org

