from domain import Sentence


class Repository:
    def __init__(self, filename):
        self.__filename = filename
        self.__data = []

        #in case is not created
        f = open(filename, "a")
        f.close()

        self.__read_from_file()

    def __read_from_file(self):
        """
            Open, read and extract the sentences from the file
        """
        self.__data = []

        f = open(self.__filename, "r")

        lines = f.readlines()
        for line in lines:
            self.__data.append(Sentence(line.strip()))

        f.close()

    @property
    def data(self):
        """
            Getter for the list of <Sentence>
        :return: self.__data - list
        """
        return self.__data