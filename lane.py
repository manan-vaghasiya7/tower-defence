from defenses_and_troops.goblin import Goblin
from defenses_and_troops.orc import Orc
from defenses_and_troops.tower import Tower
from defenses_and_troops.sniper_tower import SniperTower
from defenses_and_troops.slow_tower import SlowTower
from run_components.run_towers import run_towers
from run_components.run_goblins import run_goblins
from run_components.run_sniper_tower import run_sniper_towers
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
        self.slow_towers = {}
        self.orcs = {}



    def create_goblin(self,id):
        self.goblins[id] = Goblin(id)
        self.total_components[0].append(id)
        self.historyi.append(f"Spawned {self.goblins[id].id} goblin on lane1 at position 0.")
        print(f"Spawned {self.goblins[id].id} goblin on lane1 at position 0.")

    def create_orc(self,id):
        self.orcs[id] = Orc(id)
        self.total_components[0].append(id)
        self.historyi.append(f"Spawned {self.orcs[id].id} orc on lane1 at position 0.")
        print(f"Spawned {self.orcs[id].id} orc on lane1 at position 0.")

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

    def create_slow_tower(self,id,position):
        self.slow_towers[id] = SlowTower(id,position)
        self.total_components[position].append(id)
        self.historyi.append(f"Added {self.slow_towers[id].id} slow tower on lane1 at position {self.slow_towers[id].position}.")
        print(f"Added {self.slow_towers[id].id} slow tower on lane1 {self.slow_towers[id].position}.")



    def run_turn(self):
        self.turn += 1
        print(f"Turn {self.turn} started.")

        run_sniper_towers(self.sniper_towers,self.goblins,self.historyi,self.total_components,self.base,self.turn)

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
        
                    
