from defenses_and_troops.goblin import Goblin
from defenses_and_troops.orc import Orc
from defenses_and_troops.tower import Tower
from defenses_and_troops.sniper_tower import SniperTower
from defenses_and_troops.slow_tower import SlowTower
from defenses_and_troops.runner import Runner
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
        self.runners = {}



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
    
    def create_runner(self,id):
        self.runners[id] = Runner(id)
        self.total_components[0].append(id)
        self.historyi.append(f"Spawned {self.runners[id].id} orc on lane1 at position 0.")
        print(f"Spawned {self.runners[id].id} orc on lane1 at position 0.")

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

        # Run SniperTowers
        for sniper_tower in self.sniper_towers:
            self.sniper_towers[sniper_tower].run_sniper_tower(self.goblins,self.orcs,self.runners,self.historyi,self.total_components,self.base,self.turn)

        # Run Towers
        for tower in self.towers:
            self.towers[tower].run_tower(self.goblins,self.orcs,self.runners,self.historyi,self.total_components,self.base,self.turn)

        # Run Goblins
        to_pop = []
        for goblin in self.goblins:
            self.base = self.goblins[goblin].run_goblin(self.historyi,self.total_components,self.base,self.turn,to_pop)
        for p in to_pop:
            self.goblins.pop(p)

        # Run Orcs
        to_pop = []
        for orc in self.orcs:
            self.base = self.orcs[orc].run_orc(self.historyi,self.total_components,self.base,self.turn,to_pop)
        for p in to_pop:
            self.orcs.pop(p)

        # Run Runners
        to_pop = []
        for runner in self.runners:
            self.base = self.runners[runner].run_runner(self.historyi,self.total_components,self.base,self.turn,to_pop)
        for p in to_pop:
            self.runners.pop(p)


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
