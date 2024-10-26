from service import ScrambleService
from repository import Repository
from domain import Sentence
import unittest


class TestsScramble(unittest.TestCase):
    def test_file_repo(self):

        f = open("test1.txt", "w")
        f.write("magazie\n")
        f.write("Florin Rafiliu\n")
        f.write("Nota practic FP > 9:50\n")
        f.close()

        repo = Repository("test1.txt")
        sentences = repo.data

        self.assertEqual(len(sentences), 3, "The lines are not read well from the file!")
        self.assertEqual(sentences[0].sentence, "magazie")
        self.assertEqual(sentences[2].spaces, [4, 12, 15, 17])

    def test_service_start_new_game(self):
        repo = Repository("input.txt")
        service = ScrambleService(repo)

        service.start_new_game()

        sentences = []
        for i in repo.data:
            sentences.append(i.sentence)

        self.assertEqual(service.sentence.sentence in sentences, True)

    def test_service_game_over(self):
        repo = Repository("input.txt")
        service = ScrambleService(repo)

        service.set_sentence_and_scrambled_and_score_for_tests(Sentence("Florin"), "Flroin", 6)

        self.assertEqual(service.game_over(), False)

        service.swap(0, 2, 0, 3, False)
        self.assertEqual(service.game_over(), "You won! Your score is 5")

        service.swap(0, 2, 0, 3, False)
        service.swap(0, 2, 0, 3, False)
        service.swap(0, 2, 0, 3, False)
        service.swap(0, 2, 0, 3, False)
        service.swap(0, 2, 0, 3, False)
        self.assertEqual(service.game_over(), "You lose :((( !")

    def test_service_swap(self):
        repo = Repository("input.txt")
        service = ScrambleService(repo)

        service.set_sentence_and_scrambled_and_score_for_tests(Sentence("Florin Rafiliu"), "Florin Rafiliu", 12)

        service.swap(0, 1, 1, 1, False)
        self.assertEqual(service.score, 11)
        self.assertEqual(service.scrambled.strip(), "Faorin Rlfiliu")

        service.swap(0, 1, 1, 1, True)
        self.assertEqual(service.score, 11)
        self.assertEqual(service.scrambled.strip(), "Florin Rafiliu")

    def test_validate(self):
        repo = Repository("input.txt")
        service = ScrambleService(repo)

        service.set_sentence_and_scrambled_and_score_for_tests(Sentence("Florin Rafiliu"), "Florin Rafiliu", 12)

        try:
            service.swap(0, 0, 1, 0, False)
        except ValueError as ve:
            self.assertEqual(str(ve), "Index for the first letter exceed the limits!\nIndex for the second letter exceed the limits!\n")
        else:
            self.assertEqual(False, True)

        try:
            service.swap(0, -1, 1, 0, False)
        except ValueError as ve:
            self.assertEqual(str(ve), "Index for the first letter exceed the limits!\nIndex for the second letter exceed the limits!\n")
        else:
            self.assertEqual(False, True)

        try:
            service.swap(0, 0, 1, 6, False)
        except ValueError as ve:
            self.assertEqual(str(ve), "Index for the first letter exceed the limits!\nIndex for the second letter exceed the limits!\n")
        else:
            self.assertEqual(False, True)

        try:
            service.swap(-1, -1, 2, 0, False)
        except ValueError as ve:
            self.assertEqual(str(ve), "Index for the first word exceed the limits!\nIndex for the second word exceed the limits!\n")
        else:
            self.assertEqual(False, True)

        try:
            service.swap(0, -1, 2, 0, False)
        except ValueError as ve:
            self.assertEqual(str(ve), "Index for the first letter exceed the limits!\nIndex for the second word exceed the limits!\n")
        else:
            self.assertEqual(False, True)

        try:
            service.swap(0, 0, 1, 1, False)
        except ValueError as ve:
            self.assertEqual(str(ve), "Index for the first letter exceed the limits!\n")
        else:
            self.assertEqual(False, True)

        try:
            service.swap(0, 1, 1, 6, False)
        except ValueError as ve:
            self.assertEqual(str(ve), "Index for the second letter exceed the limits!\n")
        else:
            self.assertEqual(False, True)

        try:
            service.swap("a", 1, 1, 6, False)
        except ValueError as ve:
            self.assertEqual(str(ve), "Invalid input! (the indexes must be integers)")
        else:
            self.assertEqual(False, True)

        try:
            service.swap(1, 1, 1, "a", False)
        except ValueError as ve:
            self.assertEqual(str(ve), "Invalid input! (the indexes must be integers)")
        else:
            self.assertEqual(False, True)

    def test_undo(self):
        repo = Repository("input.txt")
        service = ScrambleService(repo)

        service.set_sentence_and_scrambled_and_score_for_tests(Sentence("Florin Rafiliu"), "Florin Rafiliu", 12)

        service.swap(0, 1, 1, 1, False)
        service.undo()
        self.assertEqual(service.scrambled.strip(), "Florin Rafiliu")
        self.assertEqual(service.score, 11)

        service.undo()
        self.assertEqual(service.scrambled.strip(), "Faorin Rlfiliu")
        self.assertEqual(service.score, 11)
