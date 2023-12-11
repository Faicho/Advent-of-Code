#example input
#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#12 red cubes, 13 green cubes, and 14 blue cubes?
file = open("inputday2.txt", "r")
ID_sum = 0
check = {"red" : 12, "green" : 13, "blue" : 14}

for line in file:
    valid = True
    id1, line = line.split(":")
    for sets in line.split(";"):
        for balls in line.split(","):
            num, colour = balls.split()
            if int(num) > check.get(colour, 0):
                valid = False
    if valid:
        game, id1 = id1.split()
        ans += int(id1)
print(ans)

