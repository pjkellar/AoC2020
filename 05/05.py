import math

with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

def findRow(boardingPass):
    min = 0
    max = 127
    for char in boardingPass[:7]:
        if char == "F":
            max = math.floor((min+max)/2)
        elif char == "B":
            min = math.ceil((min+max)/2)
    return max

def findSeat(boardingPass):
    right = 7
    left = 0
    for char in boardingPass[-3:]:
        if char == "R":
            left = math.ceil((right+left)/2)
        elif char == "L":
            right = math.floor((right+left)/2)
    return right

highest = 0
seatIDs = []
for boardingPass in data:
    seatID = (findRow(boardingPass)*8) + (findSeat(boardingPass))
    seatIDs.append(int(seatID))
    if seatID > highest:
        highest = int(seatID)

print("The highest seat ID is {}".format(highest))