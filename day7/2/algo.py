## using weightage sort
## use always waightage "(14**(5-i))" bigger than dict values, here 13 is bigger so use 13 or more
#smaller values make the given weight makes chaos in sorting

data=open("data.txt","r").readlines()
masterData={i.split(" ")[0].strip():i.split(" ")[1].strip() for i in data}

cardsSorted={
    "fiveKind":[],
    "fourKind":[],
    "fullHouse":[],
    "threeKind":[],
    "twoPair":[],
    "onePair":[],
    "highCard":[]
}

dictionary={
    "A":13, "K":12, "Q":11, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2,"J":1,
}


def weightCalc (cardName):
    weight=0
    for i in range(0,len(cardName)):
        weight+= dictionary[cardName[i]]*((100**(5-i)))
        # print(weight)
    return weight

def calc(card:dict):
   charCount={}
   
   for i in card["name"]:
       charCount[i]=card["name"].count(i)
       
   card["weight"]=weightCalc(card["name"])
   
   
   if len(charCount) ==1:
        cardsSorted["fiveKind"].append(card)
        
   elif len(charCount) ==2:
       for i in charCount:
           if charCount[i] == 4 :
        
                if "J" in charCount:
                    cardsSorted["fiveKind"].append(card)
                else:
                    cardsSorted["fourKind"].append(card)
                break
            
           if charCount[i] == 2:
               
                if "J" in charCount:
                    cardsSorted["fiveKind"].append(card)
                else:
                    cardsSorted["fullHouse"].append(card)
                break
       
   elif len(charCount) ==3:
       for i in charCount:
           if charCount[i] == 3:
                if "J" in charCount:
                    cardsSorted["fourKind"].append(card)
                else:
                    cardsSorted["threeKind"].append(card)
                break
           if charCount[i] == 2:
                if "J" in charCount:
                    if charCount["J"]==2: 
                        cardsSorted["fourKind"].append(card)
                    else:
                         cardsSorted["fullHouse"].append(card)
                else:
                    cardsSorted["twoPair"].append(card)
                break
            
   elif len(charCount) ==4:
       if "J" in charCount:
           cardsSorted["threeKind"].append(card)
       else:
            cardsSorted["onePair"].append(card)
            
   elif len(charCount) ==5:
       if "J" in charCount:
           cardsSorted["onePair"].append(card)
       else:
            cardsSorted["highCard"].append(card)
        
for i in masterData:
    calc({"name":i,"value":int(masterData[i])})

tot=0
for i in cardsSorted:
    tot+=len(cardsSorted[i])
    # print(i,len(cardsSorted[i]))
print(tot)

## sorting the cards
for i in cardsSorted:
    # print(cardsSorted[i])
    cardsSorted[i]=sorted(cardsSorted[i], key=lambda x: x['weight'],reverse=True)
    # print(cardsSorted[i])

listOfValue=[]

for i in cardsSorted:
    for cards in cardsSorted[i]:
        listOfValue.append(cards["value"])


count=1
finalValue=0
for i in listOfValue[::-1]:
    # print(i,"X",count)
    finalValue+=i*count
    count+=1

print(finalValue)


# print(weightCalc("AAT5A"))
# print("\n")
# print(weightCalc("AAJA2"))