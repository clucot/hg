


class Word():
    '''
    
    '''
    def __init__(self):

        self.word_picked    = ""
        self.word_to_guess  = ""
        self.carac_to_guess = "*"
        self.tried_letters  = []

        self.word_len       = 0

        pass

    def load_word(self):
        
        

        self.word_len = len(self.word_picked)

        pass

    def guess(self, letter):
        # protéger l'entrée ?
        # pas optimiser mais facile à lire
        if letter in self.word_picked :

            for i in range(self.word_len) :
                if letter == self.word_picked[i]:
                    self.word_to_guess[i] = letter
            return True

        else :
            # Append 
            self.tried_letters.append(letter)
            return False

    def reset_word(self):


        pass

    # @property
    # def 

