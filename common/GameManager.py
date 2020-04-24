#coding: utf-8

import pygame
import entity.Tomo as entity

"""
Class qui permetra de packagé, les composants lié a jeux 
"""
class GameManager:
    def __init__(self, title: str, w: int, h: int, frameRateLimit: int):
        print(f"{self} is created.")
        self.surfaceSize = (w, h)
        self.title = title
        self.surface = None 
        self.close = False 
        self.frameRate = frameRateLimit

        # Objets du jeux 
        self.tomo = entity.Tomo("Nom du Tomo", 1) 

    def __del__(self):
        print(f"{self} is released.")
        pygame.quit()

    def initialize(self):
        try:
            pygame.init()       
            self.surface = pygame.display.set_mode(self.surfaceSize)
        except:
            return False
        return True
    
    def run(self):
        dt = 1
        while not self.close:

            start = pygame.time.get_ticks() # Récupere le point temporel au début de la boucle 

            pygame.display.set_caption(f"{self.title} {1000 / dt} FPS") # Actualise le titre en affichant le nom d'image afficher par seconde

            # Gérer les événements de l'utilisateur avec ses périphérique 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close = True 

            # Mise a jour du compotement des élements de jeux 
            self.tomo.update(dt)

            # Affichage
            self.tomo.draw(self.surface)
            pygame.display.flip()
            # Calcul du temps d'execution de la boucle 
            if pygame.time.get_ticks() - start < 1000.0 / self.frameRate: # Si le temps d'execution de la boucle moin long que le temps d'execution pour effectuer 60 tour de boucle par seconde alors : 
                # On prend la distance en temps qui l'est sépare
                dt = (1000.0 / self.frameRate) - (pygame.time.get_ticks() - start)
                pygame.time.delay(int(dt)) # On attends 
   
        
 



            
            

            
            
        




        