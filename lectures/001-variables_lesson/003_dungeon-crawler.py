# Baby Dungeon Crawler
# --------------------
# player starts at (2, 1)
x_loc = 0
y_loc = 0
# print out the location
print("player location: (" + str(x_loc) + ", " + str(y_loc) + ")")

# choose either horizontal or vertical movement
# if horizontal, input how many spaces to move in the positive x direciton
# if vertical, input how many spaces to move in the positive y direction
# if invalid, terminate proram
x_move = 0
y_move = 0
direction = str(input("horizontal (h) or vertical (v) movement?"))
if direction is 'h':
    x_move = int(input("input horizontal movement: "))
elif direction is 'v':
    y_move = int(input("input vertical movement: "))
else:
    print("invalid direction, program terminated")

while (x_move != 0 and y_move != 0):
    x_loc += x_move
    y_loc += y_move
    print("player location: (" + str(x_loc) + ", " + str(y_loc) + ")")
    print("horizontal (h) or vertical (v) movement?")
    direction = str(input())

    x_move = 0
    y_move = 0
    if direction is "h":
        print("input horizontal movement: ")
        x_move = int(input())
    elif direction is "v":
        print("input vertical movement: ")
        y_move = int(input())
    else:
        print("invalid direction, restart program")