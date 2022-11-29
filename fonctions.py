from os import system, name
import pickle as pk


class Word:
    """
    Word class containing the word to guess
    """

    def __init__(self):

        self.__word_picked = ""
        self._word_to_guess = ""
        self.carac_to_guess = "*"
        self._tried_letters = []

        self.word_len = 0

    def load_word(self, new_word: str):
        """Load a new word and fill the unknown one"""
        self.__reset_word()

        self.__word_picked = new_word

        self.word_len = len(self.__word_picked)

        # Fill the unknown word with *****
        for i in range(self.word_len):
            self._word_to_guess += self.carac_to_guess

    def guess(self, letter: str):
        """
        Description

        :param letter:

        :return:
        """

        if letter in self.__word_picked:

            tmp_word = ""

            # Rebuild the self._word_to_guess with * or found letter
            for i in range(self.word_len):

                if letter == self.__word_picked[i]:
                    tmp_word += letter
                else:
                    tmp_word += self._word_to_guess[i]

            self._word_to_guess = tmp_word

            return True

        else:
            # Append to list of already tried letters
            self._tried_letters.append(letter)
            return False

    def is_word_found(self):
        """Return True or False if the word has been discovered"""
        if self._word_to_guess == self.__word_picked:
            return True
        else:
            return False

    def __reset_word(self):
        """
        Reset
        """
        self._tried_letters = []
        self._word_to_guess = ""

    @property
    def word_to_guess(self):
        return self._word_to_guess

    @property
    def tried_letters(self):
        return self._tried_letters


class ScoreManager:
    """
    Class which handle and manage score file
    """

    def __init__(self, file_path):

        self.score_fp = file_path

        self.__handler_file = None
        self.dict_ranking = {}

        self.__check_file()
        self.load_ranking()

    def __check_file(self):
        """
        Check if the file exists or create it
        """
        try:
            with open(self.score_fp, "rb") as self.__handler_file:
                pass

        except FileNotFoundError:
            with open(self.score_fp, "wb") as self.__handler_file:
                # Have to fill a bit the file to make the pickle work
                pk.dump({".": 0}, self.__handler_file)

    def load_ranking(self) -> None:
        """
        Load ranking dictionary contained in score file
        """
        with open(self.score_fp, "rb") as self.__handler_file:

            self.dict_ranking = pk.load(self.__handler_file)

    def save(self) -> None:
        """
        Save ranking dictionary into score file
        """
        with open(self.score_fp, "wb") as self.__handler_file:

            pk.dump(self.dict_ranking, self.__handler_file)

    def update_ranking(self, username, score):
        """
        Add or update dict_ranking username and score
        """
        self.dict_ranking[username] = score

    def get_score(self, username):
        """
        Looking for a user's score
        Return 0 if does not exist
        """
        try:
            return self.dict_ranking[username]

        except KeyError:
            return 0

        except:
            return 0


def clear_prompt() -> None:
    """Clear the prompt for windows, mac or linux"""
    # for windows
    if name == "nt":
        system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        system("clear")
