import Salles, Objets, Personnage
import time, sys

print("                                                                                                          "
      "......................................................................................................... "
      "                                                                                                          "
      " * * *   (Beginning of transmittion) - Hello fellow human, welcome to my game!  * * *                     "
      "                                                                                                          "
      "Here's the situation: due to some bad choices from the rulers of the Great Empires, nuclear centrals were "
      "left without care and without surpervision. This lack of attention brought to their explosion and the     "
      "spread of nuclear particules in the air. Civilisations are now forced to live in shelters. 704 Shelters   "
      "have been recorded around the world but more than half of the initial population perished...              "
      "                                                                                                          "
      "In this adventure you incarnate a worker in the shelter, you work in a Water treament plant. The incident "
      "that happened on the planet made you lose everything you cared about, your home, your wife and with her,  "
      "your will to live. Anger grew into you and all you want to have is revenge.                               "
      "                                                                      * * *(End of transmition)* * *      "
      "......................................................................................................... "
      "                                                                                                          ")

print("- ZZzzz.....ZZzzzz....ZZzzzz..... ... ... ... ... ")

rm = Salles.search_room(Personnage.player.playerposition)

inventory = []

max_inventory = 2



Used = []

#True/False factors
Victory = False
PlayerUp = False
OpenDoor = False
HaveMask = False
GasMask = False
RatsGone = False
NoWater = False
LoadedGun = False


#ask for input until the game isn't finished
while Victory == False:
    while PlayerUp == False:
        wake = input("\n").lower()
        if wake == "wake up":
            print("- you wake up from you bed, the alarm clock shows it's 8:10 in the morning.")
            PlayerUp = True
        elif wake == "look" or "go" or "take" or "use" or "drop":
            print("- you cannot do this action for the moment")

        elif wake != "wake up":
            print("- invalid action or invalid syntax")
            
    playerinput = input("\n").lower()

    if playerinput == "wake up":
        print("- you are already up")


#move inputs  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    elif playerinput == "move":
        if Objets.names[0] not in Used:
            print("You might want to wear your uniform instead of going out half naked.")
            time.sleep(3)

        elif Objets.names[0] in Used:
            print("- in which direction do you want to move ?")
            playerinput = input("move ").lower()
            
        #move north
            if playerinput == "north":
                Personnage.player.move(0, -1)
                rm = Salles.search_room(Personnage.player.playerposition)
                if rm.name == "None":
                    print("- There is nothing in this direction.")
                    Personnage.player.move(0, 1)
                else:
                    print("- you enter the " + rm.name)
                    if Personnage.player.playerposition == (3, 5):
                        if NoWater == False:
                            print("  #You finally understand why there is so much water on the floor: One of the pipes leaks!")
                    
        #move south    
            elif playerinput == "south":
                Personnage.player.move(0, 1)
                rm = Salles.search_room(Personnage.player.playerposition)
                if rm.name == "None":
                    print("- There is nothing in this direction.")
                    Personnage.player.move(0, -1)
                else:
                    print("- you enter the " + rm.name)
                    if Personnage.player.playerposition == (3, 7):
                        if NoWater == False:
                            print("  #All this water near the power plant is getting very, very dangerous!")
                
        #move east    
            elif playerinput == "east":
                if Personnage.player.playerposition == (1, 2):
                    if OpenDoor == True:
                        print("  #While leaving the room, you hear the door close behind you.")
                        OpenDoor = False
                        Personnage.player.move(1, 0)
                        rm = Salles.search_room(Personnage.player.playerposition)
                        if rm.name == "None":
                            print("- There is nothing in this direction.")
                            Personnage.player.move(-1, 0)
                        else:
                            print("- you enter the " + rm.name)
                else:
                    Personnage.player.move(1, 0)
                    rm = Salles.search_room(Personnage.player.playerposition)
                    if rm.name == "None":
                        print("- There is nothing in this direction.")
                        Personnage.player.move(-1, 0)
                    else:
                        print("- you enter the " + rm.name)
                        if Personnage.player.playerposition == (3, 6):
                            if NoWater == False:
                                print("  #Your feet are wet now, why is there water all over the floor?")
                        
        #move west
            elif playerinput == "west":
                Personnage.player.move(-1, 0)
                rm = Salles.search_room(Personnage.player.playerposition)
                if rm.name == "None":
                    print("- There is nothing in this direction.")
                    Personnage.player.move(1, 0)
                else:
                    print("- you enter the " + rm.name)
                    if Personnage.player.playerposition == (1, 10):
                        if RatsGone == False:
                            print("  #There is a problem, these rats shouldn't be there and they appear to have been in contact with, \n"
                                  "  #lets say, not really good products.")
                    
        #move up
            elif playerinput == "up":
                if Personnage.player.playerposition == (2, 2):
                    print("- You can't go more upwards.")
                elif Personnage.player.playerposition == (2, 6) or Personnage.player.playerposition == (2, 10):
                    Personnage.player.move(0,-4)
                    rm = Salles.search_room(Personnage.player.playerposition)
                    print("- you went up one floor.")
                else:
                    print("- You need to use an elevator to change floor.")
                    
        #move down
            elif playerinput == "down":
                if Personnage.player.playerposition == (2, 10):
                    print("- You can't go more downwards.")
                elif Personnage.player.playerposition == (2, 6):
                    if NoWater == False:
                        print("\n*** WARNING There is a problem on level -2! ***\n"
                              "- For your safety the elevator won't go down till the problem is not solved.")
                    elif NoWater == True:
                        Personnage.player.move(0, 4)
                        rm = Salles.search_room(Personnage.player.playerposition)
                        print("- You came down one floor.")
                elif Personnage.player.playerposition == (2, 2):
                    Personnage.player.move(0, 4)
                    rm = Salles.search_room(Personnage.player.playerposition)
                    print("- You came down one floor.")
                else:
                    print("- You need to use an elevator to change floor.")

            else:
                print("- Invalid syntax! Please write again")
        else:
            print("- Invalid syntax! Please write again")
                
