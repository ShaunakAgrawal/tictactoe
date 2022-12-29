import math 
import random

#base player class
class Player : 
    def __init__(self,letter):
        # the letter can be X or O
        self.letter = letter

    #we want player to get their move in the game
    def get_move(self,game):
        pass
#computer player
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass
#human player
class HumanPLayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass


    