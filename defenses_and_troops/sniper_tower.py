from defenses_and_troops.goblin import Goblin
from defenses_and_troops.orc import Orc
class SniperTower:
    def __init__(self,id,position,range):
        self.id = id
        self.active = True
        self.range = range
        self.position = position

    def run_sniper_tower(self,goblins,orcs,historyi,total_components,base,turn):
        if self.active == True:

            if len(goblins) > 0:
                nearest_to_tower = next(iter(goblins))
                for goblin in goblins:
                    if abs(self.position - goblins[goblin].position) <= abs(self.position - nearest_to_tower.position):
                        nearest_to_tower = goblins[goblin]

            if "nearest_to_tower" in locals():
                for orc in orcs:
                    if abs(self.position - orcs[orc].position) < abs(self.position - nearest_to_tower.position):
                        nearest_to_tower = orcs[orc]
            else:
                if len(orcs) > 0:
                    nearest_to_tower = next(iter(orcs))
                for orc in orcs:
                    if abs(self.position - orcs[orc].position) <= abs(self.position - nearest_to_tower.position):
                        nearest_to_tower = orcs[orc]

            if "nearest_to_tower" in locals():
                if abs(nearest_to_tower.position - self.position) <= self.range:
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

        if self.active == True:        
            historyi.append(f"Turn : {turn} , {self.id} found no enemy in range. ")
            print(f"{self.id} found no enemy in range. ")
        else:
            self.active = True




                    
        #     if abs(goblins[nearest_to_tower].position - self.position) <= self.range:
        #         if goblins[nearest_to_tower].health > 1:
        #             goblins[nearest_to_tower].health -= 1
        #             self.active = False
        #             historyi.append(f"Turn : {turn} , {self.id} attacked {goblins[nearest_to_tower].id} for 1 damage. {goblins[nearest_to_tower].id} hp={goblins[nearest_to_tower].health}. ")
        #             print(f"{self.id} attacked {goblins[nearest_to_tower].id} for 1 damage. {goblins[nearest_to_tower].id} hp={goblins[nearest_to_tower].health}. ")

        #         else:
        #             historyi.append(f"Turn : {turn} , {goblins[nearest_to_tower].id} is killed by {self.id}")
        #             print(f"{goblins[nearest_to_tower].id} is killed by {self.id} ")
        #             total_components[goblins[nearest_to_tower].position].remove(goblins[nearest_to_tower].id)
        #             self.active = False
        #             goblins.pop(nearest_to_tower)

        # if self.active == True:        
        #     historyi.append(f"Turn : {turn} , {self.id} found no enemy in range. ")
        #     print(f"{self.id} found no enemy in range. ")
        # else:
        #     self.active = True