from goblin import Goblin
from tower import Tower
from sniper_tower import SniperTower
from run_components.run_towers import run_towers
from run_components.run_goblins import run_goblins
import sys

class lane:
    def __init__(self):
        self.goblins = {}
        self.towers = {}
        self.sniper_towers = {}
        self.historyi = []
        self.total_components = [[],[],[],[],[],[]]
        self.base = 10
        self.turn = 0


    def create_goblin(self,id):
        self.goblins[id] = Goblin(id)
        self.total_components[0].append(id)
        self.historyi.append(f"Spawned {self.goblins[id].id} goblin on lane1 at position 0.")
        print(f"Spawned {self.goblins[id].id} goblin on lane1 at position 0.")



    def create_tower(self,id,position):
        self.towers[id] = Tower(id,position)
        self.total_components[position].append(id)
        self.historyi.append(f"Added {self.towers[id].id} tower on lane1 at position {self.towers[id].position}.")
        print(f"Added {self.towers[id].id} tower on lane1 at position {self.towers[id].position}.")



    def create_sniper_tower(self,id,position,range):
        self.sniper_towers[id] = SniperTower(id,position,range)
        self.total_components[position].append(id)
        self.historyi.append(f"Added {self.sniper_towers[id].id} sniper tower on lane1 of range {self.sniper_towers[id].range} at position {self.sniper_towers[id].position}.")
        print(f"Added {self.sniper_towers[id].id} sniper tower on lane1 of range {self.sniper_towers[id].range} at position {self.sniper_towers[id].position}.")



    def run_turn(self):
        self.turn += 1
        print(f"Turn {self.turn} started.")


        for sniper_tower in self.sniper_towers:
            to_pop = []
            for goblin in self.goblins:

                if self.sniper_towers[sniper_tower].active == True:
                    if self.sniper_towers[sniper_tower].range >= abs(self.goblins[goblin].position - self.sniper_towers[sniper_tower].position):

                        if self.goblins[goblin].health > 1:
                            self.goblins[goblin].health -= 1
                            self.sniper_towers[sniper_tower].active = False
                            self.historyi.append(f"Turn : {self.turn} , {self.sniper_towers[sniper_tower].id} attacked {self.goblins[goblin].id} for 1 damage. {self.goblins[goblin].id} hp={self.goblins[goblin].health}. ")
                            print(f"{self.sniper_towers[sniper_tower].id} attacked {self.goblins[goblin].id} for 1 damage. {self.goblins[goblin].id} hp={self.goblins[goblin].health}. ")

                        else:
                            self.historyi.append(f"Turn : {self.turn} , {self.goblins[goblin].id} is killed by {self.sniper_towers[sniper_tower].id}")
                            print(f"{self.goblins[goblin].id} is killed by {self.sniper_towers[sniper_tower].id} ")
                            self.total_components[self.goblins[goblin].position].remove(self.goblins[goblin].id)
                            self.sniper_towers[sniper_tower].active = False
                            to_pop.append(goblin)

            for p in to_pop:
                self.goblins.pop(p)
            if self.sniper_towers[sniper_tower].active == True:        
                self.historyi.append(f"Turn : {self.turn} , {self.sniper_towers[sniper_tower].id} found no enemy in range. ")
                print(f"{self.sniper_towers[sniper_tower].id} found no enemy in range. ")
            else:
                self.sniper_towers[sniper_tower].active = True


        run_towers(self.towers,self.goblins,self.historyi,self.total_components,self.base,self.turn)




        run_goblins(self.goblins,self.historyi,self.total_components,self.base,self.turn)
        



    def status(self):
        if(self.base == 0):
            print (f"Status : Completed ")
        else:
            print(f"Status : Running ")
            print(f"Turn : {self.turn} ")
            print(f"Base Health : {self.base} \n")
            all_lengths = []
            for i in range(0, 5):
                position_length = int()
                if len(self.total_components[i]) == 0:
                    position_length = 2 
                else:
                    position_length = 1
                    for j in self.total_components[i]:
                        position_length += (len(j)+1)
                
                all_lengths.append(position_length)

            for i in range(0, 5):
                print(f"{f"{i}":<{all_lengths[i]}}", end="")
            print("BASE")

            for i in range(0, 5):
                all_id = str()
                if len(self.total_components[i]) == 0:
                    all_id = ". "
                    print(f"{all_id:<{all_lengths[i]}}", end="")
                else:
                    for j in self.total_components[i]:
                        all_id += str(j)+","
                    print(f"{all_id:<{all_lengths[i]}}", end="")
            print("🏰")

                
    def history(self):
        for i in self.historyi:
            print(i)
        
                    