#look input - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
    elif playerinput == "look":
        print("- what do you want to look at ?")
        playerinput = input("look ").lower()
        rm = Salles.search_room(Personnage.player.playerposition)
        
    #inputs for all rooms
        if playerinput == "room":
            print(rm.description)
            rm.print_items()
            
    #information on every objects in the item list
        elif playerinput == "inventory":
            if inventory == []:
                print("- there is nothing in your inventory.")
            else:
                print(inventory)

        elif playerinput == Objets.names[0]:
            if Personnage.player.playerposition == Objets.position[0]:
                print(Objets.items[0])
            elif Objets.names[0] in inventory or Objets.names[0] in Used:
                print(Objets.items[0])
            else:
                print("There is no uniform in this room.")
            
        elif playerinput == Objets.names[1]:
            if Personnage.player.playerposition == Objets.position[1]:
                print(Objets.items[1])
            elif Objets.names[1] in inventory or Objets.names[1] in Used:
                print(Objets.items[1])
            else:
                print("There is no watch in this room.")

        elif playerinput == Objets.names[2]:
            if Personnage.player.playerposition == Objets.position[2]:
                print(Objets.items[2])
            elif Objets.names[2] in inventory or Objets.names[2] in Used:
                print(Objets.items[2])
            else:
                print("There is no broom in this room.")
        
        elif playerinput == Objets.names[3]:
            if Personnage.player.playerposition == Objets.position[3]:
                print(Objets.items[3])
            elif Objets.names[3] in inventory or Objets.names[3] in Used:
                print(Objets.items[3])
            else:
                print("There is no notebook in this room.")

        elif playerinput == Objets.names[4]:
            if Personnage.player.playerposition == Objets.position[4]:
                print(Objets.items[4])
            elif Objets.names[4] in inventory or Objets.names[4] in Used:
                print(Objets.items[4])
            else:
                print("There is no watch in this room.")
        
        elif playerinput == Objets.names[5] or playerinput == "adhesive" or playerinput == "tape":
            if Personnage.player.playerposition == Objets.position[5]:
                print(Objets.items[5])
            elif Objets.names[5] in inventory or Objets.names[5] in Used:
                print(Objets.items[5])
            else:
                print("There is no adhesive tape in this room.")

        elif playerinput == Objets.names[6]:
            if Personnage.player.playerposition == Objets.position[6]:
                print(Objets.items[6])
            elif Objets.names[6] in inventory or Objets.names[6] in Used:
                print(Objets.items[6])
            else:
                print("There is no armor in this room.")
        
        elif playerinput == Objets.names[7]:
            if Personnage.player.playerposition == Objets.position[7]:
                print(Objets.items[7])
            elif Objets.names[7] in inventory or Objets.names[7] in Used:
                print(Objets.items[7])
            else:
                print("There is no gun in this room.")
        
        elif playerinput == Objets.names[8]:
            if Personnage.player.playerposition == Objets.position[8]:
                print(Objets.items[8])
            elif Objets.names[8] in inventory or Objets.names[8] in Used:
                print(Objets.items[8])
            else:
                print("There is no lever in this room.")
        
        elif playerinput == Objets.names[9]:
            if Personnage.player.playerposition != Objets.position[9]:
                print("There are no buttons in this room.")
            if Personnage.player.playerposition == Objets.position[9]:
                print(Objets.items[9])
        
        elif playerinput == Objets.names[10]:
            if Personnage.player.playerposition == Objets.position[10]:
                print(Objets.items[10])
            elif Objets.names[10] in inventory or Objets.names[10] in Used:
                print(Objets.items[10])
            else:
                print("There are no bottles in this room.")

        elif playerinput == Objets.names[11]:
            if Personnage.player.playerposition == Objets.position[11]:
                print(Objets.items[11])
            elif Objets.names[11] in inventory or Objets.names[11] in Used:
                print(Objets.items[11])
            else:
                print("There are no syringes in this room.")

        elif playerinput == Objets.names[12]:
            if Personnage.player.playerposition == Objets.position[12]:
                print(Objets.items[12])
            elif Objets.names[12] in inventory or Objets.names[21] in Used:
                print(Objets.items[1])
            else:
                print("There are no rats in this room.")

        elif playerinput == Objets.names[13]:
            if Personnage.player.playerposition == Objets.position[13]:
                print(Objets.items[13])
            elif Objets.names[13] in inventory or Objets.names[13] in Used:
                print(Objets.items[13])
            else:
                print("There are no bullets in this room.")

        elif playerinput == Objets.names[14]:
            if Personnage.player.playerposition == Objets.position[14]:
                print(Objets.items[14])
            elif Objets.names[14] in inventory or Objets.names[14] in Used:
                print(Objets.items[14])
            else:
                print("There is no dagger in this room.")
                
        else:
            print("- Invalid syntax! Please write again")  
            
