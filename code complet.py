import pygame
import sys
from pygame.locals import *
from random import*
from sys import exit
import matplotlib.pyplot as plt
from pile import Pile
#from Menu import Fenetres
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
        self.fond = pygame.image.load("Textures/fondSol.png").convert()
        self.fenetre.blit(self.fond, (0,0))
        self.largeur = largeur
        self.hauteur = hauteur
        self.laby = [[Case() for i in range (self.hauteur)]for i in range (self.largeur)]
        self.murs = []
        self.arrivee = pygame.Rect(640-int(640/self.largeur/2)+10,640-int(640/self.largeur/2)+10,int(640/self.largeur),int(640/self.largeur))
        self.fini = False


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
            pygame.draw.rect(self.fond,(84,32,14),pygame.Rect(0,0,640,640),3)
            for j in range(self.hauteur):
                if self.laby[i][j].murS:
                    rectangle = pygame.draw.rect(self.fond,(84,32,14),(int((i)*640/self.largeur),int((j+1)*640/self.largeur),int(640/self.largeur)+3,3))
                    self.murs.append(rectangle)
                if self.laby[i][j].murE:
                    rectangle = pygame.draw.rect(self.fond,(84,32,14),(int((i+1)*640/self.largeur),int(j*640/self.largeur),3,int(640/self.largeur)+3))
                    self.murs.append(rectangle)
        arrivee = pygame.image.load("Textures/fondSol.png").convert()
        arrivee = pygame.transform.scale(arrivee, (int(640/self.largeur)-16,int(640/self.largeur)-16))

        #self.fenetre.blit()
        pygame.display.flip()

    def effacer_mur(self,mur):
        pygame.draw.rect(self.fond,(193, 196, 192),mur,3)
        pygame.display.flip()



class Minuteur :
    def __init__ (self, sec):
        self.aleatoire = randint(10, sec)
        self.sec = sec
        nb_cases = 5
        self.laby = Labyrinthe(nb_cases,nb_cases)
        self.font = pygame.font.SysFont('impact', 30)
        self.couleur = (84,32,14)
        self.start = time.time()

    def temps (self):
        while self.sec > 0 :
            print("test")
            self.sec -= 1
            return self.sec

    def affichertemps(self):
        a=int(abs(time.time() - self.start - self.sec))
        if a <= 10:
            self.couleur= (250,0,0)
        self.laby.fenetre.blit(self.font.render(str(a), True, self.couleur), (590, 5))
        if a == 0 :
            continuer = False
            pygame.display.update()
            continuer = True
            pygame.display.update()
            fenetres.fin()
            pygame.display.update()

    def augmenter_temps(self) :
        self.sec = self.sec + 20

    def temps_aleatoire(self):
        a=int(abs(time.time() - self.start - self.sec))
        if a <= self.aleatoire and a > self.aleatoire-10:
            self.laby.fenetre.blit(self.font.render("Attention inversion des touches !!!", True, (255, 0, 0)), (10, 0))
            return True
        return False

