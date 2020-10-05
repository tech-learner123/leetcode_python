from collections import defaultdict, deque


class Solution:

    def __init__(self):

        self.transform = defaultdict(list)

    def one_step_bfs(self, que, visited, other_visited):
        cur_word, level = que.popleft()

        for l in range(len(cur_word)):
            intermediate = cur_word[:l] + '*' + cur_word[l + 1:]
            for word in self.transform[intermediate]:
                if word in other_visited:
                    return level + other_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    que.append((word, level + 1))
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0

        for word in wordList:
            for l in range(len(word)):
                intermediate = word[:l] + '*' + word[l + 1:]
                self.transform[intermediate].append(word)
        # Bi-directional bfs
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}

        que_begin = deque([(beginWord, 1)])
        que_end = deque([(endWord, 1)])

        while que_begin and que_end:

            ans = self.one_step_bfs(que_begin, visited_begin, visited_end)
            if ans:
                return ans
            ans = self.one_step_bfs(que_end, visited_end, visited_begin)
            if ans:
                return ans
        return 0
