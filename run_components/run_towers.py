def run_towers(towers,goblins,historyi,total_components,base,turn):

    for tower in towers:
        to_pop = []
        for goblin in goblins:

            if towers[tower].active == True:
                if towers[tower].position == goblins[goblin].position or towers[tower].position +1 == goblins[goblin].position or towers[tower].position -1 == goblins[goblin].position:

                    if goblins[goblin].health > 1:
                        goblins[goblin].health -= 1
                        towers[tower].active = False
                        historyi.append(f"Turn : {turn} , {towers[tower].id} attacked {goblins[goblin].id} for 1 damage. {goblins[goblin].id} hp={goblins[goblin].health}. ")
                        print(f"{towers[tower].id} attacked {goblins[goblin].id} for 1 damage. {goblins[goblin].id} hp={goblins[goblin].health}. ")

                    else:
                        historyi.append(f"Turn : {turn} , {goblins[goblin].id} is killed ")
                        print(f"{goblins[goblin].id} is killed ")
                        total_components[goblins[goblin].position].remove(goblins[goblin].id)
                        towers[tower].active = False
                        to_pop.append(goblin)

        for p in to_pop:
            goblins.pop(p)
        if towers[tower].active == True:        
            historyi.append(f"Turn : {turn} , {towers[tower].id} found no enemy in range. ")
            print(f"{towers[tower].id} found no enemy in range. ")
        else:
            towers[tower].active = True