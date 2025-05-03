# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.
 
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.
player = input("Please type your name: ")
print(f"Hello {player}. \nWelcome to the game world!")
door = input("choose between the left or the right door. \nType right/left: ")
left = False
right = True
while door == False:
    left_door_coise = input("You see an empty room. Type return/look around: ")
    if left_door_coise == "look around":
        print("You look around the empty room and find a dusty sword")