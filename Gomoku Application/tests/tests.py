import unittest

from src.domain.ai import AI
from src.domain.player import Player
from src.domain.board import Board
from src.services.gameservices import AIService, BoardService

class Tests(unittest.TestCase):

    def test_board(self):
        symbol1 = "🅧"
        symbol2 = "🅥"
        board = Board()
        board_service = BoardService()
        self.assertEqual(board.matrix[0][1], '○')
        self.assertEqual(str(board), "|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |\n" +
                                            "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                            "| 1 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                            "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                            "| 2 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                     "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                     "| 3 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                     "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                     "| 4 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                     "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                     "| 5 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                     "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                     "| 6 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                     "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                     "| 7 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                     "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                     "| 8 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                     "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                     "| 9 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                     "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                     "|10 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                     "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                     "|11 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                     "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                     "|12 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                     "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                     "|13 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                     "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                     "|14 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                     "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+
                                     "|15 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |\n"+
                                     "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

        board_service.move(board, symbol1, 1, 1)
        board_service.move(board, symbol1, 2, 2)
        self.assertEqual(board_service.is_game_won(board), False)
        board_service.move(board, symbol1, 3, 3)
        board_service.move(board, symbol1, 4, 4)
        self.assertEqual(board_service.is_game_won(board), False)
        board_service.move(board, symbol1, 5,5)
        self.assertEqual(board_service.is_game_won(board), True)

        board2 = Board()
        board_service.move(board2, symbol1, 1, 1)
        board_service.move(board2, symbol1, 1, 2)
        board_service.move(board2, symbol2, 1, 3)
        board_service.move(board2, symbol1, 1, 4)
        board_service.move(board2, symbol1, 1, 5)
        self.assertEqual(board_service.is_game_won(board2), False)

        board3 = Board()
        board_service.move(board3, symbol2, 5, 1)
        board_service.move(board3, symbol2, 6, 1)
        board_service.move(board3, symbol2, 7, 1)
        board_service.move(board3, symbol2, 8, 1)
        board_service.move(board3, symbol2, 9, 1)
        self.assertEqual(board_service.is_game_won(board3), True)

        board4 = Board()
        board_service.move(board4, symbol1, 10, 3)
        board_service.move(board4, symbol1, 10, 4)
        board_service.move(board4, symbol1, 10, 5)
        board_service.move(board4, symbol1, 10, 6)
        board_service.move(board4, symbol1, 10, 7)
        self.assertEqual(board_service.is_game_won(board4), True)

        board5 = Board()
        board_service.move(board5, symbol2, 7, 7)
        board_service.move(board5, symbol2, 8, 6)
        board_service.move(board5, symbol2, 9, 5)
        board_service.move(board5, symbol2, 10,4)
        board_service.move(board5, symbol2, 11,3)
        self.assertEqual(board_service.is_game_won(board5), True)

    def test_player(self):
        player1 = Player("Alina", "X")
        player2 = Player("Elena", "Y")
        self.assertEqual(player1.name, 'Alina')
        self.assertEqual(player2.symbol, "Y")
        self.assertEqual(str(player1), "Alina is playing with symbol: X")

    def test_AI(self):
        symbol1 = "🅧"
        symbol2 = "🅥"
        player1 = Player("Alina", symbol1)
        player2 = AI(symbol2, player1.symbol)
        self.assertEqual(str(player2), "The computer is playing with this symbol: " + player2.symbol)

    def test_aiservice(self):
        symbol1 = "🅧"
        symbol2 = "🅥"
        player1 = Player("Alina", symbol1)
        player2 = AI(symbol2, player1.symbol)
        board = Board()
        board_service = BoardService()
        ai_service = AIService()

        board_service.move(board, player1.symbol, 1, 1)
        board_service.move(board, player1.symbol, 2, 2)
        board_service.move(board, player1.symbol, 3, 3)
        board_service.move(board, player1.symbol, 4, 4)
        x, y = ai_service.move(player2, board)
        x -= 1
        y -= 1
        self.assertEqual(x, 5)
        self.assertEqual(y, 5)

        board1 = Board()
        board_service.move(board1, player1.symbol, 1, 1)
        board_service.move(board1, player1.symbol, 1, 2)
        board_service.move(board1, player1.symbol, 1, 3)
        board_service.move(board1, player1.symbol, 1, 4)
        x, y = ai_service.move(player2, board1)
        x -= 1
        y -= 1
        self.assertEqual(x, 1)
        self.assertEqual(y, 5)

        board2 = Board()
        board_service.move(board2, player1.symbol, 1, 5)
        board_service.move(board2, player1.symbol, 2, 4)
        board_service.move(board2, player1.symbol, 3, 3)
        board_service.move(board2, player1.symbol, 4, 2)
        x, y = ai_service.move(player2, board2)
        x -= 1
        y -= 1
        self.assertEqual(x, 5)
        self.assertEqual(y, 1)

        board3 = Board()
        board_service.move(board3, player1.symbol, 1, 1)
        board_service.move(board3, player1.symbol, 2, 1)
        board_service.move(board3, player1.symbol, 3, 1)
        board_service.move(board3, player1.symbol, 4, 1)
        x, y = ai_service.move(player2, board3)
        x -= 1
        y -= 1
        self.assertEqual(x, 5)
        self.assertEqual(y, 1)

        board4 = Board()
        board_service.move(board4, player1.symbol, 2, 2)
        board_service.move(board4, player1.symbol, 3, 3)
        board_service.move(board4, player1.symbol, 4, 4)
        x, y = ai_service.move(player2, board4)
        x -= 1
        y -= 1
        self.assertEqual(x, 1)
        self.assertEqual(y, 1)

        board5 = Board()
        board_service.move(board5, player1.symbol, 2, 2)
        board_service.move(board5, player1.symbol, 2, 3)
        board_service.move(board5, player1.symbol, 2, 4)
        x, y = ai_service.move(player2, board5)
        x -= 1
        y -= 1
        self.assertEqual(x, 2)
        self.assertEqual(y, 1)

        board6 = Board()
        board_service.move(board6, player1.symbol, 2, 2)
        board_service.move(board6, player1.symbol, 3, 2)
        board_service.move(board6, player1.symbol, 4, 2)
        x, y = ai_service.move(player2, board6)
        x -= 1
        y -= 1
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)

        board7 = Board()
        board_service.move(board7, player1.symbol, 2, 5)
        board_service.move(board7, player1.symbol, 3, 4)
        board_service.move(board7, player1.symbol, 4, 3)
        x, y = ai_service.move(player2, board7)
        x -= 1
        y -= 1
        self.assertEqual(x, 1)
        self.assertEqual(y, 6)


