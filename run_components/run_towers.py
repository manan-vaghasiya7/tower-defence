from defenses_and_troops.goblin import Goblin

def run_towers(towers,goblins,historyi,total_components,base,turn):
    for tower in towers:
        tower_position = towers[tower].position
        nearest_to_tower = next(iter(goblins))
        if towers[tower].active == True:
            for goblin in goblins:
                if abs(tower_position - goblins[goblin].position) < abs(tower_position - goblins[nearest_to_tower].position):
                    nearest_to_tower = goblin

            if abs(goblins[nearest_to_tower].position - towers[tower].position) <= 1:
                if goblins[nearest_to_tower].health > 1:
                    goblins[nearest_to_tower].health -= 1
                    towers[tower].active = False
                    historyi.append(f"Turn : {turn} , {towers[tower].id} attacked {goblins[nearest_to_tower].id} for 1 damage. {goblins[nearest_to_tower].id} hp={goblins[nearest_to_tower].health}. ")
                    print(f"{towers[tower].id} attacked {goblins[nearest_to_tower].id} for 1 damage. {goblins[nearest_to_tower].id} hp={goblins[nearest_to_tower].health}. ")

                else:
                    historyi.append(f"Turn : {turn} , {goblins[nearest_to_tower].id} is killed ")
                    print(f"{goblins[nearest_to_tower].id} is killed ")
                    total_components[goblins[nearest_to_tower].position].remove(goblins[nearest_to_tower].id)
                    towers[tower].active = False
                    goblins.pop(nearest_to_tower)

        if towers[tower].active == True:        
            historyi.append(f"Turn : {turn} , {towers[tower].id} found no enemy in range. ")
            print(f"{towers[tower].id} found no enemy in range. ")
        else:
            towers[tower].active = True




    # for tower in towers:
    #     to_pop = []
    #     for goblin in goblins:

    #         if towers[tower].active == True:
    #             if towers[tower].position == goblins[goblin].position or towers[tower].position +1 == goblins[goblin].position or towers[tower].position -1 == goblins[goblin].position:

    #                 if goblins[goblin].health > 1:
    #                     goblins[goblin].health -= 1
    #                     towers[tower].active = False
    #                     historyi.append(f"Turn : {turn} , {towers[tower].id} attacked {goblins[goblin].id} for 1 damage. {goblins[goblin].id} hp={goblins[goblin].health}. ")
    #                     print(f"{towers[tower].id} attacked {goblins[goblin].id} for 1 damage. {goblins[goblin].id} hp={goblins[goblin].health}. ")

    #                 else:
    #                     historyi.append(f"Turn : {turn} , {goblins[goblin].id} is killed ")
    #                     print(f"{goblins[goblin].id} is killed ")
    #                     total_components[goblins[goblin].position].remove(goblins[goblin].id)
    #                     towers[tower].active = False
    #                     to_pop.append(goblin)

    #     for p in to_pop:
    #         goblins.pop(p)
    #     if towers[tower].active == True:        
    #         historyi.append(f"Turn : {turn} , {towers[tower].id} found no enemy in range. ")
    #         print(f"{towers[tower].id} found no enemy in range. ")
    #     else:
    #         towers[tower].active = True