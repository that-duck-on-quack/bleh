from game.combatsystem import Combatsystem
from game.player import Player
from game.boss import Bountyboss

tes = Player("peen")
boss = Bountyboss()


combatrun = Combatsystem(tes,boss)
combat = False
while not combat:
    combat = combatrun.turntick()
print("fin")