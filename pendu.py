# libraries
import random as rd
import time

# custom imports
from fonctions import Word, ScoreManager, clear_prompt
from donnees import *


class HangingGame:
    """
    Class HangingGame manage the hanging game process
    """

    def __init__(self, score_file_path: str, max_tries_per_word: int = 8) -> None:
        """
        :param score_file_path: File path of players score (will be created if it does not exist)
        :param max_tries_per_word: Number of fails allowed to user to guess the word, defaults to 8
        """
        self.max_tries = max_tries_per_word

        self.blank_answer = ""
        self.user_name = ""
        self.user_score = 0
        self.tries_left = 0

        self.sm_obj = ScoreManager(score_file_path)
        self.word_obj = Word()

        self.enum_yes_answer = {"y", "Y", "o", "O"}
        self.enum_no_answer = {"n", "N"}

    def display_intro(self) -> None:
        """
        Display game intro like :\n
        ---------- Jeu du pendu ----------
        """
        print("---------- Jeu du pendu ----------")

    def display_game_state(self) -> None:
        """
        Display information needed at each round : Hidden word, tries left, tried letters
        """
        clear_prompt()
        print("Mot à deviner : " + self.word_obj.get_hidden_word)
        print(str(self.tries_left) + " coup(s) restant(s)")

        # Display letters already tried if list is not empty
        if self.word_obj.get_tried_letters != []:
            print("Lettres déjà jouées : ")
            print(self.word_obj.get_tried_letters)

    def display_user_score(self) -> None:
        """
        Update and display the name and the score of the current user\n
        user_name has to be filled
        """
        clear_prompt()
        self.user_score = self.sm_obj.get_score(self.user_name)
        print(self.user_name + ", votre score est de " + str(self.user_score))
        time.sleep(2)

    def ask_name(self) -> None:
        """
        Ask for user name and save it as self.user_name
        """
        print("Nom du joueur : ")
        self.user_name = input()

    def ask_letter(self) -> str:
        """
        Ask the user to enter a letter\n
        Return the letter or a self.blank_answer if entry is incorrect

        :return: A letter or a blank str (str)
        """
        print("Essayez une lettre : ")
        letter = input()

        # Check if the entry is just a letter
        if (len(letter) == 1) and (letter.isalpha()):
            return letter
        else:
            return self.blank_answer

    def ask_play_again(self) -> bool:
        """
        Ask the user if he wants to play again. Ask again if entry is incorrect

        :return: True if yes, False if not (bool)
        """
        while True:

            clear_prompt()
            print("Souhaitez-vous rejouer ? o/n")

            answer = input()
            if answer in self.enum_yes_answer:
                return True

            elif answer in self.enum_no_answer:
                return False

            else:
                print("Entrez une valeur valide svp")
                time.sleep(1)

    def pick_a_word(self) -> None:
        """
        Pick a random word in list_words and load word_obj with it
        """
        chosen_word = rd.choice(list_words)
        self.word_obj.load_clear_word(chosen_word.lower())

    def save_score(self) -> None:
        """
        Update and save score into score file
        """
        self.sm_obj.update_ranking(self.user_name, self.user_score)
        self.sm_obj.save()

    def update_score(self) -> None:
        """
        Update user score with tries left
        """
        self.user_score += self.tries_left

    def play(self) -> None:
        """
        Main function
        """
        self.display_intro()
        self.ask_name()
        self.display_user_score()

        # While loop to play until user is over
        while True:

            self.pick_a_word()

            # Run game until word is getting found or user goes out of tries
            self.tries_left = self.max_tries
            while (not self.word_obj.is_word_found()) and (self.tries_left != 0):

                self.display_game_state()

                letter = self.ask_letter()

                # if letter is void or invalid, continue to ask the user again
                if letter == self.blank_answer:
                    continue

                # If letter is not in the word, decrease self.tries_left
                if self.word_obj.guess(letter.lower()) == False:
                    self.tries_left -= 1

            self.update_score()
            self.save_score()
            self.display_user_score()

            # Only way to stop 'while loop' playing
            if self.ask_play_again() is False:
                break


if __name__ == "__main__":
    hanging_game = HangingGame(
        score_file_path=scores_fpath, max_tries_per_word=MAX_TRIES
    )
    hanging_game.play()
