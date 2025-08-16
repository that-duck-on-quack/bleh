from game.player import Player
from game.boss import Bountyboss

class Combatsystem:
    def __init__(self,player,boss):
        
        self.player = player
        self.boss = boss
        self.turn = "player"
        self.bossdelay = 0
        self.turncount = 1 
        
    def playerturn(self, attack):
        dmg = self.player.attacktype(attack)
        self.boss.damage(dmg)
        if self.boss.current_hp <= 0:
            print("boss dead")
            return True
        if self.bossdelay > 1:
            self.turn = 'player'
            self.bossdelay -= 1 
        else:
            self.turn = 'boss'
    def postturn(self):
        self.bossdelay = self.boss.bosscharge()
        self.player.turntick()
        return False
    
    def bossturn(self):

        move = self.boss.bossmove()
        print(f"boss attack with a {move} move")
        counterfail,type = self.player.counter(input("counter type"))
        match move:
            case "basic" | "heavy":
                if not counterfail:
                    self.player.damage(self.boss.matchboss(move))
                    print(f"{type} failed")
                else: 
                    print("Countered!")
            case "dash":
                if counterfail:
                    if type == "parry":
                        print("Parried!")
                    else:
                        print("Dodge failed")
                        self.player.damage(self.boss.matchboss(move))
                else:
                    print("counter failed")
                    self.player.damage(self.boss.matchboss(move))
        self.turn = 'next'
        if self.player.current_hp <= 0:
            print("gg boss win")
            return True
        return False

    def turntick(self):
        if self.turn == "player":
            return self.playerturn(input("player turn: "))
        if self.turn == "boss":
            return self.bossturn()
        if self.turn == "next":
            self.postturn()
            self.turn = 'player'
            self.turncount += 1 
            print(self.turncount,"turn count")