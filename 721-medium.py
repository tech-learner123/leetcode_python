from collections import defaultdict


# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]
# dfs solution
# """
#     # build the adjacent list
#     adj_list = defaultdict(set)
#     email_to_name = dict()
#     for account in accounts:
#         for email in account[1:]:
#             adj_list[account[1]].add(email)
#             adj_list[email].add(account[1])
#             email_to_name[email] = account[0]
#     # print(adj_list)
#     # dfs to gather the connected component
#     visited = set()
#     res = []
#     for email in adj_list:
#         if email not in visited:
#             visited.add(email)
#             stack = [email]
#             emails = []
#             while stack:
#                 email = stack.pop()
#                 emails.append(email)
#                 for alt_email in adj_list[email]:
#                     if alt_email not in visited:
#                         stack.append(alt_email)
#                         visited.add(alt_email)
#             res.append([email_to_name[email]] + sorted(emails))
#     return res
#     """
class DSU:
    def __init__(self):
        self.p = range(10001)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution(object):
    def accountsMerge(self, accounts):
        dsu = DSU()
        em_to_name = {}
        em_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[acc[1]], em_to_id[email])

        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[dsu.find(em_to_id[email])].append(email)
        print(ans)
        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]



