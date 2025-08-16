import random as rand

class Bountyboss:
    def __init__(self):

        self.mindelay = 1
        self.maxdelay = 3
        self.hp = 1000
        self.attack = 10
        self.current_hp = self.hp
        self.moveset = ['basic','heavy','dash']
        
    def basic(self):
        damage = self.attack
        print(f"Boss hits basic attack. It does {damage}!")
        return damage
    
    def heavy(self):
        damage = self.attack * 10
        print(f"Boss hits heavy attack. It does {damage}!")
        return damage
    
    def dash(self):
        damage = self.attack * 5
        print(f"Boss hits Dash attack. It does {damage}!")
        return damage
    
    def damage(self,damage):
        self.current_hp -= damage

    def precombat(self):
        self.current_hp = self.hp

    def bosscharge(self):
        wait = rand.randint(self.mindelay,self.maxdelay)
        return wait
    
    def bossmove(self):
        move = rand.choice(self.moveset)
        return move
    
    def matchboss(self,move):
        match move:
            case 'basic':
                return self.basic()
            case 'heavy':
                return self.heavy()
            case 'dash':
                return self.dash()

        