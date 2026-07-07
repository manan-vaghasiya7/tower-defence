from defenses_and_troops.goblin import Goblin
from defenses_and_troops.orc import Orc
from defenses_and_troops.runner import Runner
class SniperTower:
    def __init__(self,id,position,range):
        self.id = id
        self.active = True
        self.range = range
        self.position = position

    def run_sniper_tower(self,goblins,orcs,runners,historyi,total_components,base,turn):
        nearest_to_tower = None

        if self.active == True:
            # Traversing in all troops to select best troop to attack
            # Traverse in Goblin
            if nearest_to_tower == None and len(goblins) > 0:
                nearest_to_tower = goblins[next(iter(goblins))]
            for goblin in goblins:
                if abs(self.position - goblins[goblin].position) <= abs(self.position - nearest_to_tower.position):
                    nearest_to_tower = goblins[goblin]
            # Traverse in Orc
            if nearest_to_tower == None and len(orcs) > 0:
                nearest_to_tower = orcs[next(iter(orcs))]
            for orc in orcs:
                if abs(self.position - orcs[orc].position) < abs(self.position - nearest_to_tower.position):
                    nearest_to_tower = orcs[orc]
            # Traverse in Runner
            if nearest_to_tower == None and len(runners) > 0:
                nearest_to_tower = runners[next(iter(runners))]
            for runner in runners:
                if abs(self.position - runners[runner].position) < abs(self.position - nearest_to_tower.position):
                    nearest_to_tower = runners[runner]

            
            # Attacking the best selected troop from all (if present)
            if nearest_to_tower is not None and abs(nearest_to_tower.position - self.position) <= self.range:
                if nearest_to_tower.health > 1:
                    nearest_to_tower.health -= 1
                    self.active = False
                    historyi.append(f"Turn : {turn} , {self.id} attacked {nearest_to_tower.id} for 1 damage. {nearest_to_tower.id} hp={nearest_to_tower.health}. ")
                    print(f"{self.id} attacked {nearest_to_tower.id} for 1 damage. {nearest_to_tower.id} hp={nearest_to_tower.health}. ")

                else:
                    historyi.append(f"Turn : {turn} , {nearest_to_tower.id} is killed by {self.id}")
                    print(f"{nearest_to_tower.id} is killed by {self.id}")
                    total_components[nearest_to_tower.position].remove(nearest_to_tower.id)
                    self.active = False
                    if isinstance(nearest_to_tower,Goblin):
                        goblins.pop(nearest_to_tower.id)
                    elif isinstance(nearest_to_tower,Orc):
                        orcs.pop(nearest_to_tower.id)
                    elif isinstance(nearest_to_tower,Runner):
                        runners.pop(nearest_to_tower.id)

        if self.active == True:        
            historyi.append(f"Turn : {turn} , {self.id} found no enemy in range. ")
            print(f"{self.id} found no enemy in range. ")
        else:
            self.active = True
