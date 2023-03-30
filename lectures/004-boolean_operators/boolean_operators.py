"""
-   Boolean operators (and, or, not)
-   Truth Tables
-   Example of 'and'
-   Example of 'or'
-   Combining both
"""

# if homework is done, user can play a game
homework = str(input("Are you finished your homework? ")).lower()
mop_floor = str(input("Are you done mopping the floor? ")).lower()
clean_room = str(input("Are you done cleaning your room? ")).lower()

if (homework == "yes" and (mop_floor == "yes" or clean_room == "yes")):
    print("You can play a game!")
else:
    if (homework == "yes"):
        print("Finish one of your chores!")
    elif (mop_floor == "yes" or clean_room == "yes"):
        print("Finish your homework!")
    else:
        print("Finish your homework and do a chore!")