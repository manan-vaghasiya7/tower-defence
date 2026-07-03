import sys

def run_goblins(goblins,historyi,total_components,base,turn):

    to_pop = []
    for goblin in goblins:
        if goblins[goblin].position == 4:
            base -= 1
            historyi.append(f"Turn : {turn} , {goblins[goblin].id} attacked Base for 1 damage and {goblins[goblin].id} is removed. Base hp ={base} ")
            print(f"{goblins[goblin].id} attacked Base for 1 damage and {goblins[goblin].id} is removed. Base hp ={base}  ")
            total_components[goblins[goblin].position].remove(goblins[goblin].id)
            to_pop.append(goblin)
            if base == 0:
                historyi.append("YOU WON")
                print("YOU WON")
                sys.exit()

        else: 
            goblins[goblin].position += 1
            historyi.append(f"{goblins[goblin].id} moved from {goblins[goblin].position-1} to {goblins[goblin].position} ")
            print(f"{goblins[goblin].id} moved from {goblins[goblin].position-1} to {goblins[goblin].position} ")
            total_components[goblins[goblin].position-1].remove(goblins[goblin].id)
            total_components[goblins[goblin].position].append(goblins[goblin].id)
    for p in to_pop:
        goblins.pop(p)
    