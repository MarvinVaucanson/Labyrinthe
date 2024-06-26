import pygame
from pygame.locals import *
from random import*
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
        self.fond = pygame.image.load("images/fondSol.png").convert()
        self.fenetre.blit(self.fond, (0,0))
        self.largeur = largeur
        self.hauteur = hauteur
        self.laby = [[Case() for i in range (self.hauteur)]for i in range (self.largeur)]
        self.murs = []
        self.arrivee = pygame.Rect(640-int(640/self.largeur/2)+10,640-int(640/self.largeur/2)+10,int(640/self.largeur),int(640/self.largeur))
        self.fini = False


    def __directions_possibles(self,i,j):
        # code à décommenter et à compléter : exercice n°4

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
        # code à décommenter et à compléter : exercice n°5

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
        # code à décommenter et à compléter : exercice n°6

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
            pygame.draw.rect(self.fond,(84,32,14),pygame.Rect(0,0,640,640),3)
            for j in range(self.hauteur):
                if self.laby[i][j].murS:
                    rectangle = pygame.draw.rect(self.fond,(84,32,14),(int((i)*640/self.largeur),int((j+1)*640/self.largeur),int(640/self.largeur)+3,3))
                    self.murs.append(rectangle)
                if self.laby[i][j].murE:
                    rectangle = pygame.draw.rect(self.fond,(84,32,14),(int((i+1)*640/self.largeur),int(j*640/self.largeur),3,int(640/self.largeur)+3))
                    self.murs.append(rectangle)
        pygame.draw.circle(self.fond,(255,0,0),(int((self.largeur-1)*640/self.largeur)+int((640/self.largeur)/2),int((self.largeur-1)*640/self.largeur)+int((640/self.largeur)/2)),10)

        #self.fenetre.blit()
        pygame.display.flip()
        
    def effacer_mur(self,mur):
        pygame.draw.rect(self.fond,(193, 196, 192),mur,3)
        pygame.display.flip()
        
        
                
class Minuteur :

    def __init__ (self, sec):
        self.sec = sec
        self.laby = Labyrinthe(nb_cases,nb_cases)
        self.font = pygame.font.SysFont('impact', 30)
        self.start = time.time()

    def temps (self):
        while self.sec > 0 :
            print("test")
            self.sec -= 1
            return self.sec

    def affichertemps(self):
        a=int(abs(time.time() - self.start - self.sec))
        self.laby.fenetre.blit(self.font.render(str(a), True, (84, 32, 14)), (590, 5))
        if a == 0 :
            pygame.quit()        
            
    def augmenter_temps(self) :
        self.sec = self.sec + 20

class Joueur:
    def __init__(self,image,nb_cases,murs):
        self.image = pygame.image.load(image).convert_alpha()
        self.orientation = 1
        self.image = pygame.transform.scale(self.image, (int(640/nb_cases)-16,int(640/nb_cases)-16))
        self.position = self.image.get_rect()
        self.murs = murs
        self.vitesse = 3
        self.casser = False
        self.mur_casse = None
        pygame.display.flip()
    def gauche (self):
        if self.position[0] >= 0 and self.collision(4) == False:
            self.joueur = pygame.transform.rotate(self.image,(self.orientation-4)*90)
            self.orientation = 4
            self.position = self.position.move(-self.vitesse,0)
    def droite (self):
        if self.position[0] <= 640-self.position[2] and self.collision(2) == False:
            self.joueur = pygame.transform.rotate(self.image,(self.orientation-2)*90)
            self.orientation = 2
            self.position = self.position.move(self.vitesse,0)
    def haut (self):
        if self.position[1] >= 0 and self.collision(1) == False:
            self.joueur = pygame.transform.rotate(self.image,(self.orientation-1)*90)
            self.position = self.position.move(0,-self.vitesse)
            self.orientation = 1
    def bas (self):
        if self.position[1] <= 640-self.position[3] and self.collision(3) == False:
            self.joueur = pygame.transform.rotate(self.image,(self.orientation-3)*90)
            self.orientation = 3
            self.position = self.position.move(0,self.vitesse)
    def collision (self,direction):
        '''Méthode qui renvoie True si la princesse essaie de se diriger sur un mur'''
        self.test = self.position
        self.test[3] += 0
        if direction == 1:
            self.test = self.test.move(0,-self.vitesse)
        elif direction == 2:
            self.test = self.test.move(self.vitesse,0)
        elif direction == 3:
            self.test = self.test.move(0,self.vitesse)
        elif direction == 4:
            self.test = self.test.move(-self.vitesse,0)
        for i in range (len(self.murs)):
            if pygame.Rect.colliderect(self.test,self.murs[i]):
                if self.casser == True :
                    self.casser = False
                    self.mur_casse = self.murs[i]
                    del self.murs[i]
                return True
        return False
        
    def potions(self, potion):
        if pygame.Rect.colliderect(self.position,potion.position): 
            return True
    
    def fin_laby(self,arrivee):
        if pygame.Rect.colliderect(self.position,arrivee):
            return True
            
    def augmenter_vitesse(self):
        self.vitesse = self.vitesse + 1
        
    def casser_mur(self) : 
        self.casser = True
        
