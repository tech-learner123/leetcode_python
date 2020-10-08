from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # dfs solution

        # build the adjacent list
        adj_list = defaultdict(set)
        email_to_name = dict()
        for account in accounts:
            for email in account[1:]:
                adj_list[account[1]].add(email)
                adj_list[email].add(account[1])
                email_to_name[email] = account[0]
        # print(adj_list)
        # dfs to gather the connected component
        visited = set()
        res = []
        for email in adj_list:
            if email not in visited:
                visited.add(email)
                stack = [email]
                emails = []
                while stack:
                    email = stack.pop()
                    emails.append(email)
                    for alt_email in adj_list[email]:
                        if alt_email not in visited:
                            stack.append(alt_email)
                            visited.add(alt_email)
                res.append([email_to_name[email]] + sorted(emails))
        return res
