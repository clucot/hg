# libraries
import random as rd
import time

# custom imports
from fonctions import *
from donnees import *


# Intro
print("---------- Jeu du pendu ----------")
print("Nom du joueur : ")
username = input()


# Identify the player and get his score
sm = ScoreManager(scores_fp)
user_score = sm.get_score(username)

print(username + ", votre dernier score est de " + str(user_score))
sm.update_ranking(username, user_score)


time.sleep(2)


# Create word object
myWord = Word()


# Infinite loop
while True:

    # Pick a random word in list and load Word object with it
    chosen_word = rd.choice(list_words)
    myWord.load_word(chosen_word.lower())

    # Loop until word is found or tries_left == 0
    tries_left = MAX_TRIES
    while not myWord.is_word_found() and tries_left:

        clear_prompt()

        print("Mot à deviner : " + myWord.word_to_guess + "\n")
        print(str(tries_left) + " coup(s) restant(s)")

        # Display letters already tried if list is not empty
        if myWord.tried_letters != []:
            print("Lettres déjà jouées : ")
            print(myWord.tried_letters)

        print("\nEssayez une lettre : ")
        letter = input()

        # if input is something else than a single letter, just ignore
        if (len(letter) != 1) or (letter.isalpha() is False):
            continue

        # If letter is wrong, decrease tries_left
        if myWord.guess(letter.lower()) == False:
            tries_left -= 1

    # Increase score and save it into file
    user_score += tries_left
    sm.update_ranking(username, user_score)
    sm.save()

    #
    clear_prompt()
    print("Dernier score : " + str(user_score))
    print("Rejouer ? y/n")
    answer = input()
    if answer == "n":
        break


if __name__ == "__main__":
    pass
