class Snake:
    def __init__(self, position : list, direction):
        self.__position = position
        self.__direction = direction

    @property
    def position(self):
        return self.__position
    @property
    def direction(self):
        return self.__direction