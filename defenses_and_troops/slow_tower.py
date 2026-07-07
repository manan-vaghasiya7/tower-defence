from defenses_and_troops.goblin import Goblin
from defenses_and_troops.orc import Orc
from defenses_and_troops.runner import Runner

class SlowTower:
    def __init__(self,id,position):
        self.active = True
        self.id = id
        self.position = position

    def run_slow_tower(self,goblins,orcs,runners,historyi,total_components,base,turn):
        nearest_to_tower = None

        if self.active == True:

            # Traversing in all troops to select best troop to attack
            # Traverse in Goblin
            if nearest_to_tower == None and len(goblins) > 0:
                nearest_to_tower = goblins[next(iter(goblins))]
            for goblin in goblins:
                if abs(self.position - goblins[goblin].position) <= abs(self.position - nearest_to_tower.position) and goblins[goblin].slow_applied == False:
                    nearest_to_tower = goblins[goblin]
            # Traverse in Orc
            if nearest_to_tower == None and len(orcs) > 0:
                nearest_to_tower = orcs[next(iter(orcs))]
            for orc in orcs:
                if abs(self.position - orcs[orc].position) < abs(self.position - nearest_to_tower.position) and orcs[orc].slow_applied == False:
                    nearest_to_tower = orcs[orc]
            # Traverse in Runner
            if nearest_to_tower == None and len(runners) > 0:
                nearest_to_tower = runners[next(iter(runners))]
            for runner in runners:
                if abs(self.position - runners[runner].position) < abs(self.position - nearest_to_tower.position) and runners[runner].slow_applied == False:
                    nearest_to_tower = runners[runner]

            
            # Attacking the best selected troop from all (if present)
            if nearest_to_tower is not None and abs(nearest_to_tower.position - self.position) <= 1 and nearest_to_tower.slow_applied == False:
                self.active = False
                nearest_to_tower.make_slow()
                historyi.append(f"Turn : {turn} , {self.id} slowed  {nearest_to_tower.id} for 1 step ")
                print(f"{self.id} slowed {nearest_to_tower.id} for 1 step ")

        if self.active == True:        
            historyi.append(f"Turn : {turn} , {self.id} found no enemy to use slow tower. ")
            print(f"{self.id} found no enemy to use slow tower. ")
        else:
            self.active = True
