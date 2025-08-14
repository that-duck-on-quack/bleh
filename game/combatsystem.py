from game.player import player
from game.boss import bountyboss

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
        if not self.player.counter(input("counter type")):
            self.player.damage(self.boss.bossmove())
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