#take input - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            
    elif playerinput == "take":
        print("- what do you want to take ?")
        playerinput = input("take ").lower()

        #removing the object from where it is to the inventory
        if playerinput == Objets.names[0]:
            if Objets.names[0] in inventory:
                print("- You already have this item, check your inventory if you need.")
            else:
                if len(inventory) < max_inventory:
                    print("- you take your uniform under the arm.")
                    inventory.append(Objets.names[0])
                    rm.items.remove(Objets.names[0])
                else:
                    print("There is no more space left in your inventory")
        
        elif playerinput == Objets.names[1]:
            if Objets.names[1] in inventory:
                print("- You already have this item, check your inventory if you need.")
            else:
                if len(inventory) < max_inventory:
                    print("- You put your watch on our wrist.")
                    inventory.append(Objets.names[1])
                    rm.items.remove(Objets.names[1])
                else:
                    print("There is no more space left in your inventory")
                
        elif playerinput == Objets.names[2]:
            if Objets.names[2] in inventory:
                print("- You already have this item, check your inventory if you need.")
            else:
                if len(inventory) < max_inventory:
                    print("- You take the broom with you, the dust on it make you caugh a bit.")
                    inventory.append(Objets.names[2])
                    rm.items.remove(Objets.names[2])
                else:
                    print("There is no more space left in your inventory")
          
        elif playerinput == Objets.names[3]:
            if Objets.names[3] in inventory:
                print("- You already have this item, check your inventory if you need.")
            else:
                if len(inventory) < max_inventory:
                    print("- A notebook has been added to your inventory.")
                    inventory.append(Objets.names[3])
                    rm.items.remove(Objets.names[3])
                else:
                    print("There is no more space left in your inventory")

        elif playerinput == Objets.names[4]:
            if Objets.names[4] in inventory:
                print("- You already have this item, check your inventory if you need.")
            else:
                if len(inventory) < max_inventory:
                    print("- You take the toolbox with you.")
                    inventory.append(Objets.names[4])
                    rm.items.remove(Objets.names[4])
                else:
                    print("There is no more space left in your inventory")
             
        elif playerinput == Objets.names[5] or playerinput == "adhesive" or playerinput == "tape":
            if Objets.names[5] in inventory:
                print("- You already have this item, check your inventory if you need.")
            else:
                if len(inventory) < max_inventory:
                    print("- An adhesif tape has been added to your inventory.")
                    inventory.append(Objets.names[5])
                    rm.items.remove(Objets.names[5])
                else:
                    print("There is no more space left in your inventory")
                
        elif playerinput == Objets.names[6]:
            if RatsGone == True:
                if Objets.names[6] in inventory:
                    print("- You already have this item, check your inventory if you need.")
                else:
                    if len(inventory) < max_inventory:
                        print("- You take the armor with you, it's really heavy though.")
                        inventory.append(Objets.names[6])
                        rm.items.remove(Objets.names[6])
                        HaveMask = True
                    else:
                        print("There is no more space left in your inventory")                    
            elif RatsGone == False:
                print("- The closer you get to the armor, the closer the rats are to you. It would be better to get them out of \n"
                      "  the way to collect the armor.")
                
        elif playerinput == Objets.names[7]:
            if RatsGone == True:
                if Objets.names[7] in inventory:
                    print("- You already have this item, check your inventory if you need.")
                else:
                    if len(inventory) < max_inventory:
                        print("- You take the gun.")
                        inventory.append(Objets.names[7])
                        rm.items.remove(Objets.names[7])
                    else:
                        print("There is no more space left in your inventory")
            elif RatsGone == False:
                print("- The closer you get to the gun, the closer the rats are to you. It would be better to get them out of \n"
                      "  the way to collect the gun.")
                
        elif playerinput == Objets.names[8]:
            print("- Good luck trying to take the lever with you!")
           
        elif playerinput == Objets.names[9]:
            print("- You can't take the buttons with you,they are fixed in the wall!")
         
        elif playerinput == Objets.names[10]:
            if Objets.names[10] in inventory:
                print("- You already have this item, check your inventory if you need")
            else:
                if len(inventory) < max_inventory:
                    print("- The bottles has been added to your inventory.")
                    inventory.append(Objets.names[10])
                    rm.items.remove(Objets.names[10])
                else:
                    print("There is no more space left in your inventory")
                
        elif playerinput == Objets.names[11]:
            if Objets.names[11] in inventory:
                print("- You already have this item, check your inventory if you need.")
            else:
                if len(inventory) < max_inventory:
                    print("- The syringes has been added to your inventory.")
                    inventory.append(Objets.names[11])
                    rm.items.remove(Objets.names[11])
                else:
                    print("There is no more space left in your inventory")
                
        elif playerinput == Objets.names[12]:
            print("- You might not want to touch the rats with bare hands.")

        elif playerinput == Objets.names[13]:
            if Objets.names[13] in inventory:
                print("- You already have this item, check your inventory if you need.")
            else:
                if len(inventory) < max_inventory:
                    print("- The bullets have been added to your inventory.")
                    inventory.append(Objets.names[13])
                    rm.items.remove(Objets.names[13])
                else:
                    print("There is no more space left in your inventory")
                
        elif playerinput == Objets.names[14]:
            if Objets.names[14] in inventory:
                print("- You already have this item, check your inventory if you need.")
            else:
                if len(inventory) < max_inventory:
                    print("- You take the dagger and put it in your pocket.")
                    inventory.append(Objets.names[14])
                    rm.items.remove(Objets.names[14])
                else:
                    print("There is no more space left in your inventory")
                
        else:
            print("- Invalid syntax! Please write again")
            
