data=open("data.txt","r").readlines()
lines=[i.strip() for i in data]

cards={}

for i in lines:
    cardNo=i.split(":")[0].split(" ")[-1].strip()
    winKeys=[int(key) for key in [key.strip() for key in i.split(":")[1].split("|")[0].strip().split(" ")] if key !='']
    ourKeys=[int(key) for key in [key.strip() for key in i.split(":")[1].split("|")[1].strip().split(" ")] if key !='']
    cards[cardNo]={"winKeys":winKeys,"ourKeys":ourKeys}

tot=0

for key,i in cards.items():
    count=0
    for ourKey in i["ourKeys"]:
        if ourKey in i["winKeys"]:
            # print(key,ourKey)
            count+=1
    if count !=0:
        tot+=2**(count-1)
print(tot)
    