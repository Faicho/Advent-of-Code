#example input
#months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#12 red cubes, 13 green cubes, and 14 blue cubes?
file = open("inputday2.txt", "r")
ID_sum = 0
check = {"red" : 12, "green" : 13, "blue" : 14}

for line in file:
    valid = True
    id1, line = line.split(":")
    for sets in line.split(";"):
        for balls in sets.split(","):
            num, colour = balls.split()
            if int(num) > check.get(colour, 0):
                valid = False
    if valid:
        game, id1 = id1.split()
        ID_sum += int(id1)
print(ID_sum)

#part2
power = 0
file = open("inputday2.txt", "r")
file = file.read()
for line in file.split("\n"):
    line = line.split(":")[1]
    check2 = {"red" : 0, "green" : 0, "blue" : 0}
    for sets in line.split("; "):
        for balls in sets.split(", "):
            num, colour = balls.split()
            check2[colour] = max(int(num), check2[colour])
    power += check2["red"] * check2["green"] * check2["blue"]

print(power)

