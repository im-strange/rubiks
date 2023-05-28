
import re
import copy

import rubiks.moves as moves
import rubiks.processor as processor

class Cube:
  def __init__(self, cube_array=processor.create_cube()):
    self.cube_array = cube_array
    self.scramble_notations = None

  # simulate rotation F
  def turn_front(self):
    self.cube_array = moves.turn_front(self.cube_array)

  # simulate rotation F'
  def turn_front_prime(self):
    self.cube_array = moves.turn_front_prime(self.cube_array)

  # simulate rotation R'
  def turn_right_prime(self):
    self.cube_array = moves.turn_right_prime(self.cube_array)

  # simulate rotation R
  def turn_right(self):
    self.cube_array = moves.turn_right(self.cube_array)

  # simulate rotation L
  def turn_left(self):
    self.cube_array = moves.turn_left(self.cube_array)

  # simulate rotation L'
  def turn_left_prime(self):
    self.cube_array = moves.turn_left_prime(self.cube_array)

  # simulate rotation U
  def turn_up(self):
    self.cube_array = moves.turn_up(self.cube_array)

  # simulate rotation U'
  def turn_up_prime(self):
    self.cube_array = moves.turn_up_prime(self.cube_array)

  # simulate rotation D
  def turn_down(self):
    self.cube_array = moves.turn_down(self.cube_array)

  # simulate rotation D'
  def turn_down_prime(self):
    self.cube_array = moves.turn_down_prime(self.cube_array)

  # simulate rotation B
  def turn_back(self):
    self.cube_array = moves.turn_back(self.cube_array)

  # simulate rotation B'
  def turn_back_prime(self):
    self.cube_array = moves.turn_back_prime(self.cube_array)

  # display array using letters
  def display_letter(self):
    copy_arr = copy.deepcopy(self.cube_array)
    letter_array = processor.to_letter(copy_arr)
    processor.display_cube_letter(letter_array)

  # display array matrices
  def display_array(self):
    processor.display_cube_arr(self.cube_array)

  # scramble cube
  def scramble(self, notations):
    self.scramble_notations = notations
    notations = notations.split()
    rotate_twice = lambda function: (function(), function())

    number_in = lambda s: bool(re.search(r'\d', s))
    moves = {
      ("R", "R2"): self.turn_right,
      ("F", "F2"): self.turn_front,
      ("L", "L2"): self.turn_left,
      ("U", "U2"): self.turn_up,
      ("D", "D2"): self.turn_down,
      ("B", "B2"): self.turn_back,

      ("F'", "F'"): self.turn_front_prime,
      ("R'", "R'"): self.turn_right_prime,
      ("L'", "L'"): self.turn_left_prime,
      ("U'", "U'"): self.turn_up_prime,
      ("D'", "D'"): self.turn_down_prime,
      ("B'", "B'"): self.turn_back_prime
    }

    for notation in notations:
      for key in moves.keys():
        if notation in key:
          if number_in(notation):
            rotate_twice(moves[key])
          else: moves[key]()


if __name__ == "__main__":
  rubiks = Cube()
  rubiks.scramble("R U R' U' R' F R F'")
  rubiks.display_letter()
