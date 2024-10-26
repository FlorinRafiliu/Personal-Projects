class AI:
    def __init__(self, symbol, human_symbol):
        """
        :param symbol: the symbol used by the computer
        :param human_symbol: the symbol used by the human
        """
        self.__symbol = symbol
        self.__human_symbol = human_symbol
    @property
    def human_symbol(self):
        """
            Getter for the human_symbol attribute
        """
        return self.__human_symbol
    @property
    def symbol(self):
        """
        Getter for the symbol attribute
        """
        return self.__symbol

    def __str__(self):
        return "The computer is playing with this symbol: " + self.symbol