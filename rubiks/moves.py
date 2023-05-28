
import copy
import rubiks.processor as processor

# available notations:
# 1) F      2) R
# 3) L      4) U
# 5) D      6) B
# 7) F'     8) R'
# 9) L'     10) U'
# 11) B'    12) D'

# turn a color array clockwise
def clockwise(sub_array, rotation=1):
  new_array = sub_array
  for rotation in range(rotation):
    new_array = [list(piece) for piece in zip(
      new_array[2], new_array[1], new_array[0])]
  return new_array

# turn a color array counter clockwise
def counter_clockwise(sub_array):
  new_array = copy.deepcopy(sub_array)
  for rotation in range(3):
    new_array = clockwise(new_array)
  return new_array

# simulate rotation F
def turn_front(cube_array):
  temp_arr = copy.deepcopy(cube_array)
  white_arr = copy.deepcopy(cube_array[0])
  orange_arr = copy.deepcopy(cube_array[1])
  green_arr = copy.deepcopy(cube_array[2])
  red_arr = copy.deepcopy(cube_array[3])
  blue_arr = copy.deepcopy(cube_array[4])
  yellow_arr = copy.deepcopy(cube_array[5])

  # white
  white_sub_arr = [list(sublist) for sublist in zip(
    orange_arr[0], orange_arr[1], orange_arr[2])][2]
  white_sub_arr.reverse()
  cube_array[0][2] = white_sub_arr

  # orange
  for index in range(3):
    cube_array[1][index][2] = yellow_arr[0][index]

  # green
  green_left_arr = [list(sublist) for sublist in zip(
    green_arr[0], green_arr[1], green_arr[2])][0]
  green_left_arr.reverse()
  cube_array[2][0] = green_left_arr

  green_right_arr = [list(sublist) for sublist in zip(
    green_arr[0], green_arr[1], green_arr[2])][2]
  green_right_arr.reverse()
  cube_array[2][2] = green_right_arr

  cube_array[2][1][0] = green_arr[2][1]
  cube_array[2][1][2] = green_arr[0][1]

  # red
  for index in range(3):
    cube_array[3][index][0] = white_arr[2][index]

  # yellow
  for index in range(3):
    cube_array[5][0][index] = temp_arr[3][index][0]
  cube_array[5][0].reverse()

  return cube_array

# simulate rotation R
def turn_right(cube_array):
  temp_arr = copy.deepcopy(cube_array)
  white_arr = copy.deepcopy(cube_array[0])
  orange_arr = copy.deepcopy(cube_array[1])
  green_arr = copy.deepcopy(cube_array[2])
  red_arr = copy.deepcopy(cube_array[3])
  blue_arr = copy.deepcopy(cube_array[4])
  yellow_arr = copy.deepcopy(cube_array[5])

  # white
  white_sub_array = [list(sublist) for sublist in zip(
    green_arr[0], green_arr[1], green_arr[2])][2]
  for index in range(3):
    cube_array[0][index][2] = white_sub_array[index]

  # green
  green_sub_array = [list(sublist) for sublist in zip(
    yellow_arr[0], yellow_arr[1], yellow_arr[2])][2]
  for index in range(3):
    cube_array[2][index][2] = green_sub_array[index]

  # blue
  blue_sub_array = [list(sublist) for sublist in zip(
    white_arr[2], white_arr[1], white_arr[0])][2]
  for index in range(3):
    cube_array[4][index][0] = blue_sub_array[index]

  # yellow
  yellow_sub_array = [list(sublist) for sublist in zip(
    blue_arr[2], blue_arr[1], blue_arr[0])][0]
  for index in range(3):
    cube_array[5][index][2] = yellow_sub_array[index]

  # red
  new_array = copy.deepcopy(cube_array)
  new_array = [
    new_array[0],
    new_array[2],
    new_array[3],
    new_array[4],
    new_array[1],
    new_array[5]
  ]
  new_array = turn_front(new_array)
  new_red_array = new_array[2]
  cube_array[3] = new_red_array

  return cube_array