class Jeu:
    def __init__(self):
        self.continuer = True
        self.minuteur = Minuteur(150)
        self.touches = [K_DOWN,K_UP,K_LEFT,K_RIGHT]
        self.jeu_fini = False
        self.laby_fini = False
        self.nb_cases = 5
        self.score = 0
        self.choix_potions = ["verte", "jaune", "bleue"]
        self.potion = choice(self.choix_potions)
    def loop(self):
        pygame.key.set_repeat(20, 20)
        while self.continuer:
            laby = Labyrinthe(self.nb_cases,self.nb_cases)
            laby.generer()
            laby.afficher()
            self.potion = choice(self.choix_potions)
            if self.potion == "verte" :
                potion = Potions('images/PotionVerte.png', self.nb_cases)
            elif self.potion == "jaune" :
                potion = Potions('images/PotionJaune.png', self.nb_cases)
            elif self.potion == "bleue" :
                potion = Potions('images/PotionBleue.png', self.nb_cases)
            laby.fenetre.blit(potion.image,(potion.x,potion.y))
            joueur = Joueur('images/princesse.png',self.nb_cases,laby.murs)
            laby.fenetre.blit(joueur.image,joueur.position)
            potions = True
            laby.fenetre.blit(laby.fenetre,(0,0))
            pygame.display.flip()
            while laby.fini == False:
                laby.fenetre.blit(laby.fond,(0,0))
                laby.fenetre.blit(laby.fenetre,(0,0))
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        self.continuer = False
                        laby.fini = True
                        self.jeu_fini = True
                    elif event.type == KEYDOWN:
                        if pygame.key.get_pressed()[self.touches[0]]:
                            joueur.bas()
                        if pygame.key.get_pressed()[self.touches[1]]:
                            joueur.haut()
                        if pygame.key.get_pressed()[self.touches[2]]:
                            joueur.gauche()
                        if pygame.key.get_pressed()[self.touches[3]]:
                            joueur.droite()
                        fin = joueur.fin_laby(laby.arrivee)
                        if fin == True:
                            laby.fini = True
                        if potions == True:
                            if joueur.potions(potion) == True :
                                if self.potion == "verte" :
                                    joueur.augmenter_vitesse()
                                elif self.potion == "jaune" :
                                    self.minuteur.augmenter_temps()
                                elif self.potion == "bleue" :
                                    joueur.casser_mur()
                                del potion
                                potions = False
                        if joueur.mur_casse != None:
                            laby.effacer_mur(joueur.mur_casse)
                            joueur.mur_casse = None
                laby.fenetre.blit(joueur.image,joueur.position)
                if potions == True:
                    laby.fenetre.blit(potion.image,(potion.x,potion.y))
                self.minuteur.affichertemps()
                pygame.display.flip()
            self.nb_cases = self.nb_cases + 2
            self.score = self.score + 1
        pygame.quit()
        
        
        
### Classe Potions ###

class Potions :
    def __init__(self, image, nb_cases):
        self.x = int((randint(0, nb_cases-1))*640/nb_cases)
        self.y = int((randint(0, nb_cases-1))*640/nb_cases)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (int(640/nb_cases)-16,int(640/nb_cases)-16))
        self.position = pygame.Rect(self.x, self.y, (int(640/nb_cases)-16), (int(640/nb_cases)-16))
        pygame.display.flip()
        



### Programme principal ###
if __name__=='__main__':
    # à compléter : exercice n°3
    """laby = Labyrinthe(6,8)
    #laby.afficher()
    laby.laby[0][0].murS = False
    laby.laby[1][0].murS = False
    laby.laby[1][1].murW = False
    laby.laby[2][0].murW = False
    laby.laby[2][0].murS = False
    laby.laby[5][7].murS = False
    laby.laby[4][4].murW = False
    laby.afficher()"""
    nb_cases = 10
    #laby = Labyrinthe(nb_cases,nb_cases)
    #joueur = Joueur('Tank2V1.png',nb_cases)
    #laby.generer()
    #laby.afficher()
    jeu = Jeu()
    jeu.loop()
