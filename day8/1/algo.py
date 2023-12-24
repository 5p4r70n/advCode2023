fielData=open("data.txt","r").readlines()
route=[int(i) for i in fielData[0].strip().replace("L","0").replace("R","1")]

lanes={i.split("=")[0].strip():i.replace("(","").replace(")","").replace(" ","").split("=")[1].strip().split(",")  for i in fielData[1:] if i.strip()!='' }

# count=0
finalKey="ZZZ"


loopCount=0
def findZ(initKey,count):
    global loopCount
    print(initKey,count)
    

    # #to stop inifinite loop
    # if loopCount>=10:
    #     return "closed"

    if  count >= len(route) : 
        print("clear Count : ",count)
        findZ(initKey,0)
        
    else:    
        loopCount+=1
        if lanes[initKey][route[count]]== finalKey:
            print("finally",loopCount)
            return
        else:
            print("firing",lanes[initKey][route[count]],count)
            findZ(lanes[initKey][route[count]],count+1)

        
    
    
    
print(findZ("AAA",0))

# print(route,lanes)