# simulate rotation L
def turn_left(cube_array):
  temp_arr = copy.deepcopy(cube_array)
  white_arr = copy.deepcopy(cube_array[0])
  orange_arr = copy.deepcopy(cube_array[1])
  green_arr = copy.deepcopy(cube_array[2])
  red_arr = copy.deepcopy(cube_array[3])
  blue_arr = copy.deepcopy(cube_array[4])
  yellow_arr = copy.deepcopy(cube_array[5])

  # white
  white_sub_array = [list(sublist) for sublist in zip(
    blue_arr[2], blue_arr[1], blue_arr[0])][2]
  for index in range(3):
    cube_array[0][index][0] = white_sub_array[index]

  # green
  green_sub_array = [list(sublist) for sublist in zip(
    white_arr[0], white_arr[1], white_arr[2])][0]
  for index in range(3):
    cube_array[2][index][0] = green_sub_array[index]

  # yellow
  yellow_sub_array = [list(sublist) for sublist in zip(
    green_arr[0], green_arr[1], green_arr[2])][0]
  for index in range(3):
    cube_array[5][index][0] = yellow_sub_array[index]

  # blue
  blue_sub_array = [list(sublist) for sublist in zip(
    yellow_arr[2], yellow_arr[1], yellow_arr[0])][0]
  for index in range(3):
    cube_array[4][index][2] = blue_sub_array[index]

 # orange
  new_array = [
    temp_arr[0],
    temp_arr[4],
    temp_arr[1],
    temp_arr[2],
    temp_arr[3],
    temp_arr[5]
  ]
  new_array = turn_front(new_array)
  rotated_orange_arr = new_array[2]
  cube_array[1] = rotated_orange_arr

  return cube_array

# simulate rotation U
def turn_up(cube_array):
  temp_arr = copy.deepcopy(cube_array)
  white_arr = copy.deepcopy(cube_array[0])
  orange_arr = copy.deepcopy(cube_array[1])
  green_arr = copy.deepcopy(cube_array[2])
  red_arr = copy.deepcopy(cube_array[3])
  blue_arr = copy.deepcopy(cube_array[4])
  yellow_arr = copy.deepcopy(cube_array[5])

  # orange
  cube_array[1][0] = green_arr[0]

  # green
  cube_array[2][0] = red_arr[0]

  # red
  cube_array[3][0] = blue_arr[0]

  # blue
  cube_array[4][0] = orange_arr[0]

  # white
  new_array = [
    temp_arr[2],
    temp_arr[3],
    temp_arr[0],
    temp_arr[1],
    temp_arr[5],
    temp_arr[4]
  ]
  new_array = turn_front(new_array)
  rotated_white_arr = new_array[2]
  cube_array[0] = rotated_white_arr

  return cube_array

# simulate rotation D
def turn_down(cube_array):
  temp_arr = copy.deepcopy(cube_array)
  white_arr = copy.deepcopy(cube_array[0])
  orange_arr = copy.deepcopy(cube_array[1])
  green_arr = copy.deepcopy(cube_array[2])
  red_arr = copy.deepcopy(cube_array[3])
  blue_arr = copy.deepcopy(cube_array[4])
  yellow_arr = copy.deepcopy(cube_array[5])

  cube_array[1][2] = blue_arr[2]    # orange
  cube_array[2][2] = orange_arr[2]  # green
  cube_array[3][2] = green_arr[2]   # red
  cube_array[4][2] = red_arr[2]     # blue

  # yellow
  new_array = [
    temp_arr[2],
    temp_arr[1],
    temp_arr[5],
    temp_arr[3],
    temp_arr[0],
    temp_arr[4]
  ]
  new_array = turn_front(new_array)
  rotated_yellow_array = new_array[2]
  cube_array[5] = rotated_yellow_array

  return cube_array

# simulate rotation B
def turn_back(cube_array):
  temp_arr = copy.deepcopy(cube_array)
  white_arr = copy.deepcopy(cube_array[0])
  orange_arr = copy.deepcopy(cube_array[1])
  green_arr = copy.deepcopy(cube_array[2])
  red_arr = copy.deepcopy(cube_array[3])
  blue_arr = copy.deepcopy(cube_array[4])
  yellow_arr = copy.deepcopy(cube_array[5])

  # white
  red_last_col = [list(sublist) for sublist in zip(
    red_arr[0], red_arr[1], red_arr[2])][2]
  for index in range(3):
    cube_array[0][0][index] = red_last_col[index]

  # orange
  white_first_row = white_arr[0]
  white_first_row.reverse()
  for index in range(3):
    cube_array[1][index][0] = white_first_row[index]

  # red
  yellow_last_row = yellow_arr[2]
  yellow_last_row.reverse()
  for index in range(3):
    cube_array[3][index][2] = yellow_last_row[index]

  # yellow
  orange_first_col = [list(sublist) for sublist in zip(
    orange_arr[0], orange_arr[1], orange_arr[2])][0]
  for index in range(3):
    cube_array[5][2][index] = orange_first_col[index]

  # blue
  new_array = [
    temp_arr[0],
    temp_arr[3],
    temp_arr[4],
    temp_arr[1],
    temp_arr[2],
    temp_arr[5]
  ]
  rotated_blue_array = turn_front(new_array)[2]
  cube_array[4] = rotated_blue_array

  return cube_array

