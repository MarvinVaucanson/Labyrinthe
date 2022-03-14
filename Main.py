#le jeu de labyrinthe
###====# Bibliotheque #====###

import pygame
from pygame.locals import *
from random import randint, choice
from sys import exit
import matplotlib.pyplot as plt
from pile import Pile

###====# Class #====###

class Jeu :
    pass

class Minuteur : #un chrono de sec temps qui affiche fin une fois fini

    def __init__ (self, sec):
        self.sec = sec

    def temps (self):
        for i in range(self.sec):
            time.sleep(1)
            self.sec -= 1
        if self.sec == 0:
            print("Fin")

###====# Main #====###

###====# Temp #====###
a = Minuteur(10)
a.temps()

#lire dans un fichier
fichier = open("data.txt", "r")
print fichier.read()
fichier.close()

#ecrire dans un fichier
fichier = open("data.txt", "a")
fichier.write("Bonjour monde")
fichier.close()
