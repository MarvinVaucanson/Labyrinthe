import pygame
from pygame.locals import *
from random import randint, choice
from sys import exit
import matplotlib.pyplot as plt
from pile import Pile
import time


class Case:
    def __init__(self):
        self.murN = True
        self.murW = True
        self.murS = True
        self.murE = True
        self.vue = False


class Labyrinthe:
    def __init__(self, largeur, hauteur):
        pygame.init()
        pygame.display.set_caption('LABYRINTHE')
        self.fenetre = pygame.display.set_mode((640, 640))
        self.fond = pygame.image.load("fondSol.png").convert()
        self.fenetre.blit(self.fond, (0,0))
        self.largeur = largeur
        self.hauteur = hauteur
        self.laby = [[Case() for i in range (self.hauteur)]for i in range (self.largeur)]

    def __directions_possibles(self,i,j):

        directions = []
        if j < self.hauteur-1 and not self.laby[i][j+1].vue:
            directions.append('S')
        if j > 0 and not self.laby[i][j-1].vue:
            directions.append('N')
        if i < self.largeur-1 and not self.laby[i+1][j].vue:
            directions.append('E')
        if i > 0 and not self.laby[i-1][j].vue:
            directions.append('W')
        return directions


    def __abattre_mur(self,i,j,dir,pile):

        if dir == 'S': # on se dirige vers le sud
            self.laby[i][j].murS = False # on abat le mur sud de la case courante
            self.laby[i][j+1].murN = False # on abat le mur nord de la case située en-dessous de la case courante
            self.laby[i][j+1].vue = True # cette case est alors marquée comme vue
            pile.empiler((i, j+1)) # on stocke les coordonnées de cette case dans la pile
        elif dir == 'N': # on se dirige vers le nord
            self.laby[i][j].murN = False
            self.laby[i][j-1].murS = False
            self.laby[i][j-1].vue = True
            pile.empiler((i, j-1))
        elif dir == 'E': # on se dirige vers l'est
            self.laby[i][j].murE = False
            self.laby[i+1][j].murW = False
            self.laby[i+1][j].vue = True
            pile.empiler((i+1, j))
        elif dir == 'W': # on se dirige vers l' ouest
            self.laby[i][j].murW = False
            self.laby[i-1][j].murE = False
            self.laby[i-1][j].vue = True
            pile.empiler((i-1, j))

    def generer(self):

        pile = Pile()
        i,j = (randint(0,self.hauteur-1),randint(0,self.largeur-1))
        pile.empiler((i,j))
        self.laby[i][j].vue = True

        while not pile.est_vide():
            (i,j) = pile.depiler()
            directions = self.__directions_possibles(i,j)
            if len(directions) > 1:
                pile.empiler((i,j))
            if len(directions) >= 1:
                dir = choice(directions)
                self.__abattre_mur(i,j,dir,pile)

    def afficher(self):
        for i in range(self.largeur):
            color="r"
            pygame.draw.rect(self.fond,(84, 32, 14),pygame.Rect(0,0,640,640),3)
            for j in range(self.hauteur):
                if self.laby[i][j].murS:
                    pygame.draw.line(self.fond,(84, 32, 14),[int((i)*640/self.largeur),int((j+1)*640/self.largeur)], [int((i+1)*640/self.largeur),int((j+1)*640/self.largeur)],3)
                if self.laby[i][j].murE:
                    pygame.draw.line(self.fond,(84, 32, 14),[int((i+1)*640/self.largeur),int(j*640/self.largeur)], [int((i+1)*640/self.largeur),int((j+1)*640/self.largeur)],3)

        pygame.display.flip()


class Minuteur :

    def __init__ (self, sec):
        self.sec = sec
        self.laby = Labyrinthe(nb_cases,nb_cases)
        self.font = pygame.font.Font('Retro Gaming.ttf', 30)
        self.start = time.time()

    def temps (self):
        while self.sec > 0 :
            self.sec -= 1
            return self.sec

    def affichertemps(self):
        a=int(abs(time.time() - self.start - self.sec))
        self.laby.fenetre.blit(self.font.render(str(a), True, (84, 32, 14)), (570, 5))
        if a == 0 :
            pygame.quit()


class Joueur:
    def __init__(self,image,nb_cases):
        self.image = pygame.image.load(image).convert_alpha()
        self.orientation = 1
        self.position = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (int(640/nb_cases)-10,int(640/nb_cases)-10))
        pygame.display.flip()
    def gauche (self):
        self.joueur = pygame.transform.rotate(self.image,(self.orientation-4)*90)
        self.orientation = 4
        self.position = self.position.move(-3,0)
    def droite (self):
        self.joueur = pygame.transform.rotate(self.image,(self.orientation-2)*90)
        self.orientation = 2
        self.position = self.position.move(3,0)
    def haut (self):
        self.joueur = pygame.transform.rotate(self.image,(self.orientation-1)*90)
        self.position = self.position.move(0,-3)
        self.orientation = 1
    def bas (self):
        self.joueur = pygame.transform.rotate(self.image,(self.orientation-3)*90)
        self.orientation = 3
        self.position = self.position.move(0,3)


class Jeu:
    def __init__(self):
        #nb_cases = 10
        self.laby = Labyrinthe(nb_cases,nb_cases)
        self.laby.generer()
        self.laby.afficher()
        self.joueur = Joueur('princesse.png',nb_cases)
        self.minuteur = Minuteur(180)
        self.continuer = True
        self.laby.fenetre.blit(self.joueur.image,self.joueur.position)
        pygame.display.flip()

    def loop(self):
        pygame.key.set_repeat(20, 20)
        self.laby.fenetre.blit(self.laby.fond,(0,0))

        while self.continuer :

            self.laby.fenetre.blit(self.laby.fond,(0,0))
            self.laby.fenetre.blit(self.laby.fenetre,(0,0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.continuer = False
                elif event.type == KEYDOWN:
                    if pygame.key.get_pressed()[K_DOWN]:
                        self.joueur.bas()
                    if pygame.key.get_pressed()[K_UP]:
                        self.joueur.haut()
                    if pygame.key.get_pressed()[K_LEFT]:
                        self.joueur.gauche()
                    if pygame.key.get_pressed()[K_RIGHT]:
                        self.joueur.droite()

            self.laby.fenetre.blit(self.joueur.image,self.joueur.position)
            self.minuteur.affichertemps()
            pygame.display.flip()
        pygame.quit()

### Programme principal ###
if __name__=='__main__':
    nb_cases = 10
    jeu = Jeu()
    jeu.loop()