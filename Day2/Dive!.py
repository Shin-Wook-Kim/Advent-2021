data = []

with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        d, m = line.split()
        data.append((d, int(m)))
        line = file.readline()

def calculatePositionProduct(data):
    res = [0,0]
    for i in range(len(data)):
        d, m = data[i]
        if d == "forward":
            res[0] += m
        if d == "down":
            res[1] += m
        if d == "up":
            res[1] -= m
    
    return res[0] * res[1]



def calcPosProdWithAim(data):
    res = [0,0,0]
    for i in range(len(data)):
        d, m = data[i]
        if d == "forward":
            res[0] += m
            res[1] += m * res[2]
        if d == "down":
            res[2] += m
        if d == "up":
            res[2] -= m
    
    return res[0] * res[1]


print(calcPosProdWithAim(data))

