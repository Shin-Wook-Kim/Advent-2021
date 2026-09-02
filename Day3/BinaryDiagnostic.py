data = []

with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        data.append(line.split()[0])
        line = file.readline()


def getFreqs(data):
    length = len(data[0])
    zeroFreqs = [0 for _ in range(length)]
    oneFreqs = [0 for _ in range(length)]
    for s in data:
        for i in range(length):
            if s[i] == '1':
                oneFreqs[i] += 1
            else:
                zeroFreqs[i] += 1
    return zeroFreqs, oneFreqs


def getPowerConsumption(zeroFreqs, oneFreqs):
    gamma = 0
    epsilon = 0
    length = len(zeroFreqs)
    for i in range(length):
        if zeroFreqs[i] > oneFreqs[i]:
            epsilon += 2**(length-i-1)
        else:
            gamma += 2**(length-i-1)
    return gamma*epsilon




def helper(data, curPos, target):
    newData = []
    for s in data:
        if s[curPos] == target:
            newData.append(s)
    return newData


def convert(bs):
    l = len(bs)
    res = 0
    for i in range(l):
        res += int(bs[i]) * (2**(l-i-1))
    return res


def getLifeSupportRating(data):
    cols = len(data[0])


    rows = len(data)
    zeroFreqs, oneFreqs = getFreqs(data)

    newData = [d for d in data]

    for i in range(cols):
        if zeroFreqs[i] <= oneFreqs[i]:
            mostCommon = '1'
        else:
            mostCommon = '0'
        newData = helper(newData, i, mostCommon)
        if len(newData) <= 1:
            break
        zeroFreqs, oneFreqs = getFreqs(newData)

    o = newData[0]


    newData = [d for d in data]

    for i in range(cols):
        if zeroFreqs[i] <= oneFreqs[i]:
            leastCommon = '0'
        else:
            leastCommon = '1'
        newData = helper(newData, i, leastCommon)
        if len(newData) <= 1:
            break
        zeroFreqs, oneFreqs = getFreqs(newData)

    c = newData[0]

    return convert(o) * convert(c)



print(getLifeSupportRating(data))