# simulate rotation F'
def turn_front_prime(cube_array):
  temp_arr = copy.deepcopy(cube_array)
  white_arr = copy.deepcopy(cube_array[0])
  orange_arr = copy.deepcopy(cube_array[1])
  green_arr = copy.deepcopy(cube_array[2])
  red_arr = copy.deepcopy(cube_array[3])
  blue_arr = copy.deepcopy(cube_array[4])
  yellow_arr = copy.deepcopy(cube_array[5])

  # white
  red_first_col = [list(sublist) for sublist in zip(
    red_arr[0], red_arr[1], red_arr[2])][0]
  cube_array[0][2] = red_first_col

  # orange
  white_last_row = white_arr[2]
  white_last_row.reverse()
  for index in range(3):
    cube_array[1][index][2] = white_last_row[index]

  # red
  yellow_first_row = yellow_arr[0]
  yellow_first_row.reverse()
  for index in range(3):
    cube_array[3][index][0] = yellow_first_row[index]

  # yellow
  orange_last_col = [list(sublist) for sublist in zip(
    orange_arr[0], orange_arr[1], orange_arr[2])][2]
  cube_array[5][0] = orange_last_col

  # green
  new_green_arr = counter_clockwise(green_arr)
  cube_array[2] = new_green_arr

  return cube_array

# simulate rotation R'
def turn_right_prime(cube_array):
  white_arr = copy.deepcopy(cube_array[0])
  yellow_arr = copy.deepcopy(cube_array[5])

  # face red as front
  new_array = [
    clockwise(white_arr),
    cube_array[2],
    cube_array[3],
    cube_array[4],
    cube_array[1],
    counter_clockwise(yellow_arr)
  ]

  # turn F' (same as R')
  new_array = turn_front_prime(new_array)

  # return front to green
  new_array = [
    counter_clockwise(new_array[0]),
    cube_array[1],
    cube_array[2],
    counter_clockwise(cube_array[3]),
    cube_array[4],
    clockwise(new_array[5])
  ]

  return new_array

# simulate rotation L'
def turn_left_prime(cube_array):
  white_arr = copy.deepcopy(cube_array[0])
  yellow_arr = copy.deepcopy(cube_array[5])

  # front to red
  new_array = [
    clockwise(white_arr, 2),
    cube_array[3],
    cube_array[4],
    cube_array[1],
    cube_array[2],
    clockwise(yellow_arr, 2)
  ]

  # rotate R' (same as L')
  new_array = turn_right_prime(new_array)
  rotated_array = [
    clockwise(new_array[0], 2),
    new_array[3],
    new_array[4],
    new_array[1],
    new_array[2],
    clockwise(new_array[5], 2)
  ]

  return rotated_array

# simulate U'
def turn_up_prime(cube_array):
  white_arr = copy.deepcopy(cube_array[0])
  orange_arr = copy.deepcopy(cube_array[1])
  green_arr = copy.deepcopy(cube_array[2])
  red_arr = copy.deepcopy(cube_array[3])
  blue_arr = copy.deepcopy(cube_array[4])

  cube_array[0] = counter_clockwise(white_arr) # white
  cube_array[1][0] = blue_arr[0]               # orange
  cube_array[2][0] = orange_arr[0]             # green
  cube_array[3][0] = green_arr[0]              # red
  cube_array[4][0] = red_arr[0]                # blue

  return cube_array

# simulate D'
def turn_down_prime(cube_array):
  orange_arr = copy.deepcopy(cube_array[1])
  green_arr = copy.deepcopy(cube_array[2])
  red_arr = copy.deepcopy(cube_array[3])
  blue_arr = copy.deepcopy(cube_array[4])
  yellow_arr = copy.deepcopy(cube_array[5])

  cube_array[1][2] = green_arr[2]
  cube_array[2][2] = red_arr[2]
  cube_array[3][2] = blue_arr[2]
  cube_array[4][2] = orange_arr[2]
  cube_array[5] = counter_clockwise(yellow_arr)

  return cube_array

# simulate B'
def turn_back_prime(cube_array):
  new_array = copy.deepcopy(cube_array)
  for rotation in range(3):
    new_array = turn_back(new_array)

  return new_array
