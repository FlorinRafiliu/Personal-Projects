class Player:
    def __init__(self, name, symbol):
        """
        :param name: the name of the player
        :param symbol: the symbol of the player
        """
        self.__name = name
        self.__symbol = symbol

    @property
    def symbol(self):
        """
        Getter for the symbol attribute
        """
        return self.__symbol

    @property
    def name(self):
        """
        Getter for the name attribute
        """
        return self.__name

    def __str__(self):
        return self.name + " is playing with symbol: " + self.symbol