#drop input - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            
    elif playerinput == "drop":

        #no drops in the elevator
        if Personnage.player.playerposition == (2, 2) or Personnage.player.playerposition == (2, 6) or Personnage.player.playerposition == (2, 10):
            print("Please don't leave objects in the Elevator. someone else might take it from you.")
            playerinput = input().lower()
        #no drops in the corridors
        elif Personnage.player.playerposition == (3, 2) or Personnage.player.playerposition == (3, 6) or Personnage.player.playerposition == (3, 10) or Personnage.player.playerposition == (1, 10):
            print("Please don't leave objects in the way, it clogs up the passage.")
            playerinput = input().lower()
        #removing the object from the inventory to the room where the player is
        print("- what do you want to drop ?")
        playerinput = input("drop ").lower()

        if playerinput == Objets.names[0]:
            if Objets.names[0] not in inventory:
                print("- You don't have this object in your inventory to throw.")
            elif Objets.names[0] in inventory:
                print("- You leave your uniform on a chair or whatever you found.")
                inventory.remove(Objets.names[0])
                rm = Salles.search_room(Personnage.player.playerposition)
                rm.items.append(Objets.names[0])
            
        elif playerinput == Objets.names[1]:
            if Objets.names[1] not in inventory:
                print("- You don't have this object in your inventory to throw.")
            elif Objets.names[1] in inventory:
                print("- You take the watch off your wrist and place it on a table.")
                inventory.remove(Objets.names[1])
                rm = Salles.search_room(Personnage.player.playerposition)
                rm.items.append(Objets.names[1])
            
        elif playerinput == Objets.names[2]:
            if Objets.names[2] not in inventory:
                print("- You don't have this object in your inventory to throw.")
            else:
                print("- You get rid of the broom in a corner of the room.")
                inventory.remove(Objets.names[2])
                rm = Salles.search_room(Personnage.player.playerposition)
                rm.items.append(Objets.names[2])
            
        elif playerinput == Objets.names[3]:
            if Objets.names[3] not in inventory:
                print("- You don't have this object in your inventory to throw.")
            else:
                print("- You don't have a notebook anymore in your inventory.")
                inventory.remove(Objets.names[3])
                rm = Salles.search_room(Personnage.player.playerposition)
                rm.items.append(Objets.names[3])

        elif playerinput == Objets.names[4]:
            if Objets.names[4] not in inventory:
                print("- You don't have this object in your inventory to throw.")
            else:
                print("- You put down the toolbox.")
                inventory.remove(Objets.names[4])
                rm = Salles.search_room(Personnage.player.playerposition)
                rm.items.append(Objets.names[4])
            
        elif playerinput == Objets.names[5] or playerinput == "adhesive" or playerinput == "tape":
            if Objets.names[5] not in inventory:
                print("- You don't have this object in your inventory to throw.")
            else:
                print("- You don't have an adhesif anymore tape in your inventory.")
                inventory.remove(Objets.names[5])
                rm = Salles.search_room(Personnage.player.playerposition)
                rm.items.append(Objets.names[5])
            
        elif playerinput == Objets.names[6]:
            if Objets.names[6] not in inventory:
                print("- You don't have this object in your inventory to throw.")
            else:
                print("- You leave the armor on the floor, on the side, and feel realised.")
                inventory.remove(Objets.names[6])
                rm = Salles.search_room(Personnage.player.playerposition)
                rm.items.append(Objets.names[6])
                HaveMask = False
            
        elif playerinput == Objets.names[7]:
            if Objets.names[7] not in inventory:
                print("- You don't have this object in your inventory to throw.")
            else:
                print("- You place the gun in a safe place of the room.")
                inventory.remove(Objets.names[7])
                rm = Salles.search_room(Personnage.player.playerposition)
                rm.items.append(Objets.names[7])
            
        elif playerinput == Objets.names[10]:
            if Objets.names[10] not in inventory:
                print("- You don't have this object in your inventory to throw.")
            else:
                print("- You don't have bottles anymore in your inventory.")
                inventory.remove(Objets.names[10])
                rm = Salles.search_room(Personnage.player.playerposition)
                rm.items.append(Objets.names[10])
            
        elif playerinput == Objets.names[11]:
            if Objets.names[11] not in inventory:
                print("- You don't have this object in your inventory to throw.")
            else:
                print("- You don't have syringes anymore in your inventory.")
                inventory.remove(Objets.names[11])
                rm = Salles.search_room(Personnage.player.playerposition)
                rm.items.append(Objets.names[11])

        elif playerinput == Objets.names[12]:
            print("- You can't take them in the first place.")

        elif playerinput == Objets.names[13]:
            if Objets.names[13] not in inventory:
                print("- You don't have this object in your inventory to throw.")
            else:
                print("- You don't have bullets anymore in your inventory.")
                inventory.remove(Objets.names[13])
                rm = Salles.search_room(Personnage.player.playerposition)
                rm.items.append(Objets.names[13])

        elif playerinput == Objets.names[14]:
            if Objets.names[14] not in inventory:
                print("- You don't have this object in your inventory to throw.")
            else:
                print("- You don't have a dagger anymore in your inventory.")
                inventory.remove(Objets.names[14])
                rm = Salles.search_room(Personnage.player.playerposition)
                rm.items.append(Objets.names[14])

        else:
            print("- Invalid syntax! Please write again")
            
