import sys

class Orc:
    def __init__(self,id):
        self.id = id
        self.health = 5
        self.speed = 1

    def __init__(self,historyi,total_components,base,turn,to_pop):
        if self.position == 4:
            base -= 1
            historyi.append(f"Turn : {turn} , {self.id} attacked Base for 1 damage and {self.id} is removed. Base hp ={base} ")
            print(f"{self.id} attacked Base for 1 damage and {self.id} is removed. Base hp ={base}  ")
            total_components[self.position].remove(self.id)
            to_pop.append(self)
            if base == 0:
                historyi.append("YOU WON")
                print("YOU WON")
                sys.exit()

        else: 
            self.position += 1
            historyi.append(f"{self.id} moved from {self.position-1} to {self.position} ")
            print(f"{self.id} moved from {self.position-1} to {self.position} ")
            total_components[self.position-1].remove(self.id)
            total_components[self.position].append(self.id)