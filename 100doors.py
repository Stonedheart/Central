DOOR_OPEN = True
DOOR_CLOSED = False
DOORS_COUNT = 4

#list init
doors = []

for i in range(1, DOORS_COUNT+1):
    doors.append(DOOR_CLOSED)


#walkthrough
print(doors)

for walk in range(1, DOORS_COUNT+1):
    for index, door in enumerate(doors):
        if (index+1) % walk == 0:
            if doors[index] == True:
                doors[index] = False
            else:
                doors[index] = True

    print(doors)


#final display
opened_doors = ""

for index, door in enumerate(doors):
    if door == DOOR_CLOSED:
        opened_doors = opened_doors + ', ' + str(index+1)


print("This doors are open: " + opened_doors)