class Joueur:
    def __init__(self,image,nb_cases,murs):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(640/nb_cases)-16,int(640/nb_cases)-16))
        self.position = self.image.get_rect()
        self.murs = murs
        self.vitesse = 4
        self.casser = False
        self.mur_casse = None
        pygame.display.flip()
   
    def gauche (self):
        if self.position[0] >= 0 and self.collision(4) == False:
            self.position = self.position.move(-self.vitesse,0)
   
    def droite (self):
        if self.position[0] <= 640-self.position[2] and self.collision(2) == False:
            self.position = self.position.move(self.vitesse,0)
   
    def haut (self):
        if self.position[1] >= 0 and self.collision(1) == False:
            self.position = self.position.move(0,-self.vitesse)
  
    def bas (self):
        if self.position[1] <= 640-self.position[3] and self.collision(3) == False:
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
        item = pygame.mixer.Sound('Audio/blop.wav')
        pygame.key.set_repeat(20, 20)
        while self.continuer:
            laby = Labyrinthe(self.nb_cases,self.nb_cases)
            laby.generer()
            laby.afficher()
            self.potion = choice(self.choix_potions)
            arrivee = pygame.image.load("Textures/porte.png").convert_alpha()
            arrivee = pygame.transform.scale(arrivee, (int(640/laby.largeur)-16,int(640/laby.largeur)-16))
            if self.potion == "verte" :
                potion = Potions('Textures/PotionVerte.png', self.nb_cases)
            elif self.potion == "jaune" :
                potion = Potions('Textures/PotionJaune.png', self.nb_cases)
            elif self.potion == "bleue" :
                potion = Potions('Textures/PotionBleue.png', self.nb_cases)
            laby.fenetre.blit(potion.image,(potion.x,potion.y))
            joueur = Joueur('Textures/princesse.png',self.nb_cases,laby.murs)
            laby.fenetre.blit(joueur.image,joueur.position)
            potions = True
            laby.fenetre.blit(laby.fenetre,(0,0))
            pygame.display.flip()
            while laby.fini == False:
                laby.fenetre.blit(laby.fond,(0,0))
                laby.fenetre.blit(laby.fenetre,(0,0))
                laby.fenetre.blit(arrivee,(int((self.nb_cases-1)*640/self.nb_cases)+6,int((self.nb_cases-1)*640/self.nb_cases)+6))
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
                                    pygame.mixer.Sound.play(item)
                                    joueur.augmenter_vitesse()
                                elif self.potion == "jaune" :
                                    pygame.mixer.Sound.play(item)
                                    self.minuteur.augmenter_temps()
                                elif self.potion == "bleue" :
                                    pygame.mixer.Sound.play(item)
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
                inversion_touches = self.minuteur.temps_aleatoire()
                if inversion_touches == True:
                    self.touches = [K_UP,K_DOWN,K_RIGHT,K_LEFT]
                else:
                    self.touches = [K_DOWN,K_UP,K_LEFT,K_RIGHT]
                pygame.display.flip()
            self.nb_cases = self.nb_cases + 2
            self.score = self.score + 1
        self.recuperer_score()
        time.sleep(3)
        pygame.quit()
        sys.exit()
        
    def recuperer_score(self):
        self.score = str(self.score)


class Potions :
    def __init__(self, image, nb_cases):
        self.x = int((randint(0, nb_cases-1))*640/nb_cases)
        self.y = int((randint(0, nb_cases-1))*640/nb_cases)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (int(640/nb_cases)-16,int(640/nb_cases)-16))
        self.position = pygame.Rect(self.x, self.y, (int(640/nb_cases)-16), (int(640/nb_cases)-16))
        pygame.display.flip()