#use input - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
    
    elif playerinput == "use":
        print("-Which item do you want to use")
        playerinput = input("use ").lower()
            
    #use the WATCH
        if playerinput == Objets.names[1]:
            if Objets.names[1] in inventory:
                print("- The hands of the watch do not seem to move,seems that there is no battery.")
            else:
                print("- There is no watch on your wrist, you forgot to put it on.")

    #use the BROOM
        elif playerinput == Objets.names[2]:
            if Objets.names[2] in inventory:
                if RatsGone == False :
                    if Personnage.player.playerposition != (1, 10):
                        print("- You sweep the floor, there is no more dust in the room.")
                    elif Personnage.player.playerposition == (1, 10):
                        print("- Do you want to remove the dust?")
                        playerinput = input().lower()
                        if playerinput == "yes":
                            print("- You sweep the floor, there is no more dust in the room.")
                        elif playerinput == "no":
                            print("- What do you want to remove then?")
                            playerinput = input().lower()
                            if playerinput == Objets.names[12]:
                                print("- You use the broom to chase the rats from the room. It works fine, the rats are gone!")
                                rm.items.remove(Objets.names[12])
                                RatsGone = True
                            elif playerinput != Objets.names[12]:
                                print("- You can't do this action")
                            else:
                                print("- Invalid syntax! Please write again")
                        else:
                            print("- Invalid syntax! Please write again")
                elif RatsGone == True:
                    print("- You sweep the floor, there is no more dust in the room.")
                else:
                    print("- Invalid syntax! Please write again")
            elif Objets.names[2] not in inventory:
                print("- It's gonna be difficult to use a broom without having a broom.")
            else:
                print("- Invalid syntax! Please write again")
                
    #use the DAGGER
        elif playerinput == Objets.names[14]:
            if Objets.names[14] in inventory:
                if RatsGone == False:
                    if Personnage.player.playerposition == (1, 10):
                        print("- You want to attack the rats?")
                        playerinput = input().lower()
                        if playerinput == "yes":
                            print("- If you think about it, they will all jump on you when you will come close to them. You should find \n "
                                  "  something to get them off without getting too near.")                                  
                        elif playerinput == "no":
                            print("- OK, well there's nothing else you might attack")
                    elif Personnage.player.playerposition != (1, 10):
                        print("- There is nothing to stab around here. Chill out you psycho!")
                elif RatsGone == True:
                    print("- There is nothing to stab around here. Chill out you psycho!")
            else:
                print("- You don't have a dagger in your inventory")

           
    #use the NOTEBOOK
        elif playerinput == Objets.names[3]:
            if Objets.names[3] in inventory:
                print("- Do you want to write in it or to read your notes?")
                playerinput = input().lower()
                if playerinput == "write":
                    noteinput = input("*Shelter 641 Journal* : ")
                elif playerinput == "read":
                    print("- Here are your previous notes : " + noteinput)
            else:
                print("- You need a notebook if you want to write in it.")
                    
    #use the TOOLBOX
        elif playerinput == Objets.names[4]:
            if Objets.names[4] in inventory:
                print("- There is nothing that really needs reparation.")
            else:
                print("- You don't have a toolbox with you.")
                
    #use the ADHESIVE TAPE
        elif playerinput == Objets.names[5] or playerinput == "adhesive" or playerinput == "tape":
            if Objets.names[5] in inventory:
                if Personnage.player.playerposition != (3, 5):
                    print("- There is nothing useful do with it in this room.")
                elif Personnage.player.playerposition == (3, 5):
                    print("- Where do you want to use it?")
                    playerinput = input().lower()
                    if playerinput == "pipes" or playerinput == "pipe":
                        print("- Good job, hopefully you have clogged the hole at the right moment. The remaining water on the floor \n"
                              "  will evacuate bit by bit in the lower level. You should have access to it now.\n"
                              "  #(the adhesive tape is consumed in this action)")
                        inventory.remove(Objets.names[5])
                        NoWater = True                           
                    else:
                        print("- You can't do this action.")
            else:
                print("- You can't use an item you don't have.")

    #use the LEVER
        elif playerinput == Objets.names[8]:
            if Objets.names[8] in rm.items:
                if OpenDoor == True:
                    print("- The Vault Door is already open.")
                elif OpenDoor == False:
                    print("- You action the lever with difficulty but manage to do it. The big door of the vault opens up with a lot "
                          "  of noise.")
                    OpenDoor = True
            else:
                print("- There is no lever in the room to action.")

    #use the SYRINGES
        elif playerinput == Objets.names[11]:
            if Objets.names[11] in inventory:
                print("- These are the syringes with the same product used on the rats you can find in storage room. You \n"
                      "  shouldn't use them anymore.")
            else:
                print("- You don't have syringes in your inventory.")
                
