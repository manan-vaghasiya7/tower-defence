from goblin import Goblin
from tower import Tower

class lane:
    def __init__(self):
        self.towers = {}
        self.goblins = {}
        self.base = 10
        self.goblins = {}

    def create_goblin(self,id,index):
        self.goblins[id] = Goblin(id)

    def create_tower(self,id,index):
        self.towers[id] = Tower(id,index)

    def run_turn(self):
        for goblin in self.goblins:
            for tower in self.towers:
                if tower.active == True:
                    if tower.index +1 == goblin.position:
                        print("{tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        if goblin.health > 0:
                            goblin.health -= 1
                            self.goblins[goblin].position += 1
                        else:
                            self.goblins.pop(goblin)
                    elif tower.index == goblin.position:
                        print("{tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        if goblin.health > 0:
                            goblin.health -= 1
                            self.goblins[goblin].position += 1
                        else:
                            self.goblins.pop(goblin)

                    elif tower.index -1 == goblin.position:
                        print("{tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        if goblin.health > 0:
                            goblin.health -= 1
                            self.goblins[goblin].position += 1
                        else:
                            self.goblins.pop(goblin)

                    else:
                        print(f"{tower.id} found no enemy in range.")

            if(goblin.position == 5):
                self.base -= 1
                self.goblins.pop(goblin)
            
                    

