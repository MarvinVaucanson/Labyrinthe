import pygame
from pygame.locals import*

pygame.init()

fenetre = pygame.display.set_mode((1000,1000),RESIZABLE)


fond = pygame.image.load("fond-bleu-texture.jpg").convert()
fenetre.blit(fond, (0,0))

chrono = 45

princesse = pygame.image.load("princesse.png").convert_alpha()
position = princesse.get_rect()
fenetre.blit(princesse,(position))

potion_jaune = pygame.image.load("PotionJaune.png").convert_alpha()
potion_verte = pygame.image.load("PotionVerte.png").convert_alpha()
potion_bleu = pygame.image.load("PotionBleu.png").convert_alpha()

class Potion():
    
    def __init__(self, loc, potion_jaune, potion_verte, potion_bleu, liste_potion):
        liste_potions = liste_potion
        potion_vitesse = potion
        potion_temps = potion2
        potion_murs = potion3
        self.position_potion = loc
        
    def hasard(self, liste_potion):
        if laby != 3:
            pass
        else :
            potion_utilisé = numpy.random.choice(listes_potion)
        
    def vitesse(self):
        vitesse_princesse = vitesse_princesse + 5
        
    def temps(self):
        chrono = chrono + 10
        
    def murs(self):
        while chronos_mur != 3 :
            collisions = False
        mur_passé = 0
        collision = False
        while mur_passé < 3 :
            if position_princesse == mur :
                mur_passé = mur_passé + 1
                
P = Potion()
liste_potion = [potion_jaune, potion_bleu, potion_verte]
loc = Rect(x, y, 0, 0)
if laby == 32 :
    P.hasard()
if potion_utilisé == potion_jaune :
    P.temps
if potion_utilisé == potion_verte :
    P.vitesse
if potion_utilisé == potion_bleu :
    P.murs

        

pygame.display.flip()

"""if princesse.position == potion.position:
    chrono = chrono + 5"""

continuer = True
pygame.key.set_repeat(400,30)
while continuer:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN and event.key == K_DOWN:
            position = position.move(0,3)
        elif event.type == KEYDOWN and event.key == K_UP:
            position = position.move(0,-3)
        elif event.type == KEYDOWN and event.key == K_LEFT:
            position = position.move(-3,0)
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            position = position.move(3,0)
    fenetre.blit(fond,(0,0))
    fenetre.blit(princesse,position)
    #rafraichissement
    pygame.display.flip()

