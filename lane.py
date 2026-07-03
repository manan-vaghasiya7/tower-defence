from goblin import Goblin
from tower import Tower

class lane:
    def __init__(self):
        self.towers = {}
        self.goblins = {}
        self.base = 10
        self.turn = 0
        self.historyi = []
        self.total_components = [[],[],[],[],[],[]]

    def create_goblin(self,id):
        self.goblins[id] = Goblin(id)
        self.total_components[0].append(id)
        print(f"Spawned {id} goblin on lane1 at position 0.")

    def create_tower(self,id,position):
        self.historyi.append("Added {id} tower on lane1 at position {position}.")
        self.towers[id] = Tower(id,position)
        self.total_components[position].append(id)
        print(f"Added {id} tower on lane1 at position {position}.")

    def run_turn(self):
        self.turn += 1
        print(f"Turn {self.turn} started.")
        for goblin in self.goblins:
            for tower in self.towers:
                if self.towers[tower].active == True:

            
                    if self.towers[tower].position == self.goblins[goblin].position:
                        self.historyi.append("Turn : {self.turn} , {self.towers[tower].id} attacked {self.goblins[goblin].id} for 1 damage. {self.goblins[goblin].id} hp={self.goblins[goblin].heath}. \n")
                        print(f"{self.towers[tower].id} attacked {self.goblins[goblin].id} for 1 damage. {self.goblins[goblin].id} hp={self.goblins[goblin].heath}. \n")

                        if self.goblins[goblin].health > 1:
                            self.goblins[goblin].health -= 1
                            self.total_components[self.goblins[goblin].position].pop(self.goblins[goblin].id)
                            self.total_components[self.goblins.postion + 1].append(self.goblins[goblin].id)
                            self.goblins[goblin].position += 1
                            print(f"{self.goblins[goblin].id} moved from {self.goblins[goblin].position-1} to {self.goblins[goblin].position} \n")

                        else:
                            print(f"{self.goblins[goblin]} is killer \n")
                            self.goblins.pop(goblin)
                            self.total_components[self.goblins[goblin].position].pop(self.goblins[goblin].id)
                        self.towers[tower].active = False


                    elif self.towers[tower].position +1 == self.goblins[goblin].position:
                        self.historyi.append( "Turn : {self.turn} , {self.towers[tower].id} attacked {self.goblins[goblin].id} for 1 damage. {self.goblins[goblin].id} hp={self.goblins[goblin].heath}. \n")
                        print(f"{self.towers[tower].id} attacked {self.goblins[goblin].id} for 1 damage. {self.goblins[goblin].id} hp={self.goblins[goblin].heath}. \n")

                        if self.goblins[goblin].health > 1:
                            self.goblins[goblin].health -= 1
                            self.total_components[self.goblins[goblin].position].pop(self.goblins[goblin].id)
                            self.total_components[self.goblins.postion + 1].append(self.goblins[goblin].id)
                            self.goblins[goblin].position += 1
                            print(f"{self.goblins[goblin].id} moved from {self.goblins[goblin].position-1} to {self.goblins[goblin].position} \n")

                        else:
                            print(f"{self.goblins[goblin]} is killer \n")
                            self.goblins.pop(goblin)
                            self.total_components[self.goblins[goblin].position].pop(self.goblins[goblin].id)
                        self.towers[tower].active = False


                    elif self.towers[tower].position -1 == self.goblins[goblin].position:
                        self.historyi.append("Turn : {self.turn} , {self.towers[tower].id} attacked {self.goblins[goblin].id} for 1 damage. {self.goblins[goblin].id} hp={self.goblins[goblin].heath}. \n")
                        print(f"{self.towers[tower].id} attacked {self.goblins[goblin].id} for 1 damage. {self.goblins[goblin].id} hp={self.goblins[goblin].heath}. \n")

                        if self.goblins[goblin].health > 1:
                            self.goblins[goblin].health -= 1
                            self.total_components[self.goblins[goblin].position].pop(self.goblins[goblin].id)
                            self.total_components[self.goblins.postion + 1].append(self.goblins[goblin].id)
                            self.goblins[goblin].position += 1
                            print(f"{self.goblins[goblin].id} moved from {self.goblins[goblin].position-1} to {self.goblins[goblin].position} \n")

                        else:
                            print(f"{self.goblins[goblin]} is killer \n")
                            self.goblins.pop(goblin)
                            self.total_components[self.goblins[goblin].position].pop(self.goblins[goblin].id)
                        self.towers[tower].active = False


                    else:
                        self.historyi.append(f"Turn : {self.turn} , {self.towers[tower].id} found no enemy in range. \n")
                        print(f"{self.towers[tower].id} found no enemy in range. \n")


            if(self.goblins[goblin].position == 5):
                self.historyi.append("Turn : {self.turn} , {self.goblins.id} attacked Base for 1 damage. Base hp ={self.base} \n")
                print(f"{self.goblins.id} attacked Base for 1 damage. Base hp ={self.base} \n")
                self.base -= 1
                self.total_components[self.goblins[goblin].position].pop(self.goblins[goblin].id)
                self.goblins.pop(goblin)

        for tower in self.towers:
            self.towers[tower] = True

    def status(self):
        if(self.base == 0):
            print (f"Status : Completed \n")
        else:
            print(f"Status : Running \n")
        print("Turn : {self.turn} \n")
        print("Base Health : {self.base} \n")
        for i in range(0,5):
            print(i)
            for j in range(0,len(self.total_components[i])):
                print(" ")
        print("Base")
        print("\n")
        print(" ")
        for i in range(0,5):
            if(len(self.total_components[i])):
                print(".  ")

            else:
                for j in self.total_components[i]:
                    print (j ,",")
                print(" ")
                
    def historyi(self):
        for i in self.total_components:
            print(i)
        
                    

