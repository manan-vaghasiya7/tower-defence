
def run_sniper_towers(sniper_towers,goblins,historyi,total_components,base,turn):

    for sniper_tower in sniper_towers:
        to_pop = []
        for goblin in goblins:

            if sniper_towers[sniper_tower].active == True:
                if sniper_towers[sniper_tower].range >= abs(goblins[goblin].position - sniper_towers[sniper_tower].position):

                    if goblins[goblin].health > 1:
                        goblins[goblin].health -= 1
                        sniper_towers[sniper_tower].active = False
                        historyi.append(f"Turn : {turn} , {sniper_towers[sniper_tower].id} attacked {goblins[goblin].id} for 1 damage. {goblins[goblin].id} hp={goblins[goblin].health}. ")
                        print(f"{sniper_towers[sniper_tower].id} attacked {goblins[goblin].id} for 1 damage. {goblins[goblin].id} hp={goblins[goblin].health}. ")

                    else:
                        historyi.append(f"Turn : {turn} , {goblins[goblin].id} is killed by {sniper_towers[sniper_tower].id}")
                        print(f"{goblins[goblin].id} is killed by {sniper_towers[sniper_tower].id} ")
                        total_components[goblins[goblin].position].remove(goblins[goblin].id)
                        sniper_towers[sniper_tower].active = False
                        to_pop.append(goblin)

        for p in to_pop:
            goblins.pop(p)
        if sniper_towers[sniper_tower].active == True:        
            historyi.append(f"Turn : {turn} , {sniper_towers[sniper_tower].id} found no enemy in range. ")
            print(f"{sniper_towers[sniper_tower].id} found no enemy in range. ")
        else:
            sniper_towers[sniper_tower].active = True