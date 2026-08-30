with open("input.txt", "r") as file:

    dataList = []

    while(True):
        line = file.readline()
        if not line:
            break
        dataList.append(int(line.strip()))

def countIncrease(array):
    res = 0
    l = len(array)
    for i in range(l-1):
        if array[i] < array[i+1]:
            res += 1
    return res

def countSlidingWindowIncrease(array):
    res = 0
    l = len(array)
    prev = array[0] + array[1] + array[2]
    for i in range(l-3):
        cur = prev - array[i] + array[i+3]
        if prev < cur:
            res += 1
        prev = cur
    return res


print(countSlidingWindowIncrease(dataList))