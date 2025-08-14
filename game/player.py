class player:
    def __init__(self,name):
        
        self.name = name
        self.hp = 100
        self.current_hp = self.hp
        self.attack = 10
        self.parrycharge = 3 
        self.dodgecharge = True
    
    def damage(self,damage):
        self.current_hp -= damage
    
    def attacktype(self,attack):
        if attack == "basic":
            return self.basic()
        if attack == "heavy":
            return self.heavy()

    def basic(self):
        damage = self.attack
        print(f"Player does a basic attack. It does {damage}!")
        return damage
    
    def heavy(self):
        damage = self.attack * 10
        print(f"Player does a heavy attack. It does {damage}!")
        return damage

    def counter(self,counter):
        match counter:
            case "parry":
                if self.parrycharge > 0:
                    self.parrycharge -= 1 
                    print("Parried!")
                    return True
                else:
                    print("Parry failed")
                    return False
            case "dodge":
                if self.dodgecharge:
                    self.dodgecharge = False
                    print("Dodged!")
                    return True
                else: 
                    print("Dodge failed")
                    return False
                
            case _:
                print("Uncountered!")
                return False
    def turntick(self):
        self.dodgecharge = True
        self.parrycharge += 1        

        
    
    def precombat(self):
        self.current_hp = self.hp
