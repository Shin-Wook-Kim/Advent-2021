fileObject = open("Day3/input.txt", "r")

Datalist = []

while(True):
    line = fileObject.readline()
    if not line:
        break
    Datalist.append(line.strip())

fileObject.close

#print(Datalist)

# count1 = [0,0,0,0,0,0,0,0,0,0,0,0]

#l = len(Datalist)

#for i in range(l):
#    for j in range(12):
#        a = Datalist[i][j]
#        if a == '1':
#            count1[j] = count1[j] + 1


#print(count1)

#gamma = [0,0,0,0,0,0,0,0,0,0,0,0]

#epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]

#for j in range(12):
#    if count1[j] > l - count1[j]:
#        gamma[j] = 1
#        epsilon[j] = 0
#    else:
#        gamma[j] = 0
#        epsilon[j] = 1

#print(gamma)
#print(epsilon)

#g = 0
#e = 0

#for j in range(12):
#    g = g + 2**(11-j) * gamma[j]
#    e = e + 2**(11-j) * epsilon[j]
    
#ans = g*e
#print(ans)


filtered = Datalist

for i in range(12):
    l = len(filtered)
    if l == 1:
        break
    count1 = 0
    for j in range(l):
        if filtered[j][i] == '1':
            count1 = count1 + 1
    if count1 >= len(filtered) - count1:
        oxysieve = '1'
    else:
        oxysieve = '0'
    temp = []
    for j in range(l):
        if filtered[j][i] == oxysieve:
            temp.append(filtered[j])
    filtered = temp

oxy = filtered[0]


filtered = Datalist

for i in range(12):
    l = len(filtered)
    if l == 1:
        break
    count1 = 0
    for j in range(l):
        if filtered[j][i] == '1':
            count1 = count1 + 1
    if count1 >= len(filtered) - count1:
        scrsieve = '0'
    else:
        scrsieve = '1'
    temp = []
    for j in range(l):
        if filtered[j][i] == scrsieve:
            temp.append(filtered[j])
    filtered = temp

scr = filtered[0]

#print(oxy)
#print(scr)
o = 0
s = 0

for j in range(12):
    o = o + 2**(11-j) * int(oxy[j])
    s = s + 2**(11-j) * int(scr[j])
    
ans = o*s
print(ans)




