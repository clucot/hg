# libraries


# custom imports
from fonctions import *
from donnees import *


#temp
user_score = 0
username = "Charlie"

#chargement list
list_words = []
list_words.append('salade')
list_words.append('Homme')
list_words.append('burger')

myWord = Word()
myWord.load_word("salade")

while not myWord.word_found :

    print("Essayez une lettre : ")
    lettre = input()

    myWord.guess(lettre)

    print(myWord.word_to_guess)



if __name__ == "__main__" :
    pass