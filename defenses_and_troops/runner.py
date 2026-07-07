import sys

class Runner:
    def __init__(self,id):
        self.id = id
        self.health = 2
        self.speed = 2
        self.position = 0
        self.slow_applied = False
        self.dont_move = False
        self.poison = 0

    def poison_attack(self,historyi,total_components,turn,to_pop):
        if self.health > 1:
            self.health -= 1
            historyi.append(f"Turn : {turn} ,{self.id} is attacked by poison for 1 damage. {self.id} hp={self.health}. ")
            print(f"{self.id} is attacked by poison for 1 damage. {self.id} hp={self.health}. ")

        else:
            historyi.append(f"Turn : {turn} , {self.id} is killed by poison")
            print(f"{self.id} is killed by poison")
            total_components[self.position].remove(self.id)
            to_pop.append(self.id)
        self.poison -= 1

    def run_runner(self,historyi,total_components,base,turn,to_pop):
        if self.dont_move:
            self.dont_move = False
            if self.position >= 4:
                base -= 1
                historyi.append(f"Turn : {turn} , {self.id} attacked Base for 1 damage and {self.id} is removed. Base hp ={base} ")
                print(f"{self.id} attacked Base for 1 damage and {self.id} is removed. Base hp ={base}  ")
                total_components[self.position].remove(self.id)
                to_pop.append(self.id)
                if base == 0:
                    historyi.append("YOU WON")
                    print("YOU WON")
                    sys.exit()
                return base

            else: 
                self.position += 1
                historyi.append(f"{self.id} moved from {self.position-1} to {self.position} ")
                print(f"{self.id} moved from {self.position-1} to {self.position} ")
                total_components[self.position-1].remove(self.id)
                total_components[self.position].append(self.id)
        else:
            if self.position >= 3:
                base -= 1
                historyi.append(f"Turn : {turn} , {self.id} attacked Base for 1 damage and {self.id} is removed. Base hp ={base} ")
                print(f"{self.id} attacked Base for 1 damage and {self.id} is removed. Base hp ={base}  ")
                total_components[self.position].remove(self.id)
                to_pop.append(self.id)
                if base == 0:
                    historyi.append("YOU WON")
                    print("YOU WON")
                    sys.exit()

            else: 
                self.position += 2
                historyi.append(f"{self.id} moved from {self.position-2} to {self.position} ")
                print(f"{self.id} moved from {self.position-2} to {self.position} ")
                total_components[self.position-2].remove(self.id)
                total_components[self.position].append(self.id)

        if self.poison > 0:
            self.poison_attack(historyi,total_components,turn,to_pop)
        return base
    
    def make_slow(self):
        self.slow_applied = True
        self.dont_move = True