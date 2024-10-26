

class Sentence:
    def __init__(self, sentence):
        self.__sentence = sentence
        self.__spaces = self.__getspaces(sentence)

    def __getspaces(self, sir):
        ans = []
        for i in range(0, len(sir)):
            if sir[i] == " ":
                ans.append(i)
        return ans

    @property
    def sentence(self):
        return self.__sentence
    @property
    def spaces(self):
        return self.__spaces
    def __str__(self):
        return self.sentence