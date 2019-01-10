class Player:
    def __init__(self, inventory, playerpositionX, playerpositionY,playerposition):
        self.inventory = inventory
        self.playerpositionX = playerpositionX
        self.playerpositionY = playerpositionY
        self.playerposition = playerposition

    def move(self,dx, dy):
        self.playerpositionX = self.playerpositionX + dx   
        self.playerpositionY = self.playerpositionY + dy
        self.playerposition = (self.playerpositionX, self.playerpositionY)
    
#creation of the world
world = {}
#set the starting position of the player
starting_position = (3, 1)

player = Player([], 3, 1, (3,1))

def load_tiles():
    #Parses a file that describes the world space into the world object
    with open('Carte.xlsx', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t')) #Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '') #Windows users may need to replace '\r\n'
            print(tile_name)
            if tile_name == 'Barracks':
                global starting_position
                starting_position = (x, y)
            world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

def is_a_tile(x, y):
    return world.get((x, y))
