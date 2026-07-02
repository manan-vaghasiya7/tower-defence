from goblin import Goblin
from tower import Tower

class lane:
    def __init__(self):
        self.towers = {}
        self.goblins = {}
        self.base = 10
        self.goblins = {}
        self.turn = 0
        self.history = []
        self.total_components = [0,0,0,0,0]

    def create_goblin(self,id,position):
        self.goblins[id] = Goblin(id)
        self.total_components[0] += 1

    def create_tower(self,id,position):
        self.history.append("")
        self.towers[id] = Tower(id,position)
        self.total_components[position]+= 1

    def run_turn(self):
        self.turn += 1
        print("Turn {self.turn} started.")
        for goblin in self.goblins:
            for tower in self.towers:
                if tower.active == True:
                    if tower.position == goblin.position:
                        self.history.append("Turn : {self.turn} , {tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        print(f"{tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        if goblin.health > 0:
                            goblin.health -= 1
                            self.total_components[self.goblins.position] -= 1
                            self.total_components[self.goblins.postion + 1] += 1
                            self.goblins[goblin].position += 1
                        else:
                            self.goblins.pop(goblin)
                            self.total_components[self.goblins.position] -= 1

                    elif tower.position +1 == goblin.position:
                        self.history.append( "Turn : {self.turn} , {tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        print(f"{tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        if goblin.health > 0:
                            goblin.health -= 1
                            self.total_components[self.goblins.position] -= 1
                            self.total_components[self.goblins.postion + 1] += 1
                            self.goblins[goblin].position += 1
                        else:
                            self.goblins.pop(goblin)
                            self.total_components[self.goblins.position] -= 1

                    elif tower.position -1 == goblin.position:
                        self.history.append("Turn : {self.turn} , {tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        print(f"{tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        if goblin.health > 0:
                            goblin.health -= 1
                            self.total_components[self.goblins.position] -= 1
                            self.total_components[self.goblins.postion + 1] += 1
                            self.goblins[goblin].position += 1

                        else:
                            self.goblins.pop(goblin)
                            self.total_components[self.goblins.position] -= 1

                    else:
                        self.history.append(f"Turn : {self.turn} , {tower.id} found no enemy in range. \n")
                        print(f"{tower.id} found no enemy in range. \n")

            if(goblin.position == 5):
                self.history.append("Turn : {self.turn} , {self.goblins.id} attacked Base for 1 damage. Base hp ={self.base} \n")
                print(f"{self.goblins.id} attacked Base for 1 damage. Base hp ={self.base} \n")
                self.base -= 1
                self.total_components[self.goblins.position] -= 1
                self.goblins.pop(goblin)


    def status(self):
        if(self.base == 0):
            print (f"Status : Completed \n")
        else:
            print(f"Status : Running \n")
        print("Turn : {self.turn} \n")
        print("Base Health : {self.base} \n")
        max = max(self.total_components)
        pr
        
        
                    

