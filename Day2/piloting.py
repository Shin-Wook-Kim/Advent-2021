fileObject = open("Day2/input.txt", "r")

Datalist = []

while(True):
    line = fileObject.readline()
    if not line:
        break
    Datalist.append(line.strip())

fileObject.close

#print(Datalist)

#coord = [0,0]
#
#for i in range(len(Datalist)):
#    s = Datalist[i]
#    if s[0] == 'f':
#        #print(s[8])
#        coord[0] = coord[0] + int(s[8])
#        #print(coord)
#    if s[0] == 'd':
#        #print(s[5])
#        coord[1] = coord[1] + int(s[5])
#        #print(coord)
#    if s[0] == 'u':
#        #print(s[3])
#        coord[1] = coord[1] - int(s[3])
#        #print(coord)
#
#a = coord[0] * coord[1]

#print(a)



coord = [0,0,0]

for i in range(len(Datalist)):
    s = Datalist[i]
    if s[0] == 'f':
        #print(s[8])
        n = int(s[8])
        coord[0] = coord[0] + n
        coord[1] = coord[1] + coord[2]*n 
        #print(coord)
    if s[0] == 'd':
        #print(s[5])
        coord[2] = coord[2] + int(s[5])
        #print(coord)
    if s[0] == 'u':
        #print(s[3])
        coord[2] = coord[2] - int(s[3])
        #print(coord)

a = coord[0] * coord[1]

print(a)