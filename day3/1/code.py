file=open("data.txt","r").readlines()

mainData=[i.strip() for i in file]

splChars=['&', '+', '-', '#', '@', '$', '*', '/', '%', '=']

splCharPos={}


for i in range(0,len(mainData)):
    row=mainData[i]
    splCharPos[i]=[]
    
    for j in range(0,len(row)):
        char=row[j]
        if char in splChars:
            splCharPos[i].append(j)

valueMap={}            

for i in range(0,len(mainData)):
    row=mainData[i]
    valueMap[i]={}
    for j in range(0,len(row)):
        char=row[j]
        if char.isnumeric():
            valueMap[i][j]=char

print(valueMap)
            
                        


