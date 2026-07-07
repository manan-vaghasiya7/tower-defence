import sys
class Goblin:
    def __init__(self,id):
        self.id = id
        self.health = 3
        self.speed = 1
        self.position = 0
        self.slow_applied = False
        self.dont_move = False
    
    def run_goblin(self,historyi,total_components,base,turn,to_pop):
        if self.dont_move == True:
            self.dont_move = False
        else:
            if self.position == 4:
                base -= 1
                historyi.append(f"Turn : {turn} , {self.id} attacked Base for 1 damage and {self.id} is removed. Base hp ={base} ")
                print(f"{self.id} attacked Base for 1 damage and {self.id} is removed. Base hp ={base}  ")
                total_components[self.position].remove(self.id)
                to_pop.append(self.id)
                if base == 0:
                    historyi.append("YOU WON")
                    print("YOU WON")
                    sys.exit()

            else : 
                self.position += 1
                historyi.append(f"{self.id} moved from {self.position-1} to {self.position} ")
                print(f"{self.id} moved from {self.position-1} to {self.position} ")
                total_components[self.position-1].remove(self.id)
                total_components[self.position].append(self.id)

        return base
    
    def make_slow(self):
        self.slow_applied = True
        self.dont_move = True


