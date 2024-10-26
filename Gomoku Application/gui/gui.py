import tkinter as tk
from tkinter import simpledialog

from termcolor import colored


from src.domain.board import Board
from src.domain.ai import AI
from src.domain.player import Player
from src.services.gameservices import AIService, BoardService


class GUI:
    def __init__(self, board_service, ai_service):
        self.board_service = board_service
        self.ai_service = ai_service
        self._window = tk.Tk()
        self._window.configure(bg='blue')

    def start(self):
        self._window.title("Gomoku")
        btn_human_vs_human = tk.Button(master=self._window, width= 35, text='Start new game!', bg='#FFDDE2', command=self.human_vs_computer)
        btn_human_vs_human.pack()
        btn_exit = tk.Button(master=self._window, width= 25 ,text='Exit', bg='#FFDDE2', command=self._window.destroy)
        btn_exit.pack()
        self._window.mainloop()

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
        name = simpledialog.askstring(title="-1st player-", prompt="Enter your name:")
        player1 = Player(name, '🅧')
        player2 = AI('🅥', '🅧')

        board = Board()

        scroll_bar = tk.Scrollbar(self._window)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_text = tk.Text(master=self._window, height=40, width=80)
        scroll_text.pack(side=tk.LEFT, fill=tk.Y)
        scroll_bar.config(command=scroll_text.yview)
        scroll_text.config(yscrollcommand=scroll_bar.set)

        text = str(player1) + "\n" + str(player2) + "\n" + str(board) + "\n"
        scroll_text.insert(tk.END, text)
        while self.board_service.is_draw(board) is False:
            row1 = simpledialog.askstring(title="-move-", prompt="{}, choose a row:".format(player1.name))
            while self.valid_row(row1) is False:
                row1 = simpledialog.askstring(title="-move-",
                                                 prompt="Invalid number, choose a value between 1 and 15: ")
            row1 = int(row1)
            row1 -= 1

            column1 = simpledialog.askstring(title="-move-", prompt="{}, choose a column:".format(player1.name))
            while self.valid_column(column1) is False:
                column1 = simpledialog.askstring(title="-move-", prompt="Invalid number, choose a value between 1 and 15: ")
            column1 = int(column1)
            column1 -= 1

            while self.board_service.move(board, player1.symbol, row1, column1) is False:
                row1 = simpledialog.askstring(title="-move-", prompt="Choose a valid row: ")
                while self.valid_row(row1) is False:
                    row1 = simpledialog.askstring(title="-move-", prompt="Invalid number, choose between 1 and 15: ")
                row1 = int(row1)
                row1 -= 1

                column1 = simpledialog.askstring(title="-move-", prompt="Choose a valid column: ")
                while self.valid_column(column1) is False:
                    column1 = simpledialog.askstring(title="-move-", prompt="Invalid number, choose between 1 and 15: ")
                column1 = int(column1)
                column1 -= 1

            text = str(board) + "\n"
            scroll_text.insert(tk.END, text)
            #scroll_text.replace(tk.FIRST, text)
            if self.board_service.is_game_won(board) is False:
                text = "The computer is thinking ... \n"
                scroll_text.insert(tk.END, text)

                row2, column2 = self.ai_service.move(player2, board)
                row2 -= 1
                column2 -= 1
                text = "The computer chose the row = " + str(row2 + 1) + " and column = " + str(column2 + 1) + "\n"
                scroll_text.insert(tk.END, text)
                #scroll_text.replace(tk.FIRST, text)
                self.board_service.move(board, player2.symbol, row2, column2)
                text = str(board) + "\n"
                scroll_text.insert(tk.END, text)
                if self.board_service.is_game_won(board) is True:
                    text = "The computer won! \n"
                    scroll_text.insert(tk.END, text)
                    break
                continue
            text = "{} won!\n".format(player1.name)
            scroll_text.insert(tk.END, text)
            break
        if self.board_service.is_draw(board) is True:
            text = "Draw!\n"
            scroll_text.insert(tk.END, text)


board_service = BoardService()
ai_service = AIService()
GUI(board_service, ai_service).start()