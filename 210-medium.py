from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # corner cases, no prerequisites
        if not prerequisites:
            return [i for i in range(numCourses)]

        # build the graph
        neigh = defaultdict(list)
        # store the number of inbound
        in_degree = {}
        for course in prerequisites:
            course, prereq = course[0], course[1]
            neigh[course].append(prereq)
            in_degree[prereq] = in_degree.get(prereq, 0) + 1

        zero_in_degree_course = deque([i for i in range(numCourses) if i not in in_degree])
        sort = []

        while zero_in_degree_course:
            course = zero_in_degree_course.popleft()
            sort.append(course)
            if course in neigh:
                for nei in neigh[course]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0:
                        zero_in_degree_course.append(nei)

        return sort[::-1] if len(sort) == numCourses else []
