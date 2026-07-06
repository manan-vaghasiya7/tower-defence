import sys

def run_orc(orcs,historyi,total_components,base,turn):

    to_pop = []
    for orc in orcs:
        if orcs[orc].position == 4:
            base -= 1
            historyi.append(f"Turn : {turn} , {orcs[orc].id} attacked Base for 1 damage and {orcs[orc].id} is removed. Base hp ={base} ")
            print(f"{orcs[orc].id} attacked Base for 1 damage and {orcs[orc].id} is removed. Base hp ={base}  ")
            total_components[orcs[orc].position].remove(orcs[orc].id)
            to_pop.append(orc)
            if base == 0:
                historyi.append("YOU WON")
                print("YOU WON")
                sys.exit()

        else: 
            orcs[orc].position += 1
            historyi.append(f"{orcs[orc].id} moved from {orcs[orc].position-1} to {orcs[orc].position} ")
            print(f"{orcs[orc].id} moved from {orcs[orc].position-1} to {orcs[orc].position} ")
            total_components[orcs[orc].position-1].remove(orcs[orc].id)
            total_components[orcs[orc].position].append(orcs[orc].id)
    for p in to_pop:
        orcs.pop(p)
    