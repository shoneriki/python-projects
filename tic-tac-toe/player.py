import math
import random

class Player:
  def __init__(self, letter):
  # letter = x or o
  self.letter = letter

  # next move
  def get_move(self, game):
    pass

class RandomComputerPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)

  def get_move(self, game):
    square = random.choice(game.available_moves())
    return square

class HumanPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)

  def get_move(self, game):
    
