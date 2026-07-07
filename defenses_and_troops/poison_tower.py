from defenses_and_troops.goblin import Goblin
from defenses_and_troops.orc import Orc
from defenses_and_troops.runner import Runner

class PoisonTower:
    def __init__(self,id,position):
        self.id = id
        self.active = True
        self.position = position

    def run_poison_tower(self,goblins,orcs,runners,historyi,total_components,base,turn):
        nearest_to_tower = None

        if self.active == True:

            # Traversing in all troops to select best troop to attack
            # Traverse in Goblin
            if len(goblins) > 0:
                nearest_to_tower = goblins[next(iter(goblins))]
                for goblin in goblins:
                    if abs(self.position - goblins[goblin].position) <= abs(self.position - nearest_to_tower.position):
                        nearest_to_tower = goblins[goblin]
            # Traverse in Orc
            if nearest_to_tower is not None:
                for orc in orcs:
                    if abs(self.position - orcs[orc].position) < abs(self.position - nearest_to_tower.position):
                        nearest_to_tower = orcs[orc]
            else:
                if len(orcs) > 0:
                    nearest_to_tower = orcs[next(iter(orcs))]
                for orc in orcs:
                    if abs(self.position - orcs[orc].position) <= abs(self.position - nearest_to_tower.position):
                        nearest_to_tower = orcs[orc]
            # Traverse in Runner
            if nearest_to_tower is not None:
                for runner in runners:
                    if abs(self.position - runners[runner].position) < abs(self.position - nearest_to_tower.position):
                        nearest_to_tower = runners[runner]
            else:
                if len(runners) > 0:
                    nearest_to_tower = runners[next(iter(runners))]
                for runner in runners:
                    if abs(self.position - runners[runner].position) <= abs(self.position - nearest_to_tower.position):
                        nearest_to_tower = runners[runner]


            # Attacking the best selected troop from all (if present)
            if nearest_to_tower is not None:
                if abs(nearest_to_tower.position - self.position) <= 1:
                        self.active = False
                        historyi.append(f"Turn : {turn} , {self.id} attacked {nearest_to_tower.id} with poison for next two steps.")
                        print(f"{self.id} attacked {nearest_to_tower.id} with poison for next 2 steps.")
                        nearest_to_tower.poison += 2


        if self.active == True:        
            historyi.append(f"Turn : {turn} , {self.id} found no enemy in range. ")
            print(f"{self.id} found no enemy in range. ")
        else:
            self.active = True
