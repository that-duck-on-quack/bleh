
import random as rand
from game.utils import loaddata

#player class
class Player:
    def __init__(self,name,pclass):
        class_data = loaddata("classes.json")

        if pclass not in class_data:
            raise Exception("invaild class")

        self.name = name
        self.pclass = pclass
        self.moves = loaddata("playerattack.json")
        self.hp = class_data[pclass]["hp"]
        self.attack = class_data[pclass]['attack']
        self.defence = class_data[pclass]['defence']
        self.cr =  class_data[pclass]["cr"]
        self.cd = class_data[pclass]['cd']
        self.current_hp = self.hp
        self.inventory = []
        self.charges = 3
        self.combo = 0
        self.energy = 0
        self.cooldown = {}

    def vaildmove(self,name):

        move = self.moves[name]

        if move.get("bosscounter",False):
            return False
        if move.get("needcombo",False):
            print("needs combo")
            if self.combo < move.get("comboneeded",0):
                return False
        if move.get("needenergy", False):
            if self.energy < move.get("energyneeded", 0):
                return False
        return True
    
    def bosscounter(self,damage,name):

        if name not in self.moves:
            self.current_hp -= damage
            return False,damage
        
        move = self.moves[name]
        if not move.get("bosscounter"):
            print("not dodge counter")
            self.current_hp -= damage
            return False,damage
        if move.get("needcharges"):
            if self.charges >= 1:
                self.charges -= 1 
                return True
        if move.get("cooldown"):
            self.cooldown.update({name:self.moves[name]["cooldown"]})
            print(self.cooldown)
            return True
        
    def playerdeath(self):
        if self.current_hp <= 0:
            return True
        return False
    
    def playerattack(self,name):
        move = self.moves[name]
        damage = self.attack * move.get("damagemult") 
        random = rand.randint(1,100)
        temp = self.cr
        square = 1 
        while temp >= 100:
            temp -= 100
            square += 1 
        if (100-temp) < random:
            square += 1
        damage = damage * ((1+(self.cd/100))**square)
        return damage

    def damage(self,damage):
       
        temp = damage / (1+ self.defence/150)
        self.current_hp -= damage
    
    def precombatreset(self):
        self.current_hp = self.hp
        self.combo = 0
        self.energy = 0 
    


