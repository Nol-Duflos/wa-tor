import random

Empty = 0
Fish = 1
Shark = 2

couleurs = ['#119DA4', '#119DA4', '#101913']
n_bin = 3


init_energy = {Fish: 20, Shark: 3}
fertility_thresholds = {Fish: 4, Shark: 12}

#On créer des classes, dans lesquelles on met des fonction, dans lesquelles on met des des self (variables d'instance)

class Creature():
    #Une créature marine vivant dans le monde de Wa-Tor

    def __init__(self, id, x, y, init_energy, fertility_threshold):
        self.id = id
        self.x = x
        self.y = y
        self.energy = init_energy
        self.fertility_threshold = fertility_threshold
        self.fertility = 0
        self.dead = False



class World():
    #Le monde de Wa-Tor
    def __init__(self, width=75, height=50):
        #Initialisation du monde de Wa-Tor

        self.width =  width
        self.height = height
        self.ncells = width * height
        self.grid = [[]*width for y in range(height)]
        self.creature = []
        #self sont les attributs et méthodes de la classe

    def spaw_creature(self, creature_id, x, y):
        creature = Creature(creature_id, x, y,
                            init_energy[creature_id],
                            fertility_thresholds [creature_id])
        self.creature.append(creature)
        self.grid[y][x] = creature

    def populate_world(self, nombreFish=120, nombreSharks=40):

        self.nombreFish = nombreFish
        self.nombreSharks = nombreSharks

        def place_creatures(ncreatures, creatur_id):

            for i in range(ncreatures):
                while True:
                    x, y = divmod(random.randrange(self.ncells), self.height)
                    if not self.grid[y][x]:
                        self.spaw_creature(creatur_id, x, y)
                        break

        place_creatures(self.nombreFish, Fish)
        place_creatures(self.nombreSharks, Shark)

    def getWorldImageArray(self):
        return [[self.grid[y][x].id if self.grid[y][x] else 0
                 for x in range(self.width)] for y in range(self.height)]
    

    def show_world

        