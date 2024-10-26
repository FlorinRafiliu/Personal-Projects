from repository import  Board


class SnakeService:
    def __init__(self, repo : Board):
        self.__repo = repo
        self.__score = 0
    def print_board(self):
        return self.__repo
    def move(self):
        snake = self.__repo.snake.position
        direction = self.__repo.snake.direction
        size = self.__repo.size

        if direction == "up":
            new_head = [snake[0][0] - 1, snake[0][1]]
            if new_head[0] < 1:
                return False
        elif direction == "left":
            new_head = [snake[0][0], snake[0][1] - 1]
            if new_head[1] < 1:
                return False
        elif direction == "down":
            new_head = [snake[0][0] + 1, snake[0][1]]
            if new_head[0] > size:
                return False
        elif direction == "right":
            new_head = [snake[0][0], snake[0][1] + 1]
            if new_head[1] > size :
                return False

        if self.__repo.isSnake(new_head[0], new_head[1]):
            return False

        new_snake = [new_head] + snake

        self.__repo.update_snake(new_snake)
        if self.__repo.isApple(new_snake[0][0], new_snake[0][1]):
            self.__repo.remove_apple(new_snake[0][0], new_snake[0][1])
            self.__repo.add_apple()
            self.__score += 1
        else:
            new_snake.pop()

        return True

    def change_direction(self, new_direction):
        if not(new_direction == "up" or new_direction == "down" or new_direction == "right" or new_direction == "left"):
            raise ValueError("Invalid command!")

        direction = self.__repo.snake.direction

        if direction == "up" and new_direction == "down" or direction == "down" and new_direction == "up":
            raise ValueError("Invalid command!")
        if direction == "right" and new_direction == "left" or direction == "left" and new_direction == "right":
            raise ValueError("Invalid command!")

        self.__repo.update_direction(new_direction)
        return self.move()
    @property
    def score(self):
        return self.__score