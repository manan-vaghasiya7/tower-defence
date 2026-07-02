from lane import lane

lane1 = lane()
gid = 1
tid = 1
while(True):
    command = input()
    if(command == "SPAWN lane1 goblin"):
        id = 'E' + str(gid)
        lane1.create_goblin(id)
        gid += 1
    
    elif(command == "ADD_TOWER lane1 0"):
        id = 'T' + str(tid)
        lane1.create_tower(0)
        tid += 1

    elif(command == "ADD_TOWER lane1 1"):
        id = 'T' + str(tid)
        lane1.create_tower(id,1)
        tid += 1

    elif(command == "ADD_TOWER lane1 2"):
        id = 'T' + str(tid)
        lane1.create_tower(id,2)
        tid += 1

    elif(command == "ADD_TOWER lane1 3"):
        id = 'T' + str(tid)
        lane1.create_tower(id,3)
        tid += 1

    elif(command == "ADD_TOWER lane1 4"):
        id = 'T' + str(tid)
        lane1.create_tower(id,4)
        tid += 1

    elif(command == "RUN_TURN"):
        lane1.run_turn()

    elif(command == "STATUS"):
        lane1.status()

    elif(command == "HISTORY"):
        lane1.history()    