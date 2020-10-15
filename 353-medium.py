from collections import deque


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.snake = deque([[0, 0]])
        self.width = width
        self.height = height
        self.food = deque(food)
        self.direction = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """

        newhead_r, newhead_c = self.snake[0][0] + self.direction[direction][0], self.snake[0][1] + \
                               self.direction[direction][1]

        if newhead_r < 0 or newhead_c < 0 or newhead_r >= self.height or newhead_c >= self.width or (
                [newhead_r, newhead_c] in self.snake and self.snake[-1] != [newhead_r, newhead_c]):
            return -1
        if self.food and self.food[0] == [newhead_r, newhead_c]:
            self.snake.appendleft([newhead_r, newhead_c])
            self.food.popleft()
        else:
            self.snake.appendleft([newhead_r, newhead_c])
            self.snake.pop()
        return len(self.snake) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)