def run_sniper_towers(sniper_towers,goblins,historyi,total_components,base,turn):

    for sniper_tower in sniper_towers:
        nearest_to_tower = next(iter(goblins))
        if sniper_towers[sniper_tower].active == True:
            for goblin in goblins:
                if abs(sniper_towers[sniper_tower].position - goblins[goblin].position) < abs(sniper_towers[sniper_tower].position - goblins[nearest_to_tower].position):
                    nearest_to_tower = goblin
            if abs(goblins[nearest_to_tower].position - sniper_towers[sniper_tower].position) <= sniper_towers[sniper_tower].range:
                if goblins[nearest_to_tower].health > 1:
                    goblins[nearest_to_tower].health -= 1
                    sniper_towers[sniper_tower].active = False
                    historyi.append(f"Turn : {turn} , {sniper_towers[sniper_tower].id} attacked {goblins[nearest_to_tower].id} for 1 damage. {goblins[nearest_to_tower].id} hp={goblins[nearest_to_tower].health}. ")
                    print(f"{sniper_towers[sniper_tower].id} attacked {goblins[nearest_to_tower].id} for 1 damage. {goblins[nearest_to_tower].id} hp={goblins[nearest_to_tower].health}. ")

                else:
                    historyi.append(f"Turn : {turn} , {goblins[nearest_to_tower].id} is killed by {sniper_towers[sniper_tower].id}")
                    print(f"{goblins[nearest_to_tower].id} is killed by {sniper_towers[sniper_tower].id} ")
                    total_components[goblins[nearest_to_tower].position].remove(goblins[nearest_to_tower].id)
                    sniper_towers[sniper_tower].active = False
                    goblins.pop(nearest_to_tower)

        if sniper_towers[sniper_tower].active == True:        
            historyi.append(f"Turn : {turn} , {sniper_towers[sniper_tower].id} found no enemy in range. ")
            print(f"{sniper_towers[sniper_tower].id} found no enemy in range. ")
        else:
            sniper_towers[sniper_tower].active = True
        