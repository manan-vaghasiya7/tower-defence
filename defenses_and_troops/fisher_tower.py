from defenses_and_troops.goblin import Goblin
from defenses_and_troops.orc import Orc
from defenses_and_troops.runner import Runner

class FisherTower:
    def __init__(self,id,position):
        self.id = id
        self.active = True
        self.position = position

    def run_fisher_tower(self,goblins,orcs,runners,historyi,total_components,base,turn):
        weakest_enemy_in_range = None

        if self.active == True:
            # Traversing in all troops to select best troop to attack
            # Traverse in Goblin
            if weakest_enemy_in_range == None and len(goblins) > 0:
                weakest_enemy_in_range = goblins[next(iter(goblins))]
            for goblin in goblins:
                if weakest_enemy_in_range.health > goblins[goblin].health and abs(self.position - goblins[goblin].position) <= 1:
                    weakest_enemy_in_range = goblins[goblin]
            # Traverse in Orc
            if weakest_enemy_in_range == None and len(orcs) > 0:
                weakest_enemy_in_range = orcs[next(iter(orcs))]
            for orc in orcs:
                    if weakest_enemy_in_range.health > orcs[orc].health and abs(self.position - orcs[orc].position) <= 1:
                        weakest_enemy_in_range = orcs[orc]
            # Traverse in Runner
            if weakest_enemy_in_range == None and len(runners) > 0:
                weakest_enemy_in_range = runners[next(iter(runners))]
            for runner in runners:
                    if weakest_enemy_in_range.health > runners[runner].health and abs(self.position - runners[runner].position) <= 1:
                        weakest_enemy_in_range = runners[runner]


            # Attacking the weakest troop from all (if present)
            if weakest_enemy_in_range is not None and abs(weakest_enemy_in_range.position - self.position) <= 1:
                if weakest_enemy_in_range.health > 1:
                    weakest_enemy_in_range.health -= 1
                    self.active = False
                    historyi.append(f"Turn : {turn} , {self.id} attacked {weakest_enemy_in_range.id} for 1 damage. {weakest_enemy_in_range.id} hp={weakest_enemy_in_range.health}. ")
                    print(f"{self.id} attacked {weakest_enemy_in_range.id} for 1 damage. {weakest_enemy_in_range.id} hp={weakest_enemy_in_range.health}. ")

                else:
                    historyi.append(f"Turn : {turn} , {weakest_enemy_in_range.id} is killed by {self.id}")
                    print(f"{weakest_enemy_in_range.id} is killed by {self.id}")
                    total_components[weakest_enemy_in_range.position].remove(weakest_enemy_in_range.id)
                    self.active = False
                    if isinstance(weakest_enemy_in_range,Goblin):
                        goblins.pop(weakest_enemy_in_range.id)
                    elif isinstance(weakest_enemy_in_range,Orc):
                        orcs.pop(weakest_enemy_in_range.id)
                    elif isinstance(weakest_enemy_in_range,Runner):
                        runners.pop(weakest_enemy_in_range.id)

        if self.active == True:        
            historyi.append(f"Turn : {turn} , {self.id} found no enemy in range. ")
            print(f"{self.id} found no enemy in range. ")
        else:
            self.active = True