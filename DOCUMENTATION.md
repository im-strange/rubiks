# `Cube` class from main module

### Methods

`Cube()` class contains several useful functions in simulating the cube.
- `turn_front()`: F
- `turn_front_prime()`: F'
- `turn_right()`: R
- `turn_right_prime()`: R'
- `turn_left()`: L
- `turn_left_prime()`: L'
- `turn_up()`: U
- `turn_up_prime()`: U'
- `turn_down()`: D
- `turn_down_prime()`: D'
- `turn_back()`: B
- `turn_back_prime()`: B'
- `display_letter()`: display cube in letters
- `display_array()`: display array
- `scramble(notations=str)`: scramble cube

### Attributes

The class also has few attributes that may be useful in simulating the cube.
- `cube_array`: contains 3-dimensional array of the cube
- `scramble_notations`: string of the scramble used in `scramble` method

### Accessing the class

The class can be accessed in such way

```py
import rubiks

# initializing the class
mycube = rubiks.Cube()

# scramble the cube
mycube.scramble("R U R' U R U2 R'")

# display the cube
mycube.display_letter()

# output: 
    GWW
    WWW
    RWB
WBB WGO WOO GRR
OOO GGG RRR BBB
OOO GGG RRR BBB
    YYY
    YYY
    YYY
```