#specific actions input - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    elif playerinput == "wear":
        print("- What do you want to wear ?")
        playerinput = input("wear ").lower()
        
    #wear the UNIFORM
        if playerinput == Objets.names[0]:
            if Objets.names[0] in Used:
                print("- You already wear your uniform.")
            elif Objets.names[0] in inventory:
                print("- You now wear your uniform, you can freely move in the vault.")
                inventory.remove(Objets.names[0])
                Used.append(Objets.names[0])
            else:
                print("- You don't have this equipment in your inventory.")

    #wear the ARMOR
        elif playerinput == Objets.names[6]:
            if Objets.names[6] in Used:
                print("- You already wear an armor.")
            elif Objets.names[6] in inventory:
                print("- You are now equiped with a fighting armor.")
                inventory.remove(Objets.names[6])
                Used.append(Objets.names[6])
            else:
                print("- You don't have this equipment in your inventory.")

    #wear the GAS MASK
        elif playerinput == "gas mask" or playerinput == "mask":
            if GasMask == True:
                print("You already wear a gas mask")
            elif HaveMask == True:
                print("- You put the gas mask on your face, you can breathe freely in the Wasteland.")
                GasMask = True
            else:
                print("- You don't have a gas mask with you, you should definitevely find one inside the shelter.")

    #use the BULLETS
    elif playerinput == "reload gun":
        if Objets.names[13] in inventory:
            if Objets.names[7] in inventory:
                print("- The gun is now loaded with bullets.")
                inventory.remove(Objets.names[13])
                LoadedGun = True
            elif Objets.names[7] not in inventory:
                print("- You don't have a gun in which to put the bullets.")
        elif Objets.names[13] not in inventory:
            print("- You have bullets to reload the gun in your inventory.")



    #Get out of the SHELTER
    elif playerinput == "exit shelter":
        if OpenDoor is False:
            print("- The Vault door is closed, you need to open it before having the possibility to go out.")
        elif OpenDoor is True:
            if GasMask == False:
                print("- You are going to exit the shelter in order to find the responsible of the world's catastrophy. But \n "
                      "  before you get out you might want to get yourself a gas mask in order to breathe when you will be in \n "
                      "  the Wasteland and it's radioactive clouds. (Door closes) ")
                OpenDoor = False
            elif GasMask == True:
                print("- You are going to exit the shelter in order to find the responsible of the world's catastrophy. Make \n"
                      "  sure you have everything you need with you for this adventure. It's going to be your last one!\n "
                      "  Are you really ready ?")
                playerinput = input().lower()
                if playerinput == "yes":
                    print("- Alright then, let's go!")
                    Personnage.player.move(6, 0)
                    Victory = True
                elif playerinput == "no":
                    print("- Allright, lets close the door then. Action the lever the lever whenever you'r ready.")
                    OpenDoor = False

    else:
        print("- Invalid syntax! Please write again")

