from domain import Snake
from random import  randint
from texttable import *



class Board:
    def __init__(self, size, nr_apples):
        self.__size = size
        self.__snake = Snake(self.__generate_snake(size), "up")
        self.__apples = {}

        self.__generate_apples(size, nr_apples)

    def __generate_snake(self, size):
        return [[size//2, (size+1)//2], [size//2+1, (size+1)//2], [size//2+2, (size+1)//2]]

    def __check(self, l, c, matrix):
        if matrix[l][c] != " ":
            return False
        if matrix[l-1][c] != " ":
            return False
        if matrix[l+1][c] != " ":
            return False
        if matrix[l][c-1] != " ":
            return False
        if matrix[l][c+1] != " ":
            return False
        return True

    def __generate_matrix(self):
        matrix = []
        for i in range(0, self.__size+2):
            matrix.append([])
            for j in range(0, self.__size+2):
                matrix[i].append(" ")

        for i in self.__snake.position:
            matrix[i[0]][i[1]] = "+"
        matrix[self.__snake.position[0][0]][self.__snake.position[0][1]] = "*"

        for apple in self.__apples.values():
            matrix[apple[0]][apple[1]] = "a"
        return matrix

    def __generate_apples(self, size, nr_apples):
        while nr_apples:

            l = randint(1, size)
            c = randint(1, size)

            if self.__check(l, c, self.__generate_matrix()):
                self.__apples[str(l) + str(c)] = [l, c]
                nr_apples -= 1

    def update_snake(self, snake):
        new_snake = Snake(snake, self.snake.direction)
        self.__snake = new_snake
    def update_direction(self, new_direction):
        new_snake = Snake(self.snake.position, new_direction)
        self.__snake = new_snake

    def remove_apple(self, l, c):
        self.__apples.pop(str(l) + str(c))

    def isSnake(self, l, c):
        if [l, c] in self.__snake.position:
            return True
        return False

    def isApple(self, l, c):
        if (str(l) + str(c)) in self.__apples.keys():
            return True
        return False

    def add_apple(self):
        while True:
            l = randint(1, self.__size)
            c = randint(1, self.__size)

            if self.__check(l, c, self.__generate_matrix()):
                self.__apples[str(l) + str(c)] = [l, c]
                break

    def __str__(self):
        table = Texttable()
        matrix = self.__generate_matrix()
        for i in range(1, self.__size+1):
            line = matrix[i][1:]
            line = line[:-1]
            table.add_row(line)
        return table.draw()
    @property
    def snake(self):
        return self.__snake
    @property
    def size(self):
        return self.__size