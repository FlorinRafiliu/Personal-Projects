from src.domain.board import Board
from src.domain.ai import AI

class BoardService:
    def is_game_won(self, board):
        """
            Checks if the game is finished
        :param board: the current state of the board
        :return: True - id someone win the game
                 False - otherwise
        """
        for i in range(0, 11):
            for j in range(0, 11):
                if board.matrix[i][j] != "○":
                    win1 = True  # row win
                    win2 = True  # column win
                    win3 = True  # diag1 win
                    if j >= 4:
                        win4 = True
                    else:
                        win4 = False
                    for k in range(0, 5):
                        if board.matrix[i][j+k] != board.matrix[i][j]:
                            win1 = False
                        if board.matrix[i+k][j] != board.matrix[i][j]:
                            win2 = False
                        if board.matrix[i+k][j+k] != board.matrix[i][j]:
                            win3 = False
                        if j >= 4:
                            if board.matrix[i+k][j-k] != board.matrix[i][j]:
                                win4 = False
                    if win1 == True or win2 == True or win3 == True or win4 == True:
                        return True
        return  False

    def is_draw(self, board):
        """
            Checks if the game is a draw
        :return: True if the game is a draw and False otherwise
        """
        for row in range(15):
            for column in range(15):
                if board.matrix[row][column] == '○':
                    return False
        return True

    def move(self, board, symbol, row, column):
        """
            A move on the board
        :param board: the current state of the board
        :param symbol: the symbol of the player who moved
        :param column: the column in which the circle will be introduced
        :return: True if the move is possible on that row and column, false otherwise
        """
        if board.matrix[row][column] == "○":
            board.matrix[row][column] = symbol
            return True
        return False


