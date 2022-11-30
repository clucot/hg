from os import system, name
import pickle as pk


class Word:
    """
    Word class is managing the word to be guessed by the user for hanging game purpose\n
    It contains the clear_word to be guessed, the letters already tried by the user, the hiding character '*' and the word hidden by the '*'
    """

    def __init__(self) -> None:

        self.clear_word = ""
        self._hidden_word = ""
        self.hiding_char = "*"
        self._tried_letters = []

        self.word_length = 0

    def load_clear_word(self, new_word: str):
        """
        Load the new word to be guessed by the user in self.clear_word\n
        Also, reset private attributes, save the word length in self.word_length and fill self._hidden_word with '*'

        :param new_word: The new word to be guessed by the user

        """
        # Reset class attributes
        self._reset_word()

        # Load word and save length
        self.clear_word = new_word
        self.word_length = len(self.clear_word)

        # Fill the _hidden_word with the exact number of '*'
        for i in range(self.word_length):
            self._hidden_word += self.hiding_char

    def guess(self, letter: str) -> bool:
        """
        Guess method where the user try to guess clear_word by proposing a letter

        :param letter: The letter tried by the user to guess the word

        :return: True if letter is the word, False otherwise (bool)
        """

        if letter in self.clear_word:

            temporary_word = ""

            # Rebuild the self._hidden_word with * or found letter
            for i in range(self.word_length):

                if letter == self.clear_word[i]:
                    temporary_word += letter
                else:
                    temporary_word += self._hidden_word[i]

            self._hidden_word = temporary_word

            return True

        else:
            # Append to list of already tried letters
            self._tried_letters.append(letter)
            return False

    def is_word_found(self) -> bool:
        """
        Compare _hidden_word and clear_word to know if all letters have been discovered

        :return: True if discovered, False otherwise (bool)
        """
        if self._hidden_word == self.clear_word:
            return True
        else:
            return False

    def _reset_word(self) -> None:
        """
        Reset private attributes _tried_letters and _hidden_word
        """
        self._tried_letters = []
        self._hidden_word = ""

    @property
    def hidden_word(self) -> str:
        return self._hidden_word

    @property
    def tried_letters(self) -> list:
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
