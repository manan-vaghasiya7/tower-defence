from lane import lane
import sys

lane1 = lane()
gid = 1
tid = 1

def display_command():
    print("SPAWN <lane> <enemyType>")
    print("ADD_TOWER <lane> <position>")
    print(" RUN_TURN")
    print("")
    print("STATUS")
    print("HISTORY")
    print("EXIT")

    
while(True):
    display_command()
    command = input()
    if(command == "SPAWN lane1 goblin"):
        id = 'E' + str(gid)
        lane1.create_goblin(id)
        gid += 1
    
    elif(command.startswith("ADD_TOWER lane1")):
        parts = command.split()
        position = int(parts[2])
        if(position >= 0 and position <= 4):
            id = 'T' + str(tid)
            lane1.create_tower(id,position)
            tid += 1
        else:
            print("Enter valid input")

    elif(command.startswith("ADD_SNIPER_TOWER lane1")):
        parts = command.split()
        position = int(parts[2])
        if(position >= 0 and position <= 4):
            id = 'ST' + str(tid)
            lane1.create_sniper_tower(id,position)
            tid += 1
        else:
            print("Enter valid input")

    elif(command == "RUN_TURN"):
        lane1.run_turn()

    elif(command == "STATUS"):
        lane1.status()

    elif(command == "HISTORY"):
        lane1.history()    

    elif(command == "EXIT"):
        sys.exit()