from repository import Repository
from random import *
class ScrambleService:
    def __init__(self, repo : Repository):
        self.__repo = repo
        self.__sentence = None
        self.__scrambled = ""
        self.__score = 0
        self.__last_operation = 0

    def scramble_sentence(self):
        """
            Create a scrambled version of the correct sentence of the game
                - extract the letters that are not first/last in the word and also not spaces
                - shuffle them
                - put them randomly in an <scrambled_sentence> variable
        :return: scrambled_sentence - str
        """
        spaces = self.__sentence.spaces
        sentence = self.__sentence.sentence

        letters = []
        for i in range(1, len(sentence)-1):
            if sentence[i] != " " and sentence[i-1] != " " and sentence[i+1] != " ":
                letters.append(sentence[i])

        shuffle(letters)

        scrambled_sentence = sentence[0]
        for i in range(1, len(sentence)-1):
            if i in spaces:
                scrambled_sentence = scrambled_sentence + " "
            elif sentence[i-1] == " " or sentence[i+1] == " ":
                scrambled_sentence = scrambled_sentence + sentence[i]
            else:
                scrambled_sentence = scrambled_sentence + letters.pop()
        scrambled_sentence = scrambled_sentence + sentence[len(sentence)-1]

        return scrambled_sentence

    def start_new_game(self):
        """
            Prepare the data for a new game of Scramble!:
                - randomly choose a sentence from the repo
                - scramble it
                - initialize the score of the game
        """
        no_of_sentence = len(self.__repo.data)
        self.__sentence = self.__repo.data[randint(0, no_of_sentence - 1)]
        self.__scrambled = self.scramble_sentence()
        self.__score = len(self.__scrambled) - len(self.__sentence.spaces)

    def __validate(self, word1, letter1, word2, letter2):
        """
            Validate the parameters for a later swap
        :param word1: str (the index of the first word from the sentence)
        :param letter1: str (the index of the first letter from the word)
        :param word2: str (the index of the second word from the sentence)
        :param letter2: str (the index of the second letter from the word)
        :raises: ValueError msg:
                    - "Invalid input! (the indexes must be integers)" : if the parameters not in fact integers
                    - "Index for the first word exceed the limits!\n"
                    - "Index for the second word exceed the limits!\n" : if index of the word is not in bounded limits of the
                                                                      numbers of words
                    - "Index for the first letter exceed the limits!\n"
                    - "Index for the second letter exceed the limits!\n" : if index of the letter is not in bounded limits of the
                                                                      numbers of words
        """
        try:
            word1 = int(word1)
            word2 = int(word2)
            letter2 = int(letter2)
            letter1 = int(letter1)
        except:
            raise ValueError("Invalid input! (the indexes must be integers)")

        errors = ""
        words = self.__scrambled.split()
        if not 0 <= word1 < len(words):
            errors += "Index for the first word exceed the limits!\n"
        elif not 1 <= letter1 < len(words[word1])-1:
            errors += "Index for the first letter exceed the limits!\n"

        if not 0 <= word2 < len(words):
            errors += "Index for the second word exceed the limits!\n"
        elif not 1 <= letter2 < len(words[word2])-1:
            errors += "Index for the second letter exceed the limits!\n"

        if errors != "":
            raise ValueError(errors)
    def undo(self):
        """
            Make an undo of last operation if possible by re-swapping the last operation
        :raise: ValueError msg:
                    - "You need first to make an operation, so that you can undo it!" : if it is the first command made in the game
        """
        if self.__last_operation == 0:
            raise ValueError("You need first to make an operation, so that you can undo it!")

        self.swap(self.__last_operation[0], self.__last_operation[1], self.__last_operation[2], self.__last_operation[3], True)

    def swap(self, word1, letter1, word2, letter2, undo):
        """
            Swap the letter from index <letter1> from word of index <word1> with the letter
                from index <letter2> from word of index <word2>
        :param word1: int
        :param letter1: int
        :param word2: int
        :param letter2: int
        :param undo: bool - False: the swap is made by the user
                          - True: the swap is made by the <undo> function
        :raises: that one made by <validate> function
        """
        self.__validate(word1, letter1, word2, letter2)

        self.__last_operation = [word1, letter1, word2, letter2]
        words = self.__scrambled.split()

        word1 = int(word1)
        word2 = int(word2)
        letter2 = int(letter2)
        letter1 = int(letter1)

        letter11 = words[word1][letter1]
        letter22 = words[word2][letter2]
        word1 = words[word1]
        word2 = words[word2]
        ans = ""
        for word in words:
            for j in range(0, len(word)):
                if word != word1 and word2 != word:
                    ans = ans + word[j]
                elif word1 == word and word2 != word:
                    if j == letter1:
                        ans = ans + letter22
                    else:
                        ans = ans + word[j]
                elif word2 == word and word1 != word:
                    if j == letter2:
                        ans = ans + letter11
                    else:
                        ans = ans + word[j]
                else:
                    if j == letter1:
                        ans = ans + letter22
                    elif j == letter2:
                        ans = ans + letter11
                    else:
                        ans = ans + word[j]
            ans = ans + " "

        if undo == False:
            self.__score -= 1
        self.__scrambled = ans

    def game_over(self):
        """
            Checks if the game is finished
                - The scrambled version of the sentence is equivalent with the correct one
        :return: - "You won! Your score is " + str(self.__score) - The scrambled version of the sentence is equivalent
                                                                 with the correct one
                 - "You lose :((( !" - The score becomes 0, so no more operation
                 - False - the game is not yet over :))
        """
        if self.__scrambled.strip() == self.__sentence.sentence.strip():
            return "You won! Your score is " + str(self.__score)
        if self.__score == 0:
            return "You lose :((( !"
        return False

    @property
    def scrambled(self):
        """
            Getter for scrambled version of the sentence
        :return: str
        """
        return self.__scrambled
    @property
    def score(self):
        """
            Getter for the score
        :return: int
        """
        return self.__score
    @property
    def sentence(self):
        return self.__sentence
    def set_sentence_and_scrambled_and_score_for_tests(self, sentence, scrambled, score):
        self.__sentence = sentence
        self.__scrambled = scrambled
        self.__score = score