from lane import lane
import sys

lane1 = lane()
gid = 1
tid = 1
while(True):
    command = input()
    if(command == "SPAWN lane1 goblin"):
        id = 'E' + str(gid)
        lane1.create_goblin(id)
        gid += 1
    
    elif(command.startswith("ADD_TOWER lane1")):
        parts = command.split()
        if(parts[2] > 4 or parts[2] < 0):
            print("YOU HAVE ENTERED THE WRONG POSITION TO CREATE TOWER")
        else:
            id = 'T'+str(tid)
            lane.create_tower(id,parts[2])
            tid += 1

    elif(command == "RUN_TURN"):
        lane1.run_turn()

    elif(command == "STATUS"):
        lane1.status()

    elif(command == "HISTORY"):
        lane1.history()    

    elif(command == "EXIT"):
        sys.exit()