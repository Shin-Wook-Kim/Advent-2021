fileObject = open("Day1/input.txt", "r")

Datalist = []

while(True):
    line = fileObject.readline()
    if not line:
        break
    Datalist.append(int(line.strip()))

fileObject.close

#comp = 0

#for x in range(len(Datalist)):
#    if x == 0:
#        prev = Datalist[x]
#        continue
#    if prev < Datalist[x]:
#        comp = comp + 1
#    prev = Datalist[x]

#print(comp)
    
acomp = 0
A = [0,0,0]
B = [0,0,0]

for i in range(len(Datalist)):
    if i == 0:
        A[0] = Datalist[i]
        continue
    B[2] = B[1]
    B[1] = B[0]
    B[0] = Datalist[i]
    if i >= 3:
        a = A[0] + A[1] + A[2]
        b = B[0] + B[1] + B[2]
        if b > a:
            acomp = acomp + 1
    A[2] = A[1]
    A[1] = A[0]
    A[0] = Datalist[i]

print(acomp)




 



# def NoInc(depths):