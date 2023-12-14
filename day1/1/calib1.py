import re


file = open("list.txt","r").readlines()
file = [i.replace("\n","") for i in file] #for removing \n

outValue=0
for i in file:
    print(i)
    searchVal=re.findall("\d",i)
    outValue+=int(searchVal[0]+searchVal[-1])
print(outValue)
    