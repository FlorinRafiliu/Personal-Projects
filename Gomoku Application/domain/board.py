class Board:
    def __init__(self):
        """
        Initializer for the Board class
        It contains a pseudo-matrix which memories the state of the board
        """
        self.matrix = [['○' for x in range(15)] for y in range(15)]

    def __str__(self):
        """
        :return: the configuration of the board as a string/board
        """
        string = '|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |\n'
        string += '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n'
        for index1 in range(15):
            if index1 + 1 < 10:
                string += '| ' + str(index1 + 1)
            else:
                string += '|' + str(index1 + 1)

            for index2 in range(15):
                string += ' | '
                string += str(self.matrix[index1][index2])
            string += ' |\n'
            string += '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n'
        return string