class AIService:
    @staticmethod
    def find_computer_win_situation(ai, board):
        """
            Find if the computer have such a move that win the game
        :param ai:
        :param board: The current state of the board
        :return: Coordinates of the winning move
                (-1, -1) if such move don t exist
        """
        for i in range(0, 15):
            for j in range(0, 15):
                if board.matrix[i][j] == ai.symbol:
                    win1 = win2 = win3 = win4 = (-1, -1, False)

                    if j > 0:
                        if board.matrix[i][j - 1] == "○":
                            win1 = (i, j - 1, True)

                    if j + 4 < 15:
                        if board.matrix[i][j + 4] == "○":
                            win1 = (i, j + 4, True)

                    if i > 0:
                        if board.matrix[i - 1][j] == "○":
                            win2 = (i - 1, j, True)

                    if i + 4 < 15:
                        if board.matrix[i + 4][j] == "○":
                            win2 = (i + 4, j, True)

                    if i > 0 and j > 0:
                        if board.matrix[i - 1][j - 1] == "○":
                            win3 = (i - 1, j - 1, True)

                    if i + 4 < 15 and j + 4 < 15:
                        if board.matrix[i + 4][j + 4] == "○":
                            win3 = (i + 4, j + 4, True)

                    if i > 0 and j + 1 < 15:
                        if board.matrix[i - 1][j + 1] == "○":
                            win4 = (i - 1, j + 1, True)
                    if j > 3 and i + 4 < 15:
                        if board.matrix[i + 4][j - 4] == "○":
                            win4 = (i + 4, j - 4, True)

                    for k in range(0, 4):
                        if j + k < 15:
                            if board.matrix[i][j + k] != board.matrix[i][j]:
                                win1 = (-1, -1, False)
                        if i + k < 15:

                            if board.matrix[i + k][j] != board.matrix[i][j]:
                                win2 = (-1, -1, False)
                        if i + k < 15 and j + k < 15:
                            if board.matrix[i + k][j + k] != board.matrix[i][j]:
                                win3 = (-1, -1, False)
                        if j >= 2 and i + k < 15:
                            if board.matrix[i + k][j - k] != board.matrix[i][j]:
                                win4 = (-1, -1, False)

                    if win1[2] == True:
                        return [win1[0], win1[1]]
                    if win2[2] == True:
                        return [win2[0], win2[1]]
                    if win3[2] == True:
                        return [win3[0], win3[1]]
                    if win4[2] == True:
                        return [win4[0], win4[1]]
        return -1, -1
    @staticmethod
    def find_human_win_situation(ai : AI, board):
        """
            Find if the human is one step to guaranteed win
        :param ai: ai
        :param board: current state of the board
        :return: coordinates of the computer move
        """

        for i in range(0, 15):
            for j in range(0, 15):
                if board.matrix[i][j] == ai.human_symbol:
                    same = []
                    neutru = []
                    # row win
                    for k in range(0, 5):
                        if j + k < 15:
                            if board.matrix[i][j + k] == board.matrix[i][j]:
                                same.append((i, j + k))
                            elif board.matrix[i][j + k] == "○":
                                neutru.append((i, j + k))

                    if len(same) == 4 and len(neutru) == 1:
                        return neutru[0][0], neutru[0][1]

                    same = []
                    neutru = []
                    #column win
                    for k in range(0, 5):
                        if i + k < 15:
                            if board.matrix[i+k][j] == board.matrix[i][j]:
                                same.append((i + k, j))
                            elif board.matrix[i + k][j] == "○":
                                neutru.append((i + k, j))

                    if len(same) == 4 and len(neutru) == 1:
                        return neutru[0][0], neutru[0][1]

                    same = []
                    neutru = []
                    #diag1 win
                    for k in range(0, 5):
                        if i + k < 15 and j + k < 15:
                            if board.matrix[i + k][j + k] == board.matrix[i][j]:
                                same.append((i + k, j + k))
                            elif board.matrix[i + k][j + k] == "○":
                                neutru.append((i + k, j + k))

                    if len(same) == 4 and len(neutru) == 1:
                        return neutru[0][0], neutru[0][1]

                    same = []
                    neutru = []
                    #diag2 win
                    for k in range(0, 5):
                        if j - k > -1 and i + k < 15:
                            if board.matrix[i + k][j - k] == board.matrix[i][j]:
                                same.append((i + k, j - k))
                            elif board.matrix[i + k][j - k] == "○":
                                neutru.append((i + k, j - k))

                    if len(same) == 4 and len(neutru) == 1:
                        return neutru[0][0], neutru[0][1]

        for i in range(0, 15):
            for j in range(0, 15):
                if board.matrix[i][j] == ai.human_symbol:
                    win1 = win2 = win3 = win4 = (-1, -1, False)

                    if j > 0:
                        if board.matrix[i][j - 1] == "○":
                            win1 = (i, j - 1, True)

                    if j + 4 < 15:
                        if board.matrix[i][j + 4] == "○":
                            win1 = (i, j + 4, True)

                    if i > 0:
                        if board.matrix[i - 1][j] == "○":
                            win2 = (i - 1, j, True)

                    if i + 4 < 15:
                        if board.matrix[i + 4][j] == "○":
                            win2 = (i + 4, j, True)

                    if i > 0 and j > 0:
                        if board.matrix[i - 1][j - 1] == "○":
                            win3 = (i - 1, j - 1, True)

                    if i + 4 < 15 and j + 4 < 15:
                        if board.matrix[i + 4][j + 4] == "○":
                            win3 = (i + 4, j + 4, True)

                    if i > 0 and j + 1 < 15:
                        if board.matrix[i - 1][j + 1] == "○":
                            win4 = (i - 1, j + 1, True)
                    if j > 3 and i + 4 < 15:
                        if board.matrix[i + 4][j - 4] == "○":
                            win4 = (i + 4, j - 4, True)

                    for k in range(0, 4):
                        if j + k < 15:
                            if board.matrix[i][j + k] != board.matrix[i][j]:
                                win1 = (-1, -1, False)
                        if i + k < 15:
                            if board.matrix[i + k][j] != board.matrix[i][j]:
                                win2 = (-1, -1, False)
                        if i + k < 15 and j + k < 15:
                            if board.matrix[i + k][j + k] != board.matrix[i][j]:
                                win3 = (-1, -1, False)
                        if j >= 2 and i + k < 15:
                            if board.matrix[i + k][j - k] != board.matrix[i][j]:
                                win4 = (-1, -1, False)

                    if win1[2] == True:
                        return [win1[0], win1[1]]
                    if win2[2] == True:
                        return [win2[0], win2[1]]
                    if win3[2] == True:
                        return [win3[0], win3[1]]
                    if win4[2] == True:
                        return [win4[0], win4[1]]

        for i in range(0, 15):
            for j in range(0, 15):
                if board.matrix[i][j] == ai.human_symbol:
                    win1 = win2 = win3 = win4 = (-1, -1, False)
                    if j > 0 and j + 3 < 15:
                        if board.matrix[i][j-1] == "○" and board.matrix[i][j+3] == "○":
                            win1 = (i, j-1, True)
                    if i > 0 and i + 3 < 15:
                        if board.matrix[i-1][j] == "○" and board.matrix[i+3][j] == "○":
                            win2 = (i-1, j, True)
                    if i > 0 and j > 0 and i + 3 < 15 and j + 3 < 15:
                        if board.matrix[i-1][j-1] == "○" and board.matrix[i+3][j+3] == "○":
                            win3 = (i-1, j-1, True)
                    if i > 0 and j > 2 and i + 3 < 15 and j + 1 < 15:
                        if board.matrix[i-1][j+1] == "○" and board.matrix[i+3][j-3] == "○":
                            win4 = (i-1, j+1, True)

                    for k in range(0, 3):
                        if j + k < 15:
                            if board.matrix[i][j+k] != board.matrix[i][j]:
                                win1 = (-1, -1, False)
                        if i + k < 15:
                            if board.matrix[i+k][j] != board.matrix[i][j]:
                                win2 = (-1, -1, False)
                        if i + k < 15 and j + k < 15:
                            if board.matrix[i+k][j+k] != board.matrix[i][j]:
                                win3 = (-1, -1, False)
                        if j >= 2 and i + k < 15:
                            if board.matrix[i+k][j-k] != board.matrix[i][j]:
                                win4 = (-1, -1, False)

                    if win1[2] == True:
                        return [win1[0], win1[1]]
                    if win2[2] == True:
                        return [win2[0], win2[1]]
                    if win3[2] == True:
                        return [win3[0], win3[1]]
                    if win4[2] == True:
                        return [win4[0], win4[1]]

        return  -1, -1
    @staticmethod
    def find_computer_move(ai, board):
        """
            Find a good move for the computer
        :param ai: ai
        :param board: Current state of the computer
        :return: coordinates of the computer move
        """
        for i in range(0, 15):
            for j in range(0, 15):
                if board.matrix[i][j] == ai.symbol:
                    win1 = win2 = win3 = win4 = (-1, -1, False)

                    if j > 0:
                        if board.matrix[i][j - 1] == "○":
                            win1 = (i, j - 1, True)

                    if j + 4 < 15:
                        if board.matrix[i][j + 4] == "○":
                            win1 = (i, j + 4, True)

                    if i > 0:
                        if board.matrix[i - 1][j] == "○":
                            win2 = (i - 1, j, True)

                    if i + 4 < 15:
                        if board.matrix[i + 4][j] == "○":
                            win2 = (i + 4, j, True)

                    if i > 0 and j > 0:
                        if board.matrix[i - 1][j - 1] == "○":
                            win3 = (i - 1, j - 1, True)

                    if i + 4 < 15 and j + 4 < 15:
                        if board.matrix[i + 4][j + 4] == "○":
                            win3 = (i + 4, j + 4, True)

                    if i > 0 and j + 1 < 15:
                        if board.matrix[i - 1][j + 1] == "○":
                            win4 = (i - 1, j + 1, True)
                    if j > 3 and i + 4 < 15:
                        if board.matrix[i + 4][j - 4] == "○":
                            win4 = (i + 4, j - 4, True)

                    for k in range(0, 4):
                        if j + k < 15:
                            if board.matrix[i][j + k] != board.matrix[i][j]:
                                win1 = (-1, -1, False)
                        if i + k < 15:
                            if board.matrix[i + k][j] != board.matrix[i][j]:
                                win2 = (-1, -1, False)
                        if i + k < 15 and j + k < 15:
                            if board.matrix[i + k][j + k] != board.matrix[i][j]:
                                win3 = (-1, -1, False)
                        if j >= 2 and i + k < 15:
                            if board.matrix[i + k][j - k] != board.matrix[i][j]:
                                win4 = (-1, -1, False)

                    if win1[2] == True:
                        return [win1[0], win1[1]]
                    if win2[2] == True:
                        return [win2[0], win2[1]]
                    if win3[2] == True:
                        return [win3[0], win3[1]]
                    if win4[2] == True:
                        return [win4[0], win4[1]]

        for i in range(0, 15):
            for j in range(0, 15):
                if board.matrix[i][j] == ai.symbol:
                    win1 = win2 = win3 = win4 = (-1, -1, False)

                    if j > 0:
                        if board.matrix[i][j - 1] == "○":
                            win1 = (i, j - 1, True)

                    if j + 3 < 15:
                        if board.matrix[i][j + 3] == "○":
                            win1 = (i, j + 3, True)

                    if i > 0:
                        if board.matrix[i - 1][j] == "○":
                            win2 = (i - 1, j, True)

                    if i + 3 < 15:
                        if board.matrix[i + 3][j] == "○":
                            win2 = (i + 3, j, True)

                    if i > 0 and j > 0:
                        if board.matrix[i - 1][j - 1] == "○":
                            win3 = (i - 1, j - 1, True)

                    if i + 3 < 15 and j + 3 < 15:
                        if board.matrix[i + 3][j + 3] == "○":
                            win3 = (i + 3, j + 3, True)

                    if i > 0 and j + 1 < 15:
                        if board.matrix[i - 1][j + 1] == "○":
                            win4 = (i - 1, j + 1, True)
                    if j > 2 and i + 3 < 15:
                        if board.matrix[i + 3][j - 3] == "○":
                            win4 = (i + 3, j - 3, True)

                    for k in range(0, 3):
                        if j + k < 15:
                            if board.matrix[i][j + k] != board.matrix[i][j]:
                                win1 = (-1, -1, False)
                        if i + k < 15:
                            if board.matrix[i + k][j] != board.matrix[i][j]:
                                win2 = (-1, -1, False)
                        if i + k < 15 and j + k < 15:
                            if board.matrix[i + k][j + k] != board.matrix[i][j]:
                                win3 = (-1, -1, False)
                        if j >= 2 and i + k < 15:
                            if board.matrix[i + k][j - k] != board.matrix[i][j]:
                                win4 = (-1, -1, False)

                    if win1[2] == True:
                        return [win1[0], win1[1]]
                    if win2[2] == True:
                        return [win2[0], win2[1]]
                    if win3[2] == True:
                        return [win3[0], win3[1]]
                    if win4[2] == True:
                        return [win4[0], win4[1]]

        for i in range(0, 15):
            for j in range(0, 15):
                if board.matrix[i][j] == ai.symbol:
                    win1 = win2 = win3 = win4 = (-1, -1, False)

                    if j > 0:
                        if board.matrix[i][j - 1] == "○":
                            win1 = (i, j - 1, True)

                    if j + 2 < 15:
                        if board.matrix[i][j + 2] == "○":
                            win1 = (i, j + 2, True)

                    if i > 0:
                        if board.matrix[i - 1][j] == "○":
                            win2 = (i - 1, j, True)

                    if i + 2 < 15:
                        if board.matrix[i + 2][j] == "○":
                            win2 = (i + 2, j, True)

                    if i > 0 and j > 0:
                        if board.matrix[i - 1][j - 1] == "○":
                            win3 = (i - 1, j - 1, True)

                    if i + 2 < 15 and j + 2 < 15:
                        if board.matrix[i + 2][j + 2] == "○":
                            win3 = (i + 2, j + 2, True)

                    if i > 0 and j + 1 < 15:
                        if board.matrix[i - 1][j + 1] == "○":
                            win4 = (i - 1, j + 1, True)
                    if j > 1 and i + 2 < 15:
                        if board.matrix[i + 2][j - 2] == "○":
                            win4 = (i + 2, j - 2, True)

                    for k in range(0, 2):
                        if j + k < 15:
                            if board.matrix[i][j + k] != board.matrix[i][j]:
                                win1 = (-1, -1, False)
                        if i + k < 15:
                            if board.matrix[i + k][j] != board.matrix[i][j]:
                                win2 = (-1, -1, False)
                        if i + k < 15 and j + k < 15:
                            if board.matrix[i + k][j + k] != board.matrix[i][j]:
                                win3 = (-1, -1, False)
                        if j >= 2 and i + k < 15:
                            if board.matrix[i + k][j - k] != board.matrix[i][j]:
                                win4 = (-1, -1, False)

                    if win1[2] == True:
                        return [win1[0], win1[1]]
                    if win2[2] == True:
                        return [win2[0], win2[1]]
                    if win3[2] == True:
                        return [win3[0], win3[1]]
                    if win4[2] == True:
                        return [win4[0], win4[1]]

        for i in range(3, 15):
            for j in range(3, 15):
                if board.matrix[i][j] == "○":
                    return [i, j]
        return -1, -1
    def move(self, ai, board):
        """
        Searches for the best move for a given state of the board
        :param ai: the computer
        :param board: the state of the board
        :return: the best move as a column number
        """
        next_move = self.find_computer_win_situation(ai, board)
        if next_move[0] == -1:
            next_move = self.find_human_win_situation(ai, board)
            if next_move[0] == -1:
                next_move = self.find_computer_move(ai, board)
                return next_move[0] + 1, next_move[1] + 1
            else:
                return next_move[0] + 1, next_move[1] + 1
        else:
            return next_move[0] + 1, next_move[1] + 1