class Fenetres():
    
    def __init__(self):
        self.jeu = None
        

    def chargement(self):
        pygame.init()
        fenetre = pygame.display.set_mode((640,640))
        pygame.display.set_caption('Lancement En Cours ...')

        fond = pygame.image.load("Textures/Chargement.png").convert()
        fenetre.blit(fond,(0,0))

        continuer = True
        while continuer:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continuer = False

                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        continuer = False
                        pygame.display.update()
                        continuer = True
                        pygame.display.flip
                        self.menu()
                        pygame.display.flip

            pygame.display.update()
        pygame.quit()



    def menu(self):
        clic = pygame.mixer.Sound('Audio/clic.wav')
        pygame.init()
        fenetre = pygame.display.set_mode((640, 640))
        pygame.display.set_caption('Bienvenue dans notre labyrinthe !')

        fond = pygame.image.load("Textures/fondMenu.png").convert()
        fenetre.blit(fond,(0,0))

        infos = pygame.image.load('Textures/BoutonOptions.png').convert_alpha()
        infos = pygame.transform.scale(infos, (75,75))
        fenetre.blit(infos,(520,520))

        Sponsor = pygame.image.load('Textures/logoCochonLicorne2.png').convert_alpha()
        Sponsor = pygame.transform.scale(Sponsor, (300,75))
        fenetre.blit(Sponsor,(0,535))

        jouer = pygame.image.load('Textures/jouer2.png').convert_alpha()
        jouer = pygame.transform.scale(jouer, (300,75))
        fenetre.blit(jouer,(170,250))

        credits = pygame.image.load('Textures/credits2.png').convert_alpha()
        credits = pygame.transform.scale(credits, (300,75))
        fenetre.blit(credits,(170,370))

        quitter = pygame.image.load('Textures/quitter2.png').convert_alpha()
        quitter = pygame.transform.scale(quitter, (300,75))
        fenetre.blit(quitter,(170,490))


        pygame.display.flip()

        continuer = True
        while continuer:

            mouse = pygame.mouse.get_pos()
            selec = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False




        # BOUTON JOUER #
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 170 <= mouse[0] <= 570 and 250 <= mouse[1] <= 350:
                            pygame.mixer.Sound.play(clic)
                            continuer = False
                            pygame.display.update()
                            continuer = True
                            pygame.display.update()
                            self.jeu=Jeu()
                            self.jeu.loop()
                            pygame.display.update()

        # BOUTTON CREDITS #
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 170 <= mouse[0] <= 570 and 370 <= mouse[1] <= 470:
                            pygame.mixer.Sound.play(clic)
                            continuer = False
                            pygame.display.update()
                            continuer = True
                            pygame.display.update()
                            self.screenCredits()
                            pygame.display.update()

        # BOUTTON INFOS #
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 500 <= mouse[0] <= 600 and 500 <= mouse[1] <= 600:
                            pygame.mixer.Sound.play(clic)
                            continuer = False
                            pygame.display.update()
                            continuer = True
                            pygame.display.update()
                            self.screenInfos()
                            pygame.display.update()

        # BOUTTON QUITTER #
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 170 <= mouse[0] <= 570 and 490 <= mouse[1] <= 590:
                            pygame.mixer.Sound.play(clic)
                            continuer = False
                            pygame.quit()
                            sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continuer = False
                        pygame.quit()
                        sys.exit()

        pygame.display.update()


    def screenCredits(self):
        clic = pygame.mixer.Sound('Audio/clic.wav')
        pygame.init()
        fenetre = pygame.display.set_mode((640,640))
        pygame.display.set_caption('Crédits')
        fond = pygame.image.load("Textures/fondMenu.png").convert()
        rectscreen = fenetre.get_rect()
        fenetre.blit(fond,(0,0))

        credits = pygame.image.load("Textures/Nomscredits.png").convert_alpha()
        fenetre.blit(credits,(190,300))

        retour = pygame.image.load('Textures/retour.png').convert_alpha()
        retour = pygame.transform.scale(retour, (50,50))
        fenetre.blit(retour,(550,550))

        continuer = True
        while continuer:

            mouse = pygame.mouse.get_pos()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 550 <= mouse[0] <= 600 and 550 <= mouse[1] <= 600:
                        pygame.mixer.Sound.play(clic)
                        continuer = False
                        pygame.display.update()
                        continuer = True
                        pygame.display.update()
                        self.menu()
                        pygame.display.update()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continuer = False

            pygame.display.update()
        pygame.quit()

    def scoreboard(self):
        clic = pygame.mixer.Sound('Audio/clic.wav')
        pygame.init()
        fenetre = pygame.display.set_mode((640,640))
        pygame.display.set_caption('Scoreboard')
        fond = pygame.image.load("Textures/fond.png").convert()
        rectscreen = fenetre.get_rect()
        fenetre.blit(fond,(0,0))

        retour = pygame.image.load('Textures/retour.png').convert_alpha()
        retour = pygame.transform.scale(retour, (50,50))
        fenetre.blit(retour,(550,550))

        continuer = True
        while continuer:

            mouse = pygame.mouse.get_pos()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 550 <= mouse[0] <= 600 and 550 <= mouse[1] <= 600:
                        pygame.mixer.Sound.play(clic)
                        continuer = False
                        pygame.display.update()
                        continuer = True
                        pygame.display.update()
                        self.fin()
                        pygame.display.update()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continuer = False

            pygame.display.update()
        pygame.quit()


    def screenInfos(self):
        clic = pygame.mixer.Sound('Audio/clic.wav')
        pygame.init()
        fenetre = pygame.display.set_mode((640,640))
        pygame.display.set_caption('Infos')
        fond = pygame.image.load("Textures/tuto.png").convert()
        rectscreen = fenetre.get_rect()
        fenetre.blit(fond,(0,0))

        retour = pygame.image.load('Textures/retour.png').convert_alpha()
        retour = pygame.transform.scale(retour, (50,50))
        fenetre.blit(retour,(550,550))

        continuer = True
        while continuer:

            mouse = pygame.mouse.get_pos()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 550 <= mouse[0] <= 600 and 550 <= mouse[1] <= 600:
                        pygame.mixer.Sound.play(clic)
                        continuer = False
                        pygame.display.update()
                        continuer = True
                        pygame.display.update()
                        self.menu()
                        pygame.display.update()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer = False

            pygame.display.update()
        pygame.quit()

    def fin(self):
        clic = pygame.mixer.Sound('Audio/clic.wav')
        pygame.init()
        fenetre = pygame.display.set_mode((640,640))
        pygame.display.set_caption('Bravo !!!')

        fond = pygame.image.load("Textures/screenFin.png").convert()
        fenetre.blit(fond,(0,0))

        rejouer = pygame.image.load('Textures/rejouer.png').convert_alpha()
        rejouer = pygame.transform.scale(rejouer, (75,75))
        fenetre.blit(rejouer,(40,225))

        home = pygame.image.load('Textures/home.png').convert_alpha()
        home = pygame.transform.scale(home, (75,75))
        fenetre.blit(home,(40,325))

        scoreboard = pygame.image.load('Textures/scoreboard.png').convert_alpha()
        scoreboard = pygame.transform.scale(scoreboard, (75,75))
        fenetre.blit(scoreboard,(40,425))
        
        fenetre.blit(pygame.font.SysFont('Liberation',30).render(("Score : "+ str(self.jeu.score)), True, (84, 32, 14)), (500, 5))
        
        continuer = True
        while continuer:

            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continuer = False

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 40 <= mouse[0] <= 105 and 225 <= mouse[1] <= 300:
                            pygame.mixer.Sound.play(clic)
                            continuer = False
                            pygame.display.update()
                            continuer = True
                            pygame.display.update()
                            jeu=Jeu()
                            jeu.loop()
                            pygame.display.update()

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 40 <= mouse[0] <= 105 and 325 <= mouse[1] <= 400:
                            pygame.mixer.Sound.play(clic)
                            continuer = False
                            pygame.display.update()
                            continuer = True
                            pygame.display.update()
                            self.menu()
                            pygame.display.update()

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 40 <= mouse[0] <= 105 and 425 <= mouse[1] <= 500:
                            pygame.mixer.Sound.play(clic)
                            continuer = False
                            pygame.display.update()
                            continuer = True
                            pygame.display.update()
                            self.scoreboard()
                            pygame.display.update()

            pygame.display.update()
        pygame.quit()
        sys.exit()
        



### Programme principal ###
if __name__=='__main__':

    #laby = Labyrinthe(nb_cases,nb_cases)
    #joueur = Joueur('Tank2V1.png',nb_cases)
    #laby.generer()
    #laby.afficher()
    fenetres = Fenetres()
    fenetres.chargement()
    #Fenetres.fin()



    #Fenetres.chargement()
