class SniperTower:
    def __init__(self,id,position,range):
        self.id = id
        self.active = True
        self.range = range
        self.position = position

    def run_sniper_tower(self,goblins,historyi,total_components,base,turn):
        nearest_to_tower = next(iter(goblins))
        if self.active == True:
            for goblin in goblins:
                if abs(self.position - goblins[goblin].position) < abs(self.position - goblins[nearest_to_tower].position):
                    nearest_to_tower = goblin
            if abs(goblins[nearest_to_tower].position - self.position) <= self.range:
                if goblins[nearest_to_tower].health > 1:
                    goblins[nearest_to_tower].health -= 1
                    self.active = False
                    historyi.append(f"Turn : {turn} , {self.id} attacked {goblins[nearest_to_tower].id} for 1 damage. {goblins[nearest_to_tower].id} hp={goblins[nearest_to_tower].health}. ")
                    print(f"{self.id} attacked {goblins[nearest_to_tower].id} for 1 damage. {goblins[nearest_to_tower].id} hp={goblins[nearest_to_tower].health}. ")

                else:
                    historyi.append(f"Turn : {turn} , {goblins[nearest_to_tower].id} is killed by {self.id}")
                    print(f"{goblins[nearest_to_tower].id} is killed by {self.id} ")
                    total_components[goblins[nearest_to_tower].position].remove(goblins[nearest_to_tower].id)
                    self.active = False
                    goblins.pop(nearest_to_tower)

        if self.active == True:        
            historyi.append(f"Turn : {turn} , {self.id} found no enemy in range. ")
            print(f"{self.id} found no enemy in range. ")
        else:
            self.active = True