
# create array cube
def create_cube():
  cube_array = []
  for color in range(0, 6):
    side = []
    for row in range(0, 3):
      row_list = []
      for col in range(3):
        row_piece = [color, row, col]
        row_list.append(row_piece)
      side.append(row_list)
    cube_array.append(side)
  return cube_array

# display the cube by the corresponding letter
def display_cube_letter(array):
  white = array[0]
  orange = array[1]
  green = array[2]
  red = array[3]
  blue = array[4]
  yellow = array[5]

  sides = [orange, green, red, blue]

  for arr in white:
    line = "".join(letter for letter in arr)
    print(f"{line:>7}")

  sides = [["".join(item for item in side) for side in sublist] for sublist in sides]
  sides = [list(sublist) for sublist in zip(*sides)]
  sides = [" ".join(string) for string in sides]

  for side in sides:
    print(side)

  for arr in yellow:
    line = "".join(letter for letter in arr)
    print(f"{line:>7}")

# display cube array
def display_cube_arr(array):
  for side in array:
    for row in side:
      print(row)
    print()

# turn array into letter
def to_letter(array):
  colors = {
    0: "W", 1: "O", 2: "G",
    3: "R", 4: "B", 5: "Y"
  }

  for color in range(6):
    for row in range(3):
      for col in range(3):
        piece = array[color][row][col][0]
        piece = colors[piece]
        array[color][row][col] = piece
  return array
