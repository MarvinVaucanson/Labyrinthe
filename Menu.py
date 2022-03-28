import pygame, sys
from pygame.locals import*


class Fenetres():
    
    def chargement():
        width = 640
        height = 640
        pygame.init()
        fenetre = pygame.display.set_mode((width, height))
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
                        pygame.display.update()
                        Fenetres.menu()
                        pygame.display.update()
                        
            pygame.display.flip()
        pygame.quit()
        
    
    
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
        
        jouer = pygame.image.load('Textures/jouer2.png').convert_alpha()
        jouer = pygame.transform.scale(jouer, (300,75))
        fenetre.blit(jouer,(170,250))
        
        credits = pygame.image.load('Textures/credits2.png').convert_alpha()
        credits = pygame.transform.scale(credits, (300,75))
        fenetre.blit(credits,(170,370))
        
        quitter = pygame.image.load('Textures/quitter2.png').convert_alpha()
        quitter = pygame.transform.scale(quitter, (300,75))
        fenetre.blit(quitter,(170,490))
        
        """select1 = pygame.image.load('Textures/select.png').convert_alpha()
        select1 = pygame.transform.scale(select1, (300,75))
        fenetre.blit(jouer,(170,250))"""
        
        continuer = True
        while continuer:
            
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False
        
        # BOUTON JOUER #
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 170 <= mouse[0] <= 570 and 250 <= mouse[1] <= 350:
                            continuer = False
                            pygame.display.update()
                            continuer = True
                            pygame.display.update()
                            jeu=Jeu()
                            jeu.loop()
                            pygame.display.update()
        
        # BOUTTON CREDITS #
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 170 <= mouse[0] <= 570 and 370 <= mouse[1] <= 470:
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
        
        retour = pygame.image.load('Textures/retour.png').convert_alpha()
        retour = pygame.transform.scale(retour, (150,150))
        fenetre.blit(jouer,(550,550))
    
        continuer = True
        while continuer:
            
            mouse = pygame.mouse.get_pos()
            
            
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
        
        retour = pygame.image.load('Textures/retour.png').convert_alpha()
        retour = pygame.transform.scale(retour, (150,150))
        fenetre.blit(jouer,(550,550))
    
        continuer = True
        while continuer:
    
            mouse = pygame.mouse.get_pos()
            
    
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

    Fenetres.chargement()
    
