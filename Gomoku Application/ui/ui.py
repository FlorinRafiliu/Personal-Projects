from src.domain.board import Board
from src.domain.ai import AI
from src.domain.player import Player
from src.services.gameservices import AIService, BoardService


class UI:
    def __init__(self, board_service: BoardService, ai_service: AIService):
        self.__board_service = board_service
        self.__ai_service = ai_service

    @staticmethod
    def print_menu():
        print("Welcome to gomoku game:")
        print("1. Start new game!")
        print("0. Exit")

    @staticmethod
    def valid_column(message):
        if message.isdigit():
            column = int(message)
            if 0 < column < 16:
                return True
        return False

    @staticmethod
    def valid_row(message):
        if message.isdigit():
            column = int(message)
            if 0 < column < 16:
                return True
        return False

    def human_vs_computer(self):
        name = input("Enter your name: ")
        player1 = Player(name, '🅧')
        player2 = AI('🅥', '🅧')
        board = Board()

        print(player1)
        print(player2)
        print(board)

        while self.__board_service.is_draw(board) is False:
            row1 = input(player1.name + ", choose the row for your move: ")
            while self.valid_row(row1) is False:
                row1 = input("Invalid row number, please choose a number between 1 and 15: ")

            column1 = input(player1.name + ", choose the column for your move: ")
            while self.valid_column(column1) is False:
                column1 = input("Invalid column number, please choose a number between 1 and 15: ")

            row1 = int(row1)
            column1 = int(column1)

            row1 -= 1
            column1 -= 1

            while self.__board_service.move(board, player1.symbol, row1, column1) is False:
                print("Please choose a position which is not full: ")
                row1 = input("New row: ")
                while self.valid_row(row1) is False:
                    row1 = input("Invalid row number, please choose a number between 1 and 15: ")
                row1 = int(row1)
                row1 -= 1

                column1 = input("New column: ")
                while self.valid_column(column1) is False:
                    column1 = input("Invalid column number, please choose a number between 1 and 7: ")
                column1 = int(column1)
                column1 -= 1

            if self.__board_service.is_game_won(board) is False:
                row2, column2 = self.__ai_service.move(player2, board)
                print("The computer chose the row = " + str(row2) + " and column = " + str(column2))

                row2 -= 1
                column2 -= 1

                self.__board_service.move(board, player2.symbol, row2, column2)
                print(player1)
                print(player2)
                print(board)

                if self.__board_service.is_game_won(board) is True:
                    print("The computer won!")
                    break
                continue
            print("{} won!".format(player1.name))
            break
        if self.__board_service.is_draw(board) is True:
            print("Draw!")

    def menu(self):
        while True:
            UI.print_menu()
            option = input("Choose an option: ")
            if option == '1':
                self.human_vs_computer()
            elif option == "0":
                break
            else:
                print("Invalid operation!")


board_service = BoardService()
ai_service = AIService()
Game = UI(board_service, ai_service)
Game.menu()
