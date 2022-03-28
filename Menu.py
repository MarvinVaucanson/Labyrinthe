import pygame, sys
from pygame.locals import*
pygame.mixer.init() 



width = 640
height = 640
pygame.init()
fenetre = pygame.display.set_mode((width, height))
pygame.display.set_caption('Lancement En Cours ...')
    
fond = pygame.image.load("Textures/Chargement.png").convert()
fenetre.blit(fond,(0,0))
    
    
# IMAGES #

jouer_img = pygame.image.load('Textures/jouer2.png').convert_alpha()
credits_img = pygame.image.load('Textures/credits2.png').convert_alpha()
quitter_img = pygame.image.load('Textures/quitter2.png').convert_alpha()
retour_img = pygame.image.load('Textures/retour.png').convert_alpha()
select1_img = pygame.image.load('Textures/select.png').convert_alpha()


class Bouton():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale),int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        fenetre.blit(self.image, (self.rect.x, self.rect.y))

    # BOUTONS #
    
jouer_bouton = Bouton(170, 250, jouer_img, 0.75)
credits_bouton = Bouton(170, 370, credits_img, 0.75)
quitter_bouton = Bouton(170, 490, quitter_img, 0.75)
retour_bouton = Bouton(550, 550, retour_img, 0.35)

'''class Chargement(pygame.sprite.Sprite):
    
    ecranChargement = pygame.image.load("Textures/SpriteChargement.png").convert_alpha()
    sequences = [(0,13,True)]
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = Chargement.ecranChargement.subsurface(pygame.Rect(0,0,640,640))
        self.rect = pygame.Rect(0,0,640,640)
        self.rect.botton = HEIGTH
        
        self.numeroSequence = 0
        self.flip = False
        
        self.deltaTime = 0
        self.vitesse = int(round(26/FPS))'''
    
    
    
class Fenetres():
    
    def menu():
        width = 640
        height = 640
        pygame.init()
        fenetre = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Bienvenue dans notre labyrinthe !')
        
        fond = pygame.image.load("Textures/fondMenu.png").convert()
        fenetre.blit(fond,(0,0))
        
        infos = pygame.image.load('Textures/BoutonOptions.png').convert_alpha()
        infos = pygame.transform.scale(infos, (75,75))
        fenetre.blit(infos,(520,520))
        
        Sponsor = pygame.image.load('Textures/logoCochonLicorne2.png').convert_alpha()
        Sponsor = pygame.transform.scale(Sponsor, (300,75))
        fenetre.blit(Sponsor,(0,535))
        continuer = True
        while continuer:
        
            mouse = pygame.mouse.get_pos()
            jouer_bouton.draw()
            credits_bouton.draw()
            quitter_bouton.draw()
        
            pygame.display.update()
        
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False
        
        # BOUTON JOUER #
                '''if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 170 <= mouse[0] <= 570 and 250 <= mouse[1] <= 350:
                            pygame.display.update()'''
        
        # BOUTTON CREDITS #
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 170 <= mouse[0] <= 570 and 370 <= mouse[1] <= 470:
                            '''clic.play()'''
                            continuer = False
                            pygame.display.update()
                            continuer = True
                            pygame.display.update()
                            Fenetres.screenCredits()
                            pygame.display.update()
        
        # BOUTTON INFOS #
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 500 <= mouse[0] <= 600 and 500 <= mouse[1] <= 600:
                            continuer = False
                            pygame.display.update()
                            continuer = True
                            pygame.display.update()
                            Fenetres.screenInfos()
                            pygame.display.update()
        
        # BOUTTON QUITTER #
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 170 <= mouse[0] <= 570 and 490 <= mouse[1] <= 590:
                            continuer = False
                            pygame.quit()
    
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continuer = False
                        pygame.quit()
        
        pygame.display.update()
    
        
    def screenCredits():
        width = 640
        height = 640
        pygame.init()
        fenetre = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Crédits')
        fond = pygame.image.load("Textures/fondMenu.png").convert()
        rectscreen = fenetre.get_rect()
        fenetre.blit(fond,(0,0))
    
        credits = pygame.image.load("Textures/Nomscredits.png").convert_alpha()
        fenetre.blit(credits,(190,300))
    
        continuer = True
        while continuer:
            
            mouse = pygame.mouse.get_pos()
            retour_bouton.draw()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False
                    
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 550 <= mouse[0] <= 600 and 550 <= mouse[1] <= 600:
                        continuer = False
                        pygame.display.update()
                        continuer = True
                        pygame.display.update()
                        Fenetres.menu()
                        pygame.display.update()
                                        
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continuer = False
                        
            pygame.display.update()
        pygame.quit()
    
        
    def screenInfos():
        width = 640
        height = 640
        pygame.init()
        fenetre = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Infos')
        fond = pygame.image.load("Textures/tuto.png").convert()
        rectscreen = fenetre.get_rect()
        fenetre.blit(fond,(0,0))
    
        continuer = True
        while continuer:
    
            mouse = pygame.mouse.get_pos()
            retour_bouton.draw()
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False
    
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 550 <= mouse[0] <= 600 and 550 <= mouse[1] <= 600:
                        continuer = False
                        pygame.display.update()
                        continuer = True
                        pygame.display.update()
                        Fenetres.menu()
                        pygame.display.update()
                        
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer = False
    
            pygame.display.update()
        pygame.quit()



    ### MENU DE BASE ###
if __name__=='__main__':    
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
                    pygame.display.update()
                    Fenetres.menu()
                    pygame.display.update()
                    
                        
        pygame.display.update()
    pygame.quit()
    
