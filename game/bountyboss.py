from game.utils import loaddata
import random


class Bountyboss:
    def __init__(self,boss):
        bossinfo = loaddata("bossinfo.json")

        if boss not in bossinfo:
            raise Exception("invaild boss name")
        
        currentboss = bossinfo[boss]
        print(currentboss)

        
        self.hp = currentboss["mainstats"]["hp"]
        self.defence = currentboss["mainstats"]["defence"]
        self.weights = currentboss["weights"]
    
    def damage(self,damage,pen):

        realdefence = 0
        if self.defence < pen:
            realdefence = 0
        else:
            realdefence = self.defence-pen

        self.hp -= damage*(1-((realdefence)/100))
        pass

    def bossattack(self):
        names = list(self.weights.keys())
        weightsvalues = list(self.weights.values())
        attack = random.choices(names,weights=weightsvalues,k=1)[0]
        
        