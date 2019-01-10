import Personnage, Objets

class Room:
    def __init__(self, name, description, items, location):
        self.name = name
        self.description = description
        self.items = items
        self.location = location

    def print_items(self):
        item_str = ""
        for item in self.items:
            item_str = item_str + item + ", " 
        if self.items == []:
            print("  The is nothing useful to look at.")
        else:
            print("  ### Item(s) in the room: " + item_str[0:-2] + " ###")

def search_room(location):
    for room in rooms:
        if room.location == location:
            return room

rooms = []

#Vault door             =     (1, 2)
#Elevator               =     (2, 2), (2, 6), (2, 10)
#Barracks               =     (3, 1)
#Corridors              =     (3, 2), (3, 6), (3, 10), (1, 10)
#Dining room            =     (3, 3)
#storage room           =     (1, 6)
#Water treatment plant  =     (3, 5)
#power plant            =     (3, 7)
#armory                 =     (1, 9)
#weight room            =     (1, 11)
#hospital               =     (3, 9)
#science lab            =     (3, 11)



rooms.append( Room("vault door", "- You are in front of the main door. it's the only door that gives access to the outside.\n  There is way out to the east and you can exit the shelter via the huge Vault door.", [Objets.names[8]], (1, 2)))
#lever

rooms.append(Room("elevator", "- This is an elevator, use it to get through the floors. You are currently on floor 0.\n  There is way out to the east and to the west. You can also go down a floor.", [], (2, 2)))
rooms.append(Room("elevator", "- This is an elevator, use it to get through the floors. You are currently on floor -1.\n  There is way out to the east and to the west. You can also go down or up a floor.", [], (2, 6)))
rooms.append(Room("elevator", "- This is an elevator, use it to get through the floors. You are currently on floor -2.\n  There is way out to the east and to the west. You can also go up a floor.", [], (2, 10)))
#level buttons
#shelter map

rooms.append(Room("barracks", "- Here are the barracks: This is the place where the dwellers rest and sleep.\n  There is way out to the south.", [Objets.names[0],Objets.names[1]], (3, 1)))
#alarm clock
#uniforms
#watch
#alarm button

rooms.append(Room("dining room", "- The dining room, of course, the place for dwellers to eat and drink during their breaks.\n  There is way out to the west and to the north.", [Objets.names[10],Objets.names[2],Objets.names[14]], (3, 3)))
#bottles
#plates
#jukebox
#fountain
#broom
#alarm button

rooms.append(Room("storage room", "- This is the storage room, this is where all the unused objects and materials are stored.\n  There is way out to the east.",[Objets.names[6],Objets.names[7],Objets.names[12]], (1, 10)))
#boxes
#junks and scrap
#armors
#guns
#rats

rooms.append(Room("power plant", "- The electric central! the room that produces all the electrical energy of the vault,\n  it is essential for survival in the vault.\n  There is way out to the north.", [Objets.names[3],Objets.names[4]], (3, 7)))
#notebook
#toolbox
#control panel
#extinguisher

rooms.append(Room("water treatment plant", "- The water treatment center allows all dwellers to have access to drinking water.\n  There is way out to the south.", [Objets.names[5]], (3, 5)))
#notebook
#toolbox
#adhesif
#control panel
#extinguisher

rooms.append(Room("armory","- The armory is the room where all the weapons are stored, All weapons are used for the moment.\n  There is way out to the south.", [Objets.names[13]], (1, 5)))
#bullets
#machines

rooms.append(Room("weight room", "- The weight rooms. Space of well being, made to keep the dwellers in good physical shape.\n  There is way out to the north.", [], (1, 7)))
#weights
#ropes
#work bench

rooms.append(Room("hospital","- you are in the hospital. There is way out to the south.", [Objets.names[9]], (3, 9)))
#beds
#first aid kit
#syringes

rooms.append(Room("science lab", "- The science lab is the privatized space for the smartest of the dwellers.\n  They are doing experiments to solve the problem of radioactive clouds found in the wasteland.\n  There is way out to the north.", [], (3, 11)))
#chemicals
#microscope
#anti-radiation suit
#anti-radiation care

rooms.append(Room("corridor", "- you are in a corridor. You can enter a room to the north, to the south and to the west.", [], (3, 2)))
rooms.append(Room("corridor", "- you are in a corridor. You can enter a room to the north, to the south and to the west.", [], (3, 6)))
rooms.append(Room("corridor", "- you are in a corridor. You can enter a room to the north, to the south and to the west.", [], (3, 10)))
rooms.append(Room("corridor", "- you are in a corridor. You can enter a room to the north, to the south and to the east.", [], (1, 6)))

#Not existing rooms
rooms.append(Room("None","- There is nothing in this direction", [], (0, 2)))
rooms.append(Room("None","- There is nothing in this direction", [], (0, 6)))
rooms.append(Room("None","- There is nothing in this direction", [], (0, 9)))
rooms.append(Room("None","- There is nothing in this direction", [], (0, 10)))
rooms.append(Room("None","- There is nothing in this direction", [], (0, 11)))
rooms.append(Room("None","- There is nothing in this direction", [], (1, 1)))
rooms.append(Room("None","- There is nothing in this direction", [], (1, 3)))
rooms.append(Room("None","- There is nothing in this direction", [], (1, 4)))
rooms.append(Room("None","- There is nothing in this direction", [], (1, 8)))
rooms.append(Room("None","- There is nothing in this direction", [], (1, 9)))
rooms.append(Room("None","- There is nothing in this direction", [], (1, 11)))
rooms.append(Room("None","- There is nothing in this direction", [], (2, 1)))
rooms.append(Room("None","- There is nothing in this direction", [], (2, 3)))
rooms.append(Room("None","- There is nothing in this direction", [], (2, 5)))
rooms.append(Room("None","- There is nothing in this direction", [], (2, 7)))
rooms.append(Room("None","- There is nothing in this direction", [], (2, 9)))
rooms.append(Room("None","- There is nothing in this direction", [], (2, 11)))
rooms.append(Room("None","- There is nothing in this direction", [], (3, 0)))
rooms.append(Room("None","- There is nothing in this direction", [], (3, 4)))
rooms.append(Room("None","- There is nothing in this direction", [], (3, 8)))
rooms.append(Room("None","- There is nothing in this direction", [], (3, 12)))
rooms.append(Room("None","- There is nothing in this direction", [], (4, 1)))
rooms.append(Room("None","- There is nothing in this direction", [], (4, 2)))
rooms.append(Room("None","- There is nothing in this direction", [], (4, 3)))
rooms.append(Room("None","- There is nothing in this direction", [], (4, 5)))
rooms.append(Room("None","- There is nothing in this direction", [], (4, 6)))
rooms.append(Room("None","- There is nothing in this direction", [], (4, 7)))
rooms.append(Room("None","- There is nothing in this direction", [], (4, 9)))
rooms.append(Room("None","- There is nothing in this direction", [], (4, 10)))
rooms.append(Room("None","- There is nothing in this direction", [], (4, 11)))

