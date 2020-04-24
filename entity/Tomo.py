#coding: utf-8
import time
from typing import Tuple

import pygame

"""
A mettre dans un package de fonction utilitaire par exemple 
Va servir a transformer des coordonnées normaliser entre -1 et 1 vers des coordonnées 
ecran 0 et 800 et 0 et 600 par exemple 
"""
def linearInterpolation(xa: float, ya: float, xb: float, yb: float, x: float):
    return ( (xb - x) / (xb - xa) ) * ya + ((x - xa) / (xb - xa)) * yb
"""

Class Tomo qui servira a manipuler le Tomo
"""
class Tomo:
    """
    Instancie un Tomo
    """
    def __init__(self, name: str, age: int):
        self.moralState = ("Bonheur", "Tristesse", "Colere", "Peur", "Faim", "Mort") # Etat possible pour le Tomo
        self.moralID = 0 # Au début du commence "Heureux"
        self.name = name # Nom en chaine de caractère
        self.health = 100 # Taux de point de vie en %
        self.age = 1 # Age en tant qu'entier 
        self.is_alive = True # Est-ce que le tomo est en vie ? 
        self.delay = 100 # delay en ms
        self.chrono = 0 # Compteur (ms)

        # Sommets pour le Tomo
        self.vertices = [
            (-0.5, -0.5), 
            (0.5, -0.5), 
            (0.0, 0.5)
        ] 
        self.color = (255, 0, 0)
    """
    Gére l'action de nourir le Tomo
    """
    def eat(self, pts: int):
        if self.health >= 100: # Gére le cas ou on ne peut plus manger 
            print(f"{self.name} est repus")
            self.health = 100 # Contrainde la valeur a 100 si health = 95 et que pts vaut 10
        else:
            self.health += pts # Manger reviens a augmente
    """
    Gére l'action de décés du Tomo
    """
    def dead(self):
        self.moralID = 5
        self.alive = False 
        print(f"{self.name} est mort de {self.moralState[self.moralID]}.")
        print("GAME OVER")
    
    """
    Evolution du Tomo
    """
    def update(self, dt: int):
        self.chrono += dt

        # Attendre self.delay seconde
        if self.chrono > self.delay:
            self.chrono = 0
            if self.health > 0:
                self.health -= 1

        # Gérer les état en fonction de la santé 
        if self.health > 70:
            self.moralID = 0
        elif self.health > 50:
            self.moralID = 4
        elif self.health > 30:
            self.moralID = 1
        elif self.health > 15:
            self.moralID = 2 
        elif self.health > 0:
            self.moralID = 3
        if self.health == 0:
            self.dead()
        
        print(f"La vie de tomo {self.health} % et a pour moral {self.moralState[self.moralID]}")

    """
    Dessine le tomo 
    """
    def draw(self, surface):
        screenCoordinate = [] # Coordonnées ecran pour la surface
        
        for vertex in self.vertices:
            x = linearInterpolation(-1, 0, 1, surface.get_width(), vertex[0] * -1) # Transforme [-1, 1] entre (0 et w)
            y = linearInterpolation(-1, 0, 1, surface.get_height(), vertex[1] * -1) # Transofmr [-1, 1] entre (0 et h)
            screenCoordinate.append((x, y))
        pygame.draw.polygon(surface, self.color, screenCoordinate, 2)
        

# Test du fonctionnement de la class
if __name__ == "__main__":
    animal = Tomo("Tomo", 14)
    while animal.is_alive:
        animal.update(16) # Mise a jour du tomo
        time.sleep(16 / 1000) # A modifier plus tard