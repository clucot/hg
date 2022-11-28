


class Word:
    '''
    
    '''
    def __init__(self):

        self.word_picked    = ""
        self.word_to_guess  = ""
        self.carac_to_guess = "*"
        self.tried_letters  = []

        self.word_len       = 0

        self.word_found     = False


    def load_word(self, new_word):
        
        self.reset_word()

        self.word_picked = new_word

        self.word_len = len(self.word_picked)

        for i in range (self.word_len):
            self.word_to_guess += self.carac_to_guess



    def guess(self, letter):
        # protéger l'entrée ?
        # pas optimiser mais facile à lire
        if letter in self.word_picked :

            tmp_word = ""

            for i in range(self.word_len) :

                if letter == self.word_picked[i]:
                    tmp_word += letter
                else :
                    tmp_word += self.word_to_guess[i]

            self.word_to_guess = tmp_word

            return True

        else :
            # Append 
            self.tried_letters.append(letter)
            return False

    def reset_word(self):
        
        self.tried_letters = []
        self.word_to_guess = ""

    # @property
    # def 

