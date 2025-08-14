from game.combatsystem import Combatsystem
from game.player import player
from game.boss import bountyboss

tes = player("peen")
boss = bountyboss()


combatrun = Combatsystem(tes,boss)
combat = False
while not combat:
    combat = combatrun.turntick()
print("fin")