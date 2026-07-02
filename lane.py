from goblin import Goblin
from tower import Tower

class lane:
    def __init__(self):
        self.towers = {}
        self.goblins = {}
        self.base = 10
        self.goblins = {}
        self.turn = 0
        self.historyi = []
        self.total_components = [[],[],[],[],[],[]]

    def create_goblin(self,id):
        self.goblins[id] = Goblin(id)
        self.total_components[0].append(id)
        print("Spawned {id} goblin on lane1 at position 0.")

    def create_tower(self,id,position):
        self.historyi.append("")
        self.towers[id] = Tower(id,position)
        self.total_components[position].append(id)
        print(f"Added {id} tower on lane1 at position {position}.")

    def run_turn(self):
        self.turn += 1
        print("Turn {self.turn} started.")
        for goblin in self.goblins:
            for tower in self.towers:
                if tower.active == True:
                    if tower.position == goblin.position:
                        self.historyi.append("Turn : {self.turn} , {tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        print(f"{tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        if goblin.health > 0:
                            goblin.health -= 1
                            self.total_components[self.goblins.position].pop(goblin.id)
                            self.total_components[self.goblins.postion + 1].append(goblin.id)
                            self.goblins[goblin].position += 1
                        else:
                            self.goblins.pop(goblin)
                            self.total_components[self.goblins.position].pop(goblin.id)

                    elif tower.position +1 == goblin.position:
                        self.historyi.append( "Turn : {self.turn} , {tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        print(f"{tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        if goblin.health > 0:
                            goblin.health -= 1
                            self.total_components[self.goblins.position].pop(goblin.id)
                            self.total_components[self.goblins.postion + 1].append(goblin.id)
                            self.goblins[goblin].position += 1
                        else:
                            self.goblins.pop(goblin)
                            self.total_components[self.goblins.position].pop(goblin.id)

                    elif tower.position -1 == goblin.position:
                        self.historyi.append("Turn : {self.turn} , {tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        print(f"{tower.id} attacked {goblin.id} for 1 damage. {goblin.id} hp={goblin.heath}. \n")
                        if goblin.health > 0:
                            goblin.health -= 1
                            self.total_components[self.goblins.position].pop(goblin.id)
                            self.total_components[self.goblins.postion + 1].append(goblin.id)
                            self.goblins[goblin].position += 1

                        else:
                            self.goblins.pop(goblin)
                            self.total_components[self.goblins.position].pop(goblin.id)

                    else:
                        self.historyi.append(f"Turn : {self.turn} , {tower.id} found no enemy in range. \n")
                        print(f"{tower.id} found no enemy in range. \n")

            if(goblin.position == 5):
                self.historyi.append("Turn : {self.turn} , {self.goblins.id} attacked Base for 1 damage. Base hp ={self.base} \n")
                print(f"{self.goblins.id} attacked Base for 1 damage. Base hp ={self.base} \n")
                self.base -= 1
                self.total_components[self.goblins.position].pop(goblin.id)
                self.goblins.pop(goblin)


    def status(self):
        if(self.base == 0):
            print (f"Status : Completed \n")
        else:
            print(f"Status : Running \n")
        print("Turn : {self.turn} \n")
        print("Base Health : {self.base} \n")
        for i in range(0,5):
            print(i)
            for j in range(0,len(self.total_components[i])):
                print(" ")
        print("Base")
        print("\n")
        print(" ")
        for i in range(0,5):
            if(len(self.total_components[i])):
                print(".  ")

            else:
                for j in self.total_components[i]:
                    print (j ,",")
                print(" ")
                
    def historyi(self):
        for i in self.total_components:
            print(i)
        
                    

