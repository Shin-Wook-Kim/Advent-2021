fileObject = open("Day4/input.txt", "r")

cstring = ''
rstring = ''
calls = []
boards = []
tempboard = []
temprow = [0,0,0,0,0]
temp = ''

linecheck = 0

while(True):
    line = fileObject.readline()
    if not line:
        break
    elif line[0] == '\n' and linecheck > 1:
        boards.append(tempboard)
        tempboard = []
    elif line[0] == '\n':
        linecheck = linecheck + 1
    elif linecheck == 0:
        cstring = line.strip()
        linecheck = linecheck + 1
    else:
        rstring = line.strip()
        if rstring[1] == ' ':
            temprow[0] = int(rstring[0])
            n = 2
        else:
            temp = rstring[0] + rstring[1]
            temprow[0] = int(temp)
            n=3
        for i in range(1,5):
            if line[n] == ' ':
                temprow[i] = int(rstring[n+1])
            else:
                temp = rstring[n] + rstring[n+1]
                temprow[i] = int(temp)
            n = n + 3
        tempboard.append(temprow)
        temprow = [0,0,0,0,0]


fileObject.close

print(cstring)
print(boards)