from service import ScrambleService
from repository import Repository
from Tests import TestsScramble


class UI:
    def __init__(self, _service : ScrambleService):
        self.__service = _service

    def __swap(self, word1, letter1, word2, letter2):
        self.__service.swap(word1, letter1, word2, letter2, False)

    def __message(self):
        print("The scrambled sentence is: " + self.__service.scrambled + "  [score is: " + str(
            self.__service.score) + "]")

    def start_game(self):

        self.__service.start_new_game()
        print("\t\t<<<Welcome to Scramble! game>>>\n")

        while True:
            self.__message()
            conclusion = False

            while True:
                option = input(" <<< ")

                option = option.split()

                try:
                    if len(option) == 6 and option[0] == "swap" and option[3] == "-":
                        self.__swap(option[1], option[2], option[4], option[5])
                        break
                    elif len(option) == 1 and option[0] == "exit":
                        conclusion = True
                        break
                    elif len(option) == 1 and option[0] == "undo":
                        self.__service.undo()
                        break
                    else:
                        print("Invalid command")
                except ValueError as ve:
                    print(ve)

            if conclusion:
                break

            conclusion = self.__service.game_over()
            if conclusion != False:
                self.__message()
                print(conclusion)
                break

TestsScramble()
repo = Repository("input.txt")
service = ScrambleService(repo)
ui = UI(service)

ui.start_game()