if Victory is True:
    print("                                                                                                          "
          "......................................................................................................... "
          "                                                                                                          "
          " * * *   (Beginning of transmittion) - New transmittion : 15h40   * * *                                   "
          "                                                                                                          "
          "After several hours of walking in the Wasteland, stopping by at each and every vault you see asking for   "
          "information on were you could find the Vault where the big heads are, you finally find a major information"
          "in a journal lost on the ground. It's 10h25 when you start to move in a strait direction : MetivaPolis!   "
          "                                                                                                          "
          "The Shelter 017, it's his number, is in the surronding of the city of MetivaPolis and built in the hollow "
          "of a mountain. Of course in a space well protected from invasions and from the mass pollution. It has also"
          "a great access to primary ressources and food too.                                                        "
          "                                                                                                          "
          "Now is your chance to have your revenge on the people who took away your loved ones. All the people inside"
          "this vault 017 is a priviledged person that needs to pay for whatever they have done wrong to the people. "
          "You are going to be executioner who will make them pay for all their sins . . .                           "
          "                                                                                                          "
          ".........................................................................................................."
          "                                                                                                          ")
    if Objets.names[7] in inventory and LoadedGun == True:
              
        print("When you arrive in front of the door, you give up the front door with a gun, you break into vault 017 and \n"
              "shoot everyone you see in your path. You see a room protected by guards, it is necessarily in this room \n "
              "that the great leaders find themselves. After having put down the guards and smashed the door your rifle \n"
              "no longer has any ammunition but you decide to continue anyway, with your bare hand if necessary. You jump\n"
              "on the commanders, who see you arrive like a fury, and get rid of them one by one. But doing this it with \n"
              "bare hands takes you too much time and meanwhile, security has organized itself and some of them are \n"
              "already aiming you. It's the end for you but at least you got what you wanted.")
              
    elif Objets.names[14] in inventory:
        print("When you arrive in front of the door, you realize that you have nothing to force yourself into the vault,\n"
              "you will have to wait for the door to open on its own. After a day of waiting a soldier enters the \n"
              "shelter, you take advantage of the door being open to sneak inside and attack the soldier from behind. In \n"
              "the vault you dodge the armed soldiers as much as possible while staying in search of a room more \n"
              "important than the others. Only one room is protected by soldiers, it is necessarily in this room that \n"
              "the great leaders find themselves. After having put down the guards and broken down the door you violently\n"
              "attack the commanders of the nations but trying to make the least noise.The case is over, your conscience \n"
              "lighter than ever, you leave without paying attention to anyone. Security finally intervenes but doesn't \n"
              "shoot you, he just stops you. Prison is not disturbing for you, you did what you had to do.")
              
    elif Objets.names[14] and Objets.names[7] and LoadedGun == True:
        print("when you arrive in front of the door, you give up the front door with a gun, you break into vault 017 and\n"
              "shoot everyone you see in your path. After several minutes spent getting rid of security you see a room \n"
              "protected by guards, it is necessarily in this room that the great leaders find it. You knock down the \n"
              "guards and break down the door, unfortunately your rifle is out of ammunition. It is time to use the \n"
              "dagger you recovered from the dining room: you violently attack the commanders of the nations while \n"
              "taking all the time you need. The case is over, your conscience is lighter than ever. There is nothing \n"
              "left alive in the vault. All that's left is you, with a bloody knife in your hand. You did what you've \n"
              "been hoping to do for months, that's it and nothing else kept you alive. . .  Facing the vast landscape \n"
              "destroyed by radioactivity, you drop the knife that lands on the ground and remove your gas mask.")

    print("                                                                                                          "
          "......................................................................................................... "
          "                                                                                                          "
          "                          * * * Well done! You have finished my game * * *                                "
          "       You have finished the game once but did you know that your story can be slightly different?        "
          "                       Try the game again and you might find the other endings.                           "
          "                                                                                                          "
          "......................................................................................................... "
          "                                                                                                          ")
