file = open('inputday1.txt', 'r')
calib = 0
calib2 = 0

#zero isn't needed but the list is enumerated
digitNames = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def part_2(line):
    for num, name in enumerate(digitNames):
        line = line.replace(name, f"{name}{num}{name}")
    return line

for line in file:
    line = part_2(line)
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)
    lineSum = int(digits[0] + digits[-1])
    calib += lineSum

print(calib)


