from service import SnakeService
from repository import Board

class UI:
    def __init__(self, service : SnakeService):
        self.__service = service

    def print_board(self):
        print(self.__service.print_board())

    def move(self, n):
        try:
            n = int(n)
        except:
            raise ValueError("<N> must be integer!")
        while n:
            conclusion = self.__service.move()
            if conclusion == False:
                return False
            n -= 1
        return True
    def move_direction(self, direction):
        return self.__service.change_direction(direction)

    def start(self):
        directions = ["up", "down", "left", "right"]

        while True:
            self.print_board()
            print("Score:",self.__service.score)
            
            conclusion = True
            option = input(" <<< ")
            option = option.split()

            try:
                if option[0] == "move" and len(option) == 1:
                    conclusion = self.move(1)
                elif option[0] == "move" and len(option) == 2:
                    conclusion = self.move(option[1])
                elif option[0] in directions and len(option) == 1:
                    conclusion = self.move_direction(option[0])
                else:
                    print ("Invalid command")
            except ValueError as ve:
                print(ve)

            if conclusion == False:
                print("YOU LOSE!")
                break

repo = Board(7, 10)
service = SnakeService(repo)
ui = UI(service)
ui.start()