import random

Empty = 0
Fish = 1
Shark = 2

couleurs = ['#119DA4', '#119DA4', '#101913']
n_bin = 3

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