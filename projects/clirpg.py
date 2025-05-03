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
door = (input("choose between the left or the right door. \nType right/left: ").lower())
while door == "left":
    left_door_coise = (input("You see an empty room. \nType return/look around: ").lower())
    if left_door_coise == "look around":
        print("You look around the empty room and find a sword")
        sword_choise = (input("Take the sword or leave is? \nType yes/no: ").lower())
        if sword_choise == "yes":
            print("You returned and entered the right door \nYou see a dragon in the room.")
            dragon_choise = (input("Fight the dragon or return \nType fight/return: ").lower())
            if dragon_choise == "fight":
                print("You won!!!")    
            break
    else:
        if left_door_coise == "return":
            print("You returned and entered the right door \nYou see a dragon in the room.")
            dragon_choise = input("Fight the dragon or return \nType fight/return: ")
            if dragon_choise == "fight":
                 print("You've been eaten by the dragon! \nYou lost.") 
                 break
        else:
            if dragon_choise == "return":
                print("You went back and entered the left room, you look around and find a sword")
                sword_choise = (input("Take the sworr or leave is? \nType yes/no: ").lower())
                if sword_choise == "yes":
                        print("You returned and entered the right door \nYou see a dragon in the room.")
                        dragon_choise = (input("Fight the dragon or return \nType fighe/return: ").lower())
                        if dragon_choise == "fight":
                                print("You won!!!")
                                break
                        else:
                            if dragon_choise == "return":
                                print("star over")
                                break        
                else:
                    if sword_choise == "no":
                        print("start over")
                        break    
else: 
    while door == "right":
        print("You returned and entered the right door \nYou see a dragon in the room.")
        dragon_choise = input("Fight the dragon or return \nType fighe/return: ")
        if dragon_choise == "fight":
             print("You've been eaten by the dragon! \nYou lost.") 
             break
        else:
            if dragon_choise == "return":
                print("You went back and entered the left room")
                left_door_coise = (input("You see an empty room. \nType return/look around: ").lower())
                if left_door_coise == "look around":
                    print("You've looked around the left room and found a sword.")
                    sword_choise = (input("Take the sword or leave it? \nType yes/no: ").lower())
                    if sword_choise == "yes":
                        print("You returned and entered the right door \nYou see a dragon in the room.")
                        dragon_choise = (input("Fight the dragon or return \nType fighe/return: ").lower())
                        if dragon_choise == "fight":
                            print("You won!!!")
                        break
                    elif sword_choise == "no":
                        print("You look around the empty room and find a sword")
                        sword_choise = (input("Take the sword or leave it? \nType yes/no: ").lower())
                        if sword_choise == "yes":
                            print("You returned and entered the right door \nYou see a dragon in the room.")  
                            dragon_choise = (input("Fight the dragon or return \nType fighe/return: ").lower())
                            if dragon_choise == "fight":
                                print("You Won!")
                                break
                            else:
                                print("Start over!")
                                break
         
            
           