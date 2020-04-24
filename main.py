#coding: utf-8
import time 

class Tomo:
    def __init__(self, name, age):
        self.moralState = ["Bonheur", "Tristesse", "Colere", "Peur", "Faim", "Mort"]
        self.moralID = 0 # Au début du commence "Heureux"
        self.name = name # Nom en chaine de caractère
        self.health = 100 # Taux de point de vie en %
        self.age = 1 # Age en tant qu'entier 
        self.alive = True # Est-ce que le tomo est en vie ? 
        self.delay = 100 # delay en ms
        self.chrono = 0 # Compteur (ms)

    def isAlive(self):
        return self.alive 

    def eat(self, pts):
        if self.health >= 100: # Gére le cas ou on ne peut plus manger 
            print("{} est repus".format(self.name))
            self.health = 100 # Contrainde la valeur a 100 si health = 95 et que pts vaut 10
        else:
            self.health += pts # Manger reviens a augmenter

    def dead(self):
        print("{} est mort de {}.".format(self.name, self.moralState[self.moralID]))
        print("GAME OVER")
    
    def update(self, dt):
        self.chrono += dt

        # Attendre self.DELAY seconde
        if self.chrono > self.delay:
            self.chrono = 0
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
            self.moralID = 5
            self.dead()
            self.alive = False
        
        print("La vie de tomo {} % et a pour moral {}".format(self.health, self.moralState[self.moralID]))

animal = Tomo("Tomo", 14)

while animal.isAlive():
    animal.update(16) # Mise a jour du tomo
    time.sleep(16 / 1000) # A modifier plus tard