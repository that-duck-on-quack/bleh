class player:
    def __init__(self,name):
        
        self.name = name
        self.hp = 100
        self.current_hp = self.hp
        self.attack = 10
    
    def takedamage(self,damage):
        self.current_hp -= damage
    
    def basic(self):
        damage = self.attack
        return damage