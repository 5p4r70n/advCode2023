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
    "A":12, "K":11, "Q":10, "J":9, "T":8, "9":7, "8":6, "7":5, "6":4, "5":3, "4":2, "3":1, "2":0
}

def calc(card:str):
   returnData={}
   for i in card:
       returnData[i]=card.count(i)
   print(returnData)
   
   if len(returnData) ==1:
        cardsSorted["fiveKind"].append(card)
   elif len(returnData) ==2:
       cardsSorted["fourKind"].append(card)
       
   elif len(returnData)==2 and :
        
       
        
        



calc("KKKTT")

print(cardsSorted)