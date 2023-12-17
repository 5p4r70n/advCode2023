_data=open("test.txt","r").readlines()

contents={}


# for i in _data:
#     if "seeds:" in i:
#         contents["seeds"]=[]
#         splitedLine=i.split(":")[1].strip().replace("  "," ").split(" ")
#         for j in range(0,len(splitedLine),2):
#             print(splitedLine[j])
#             contents["seeds"].extend( [ k for k in range ( int(splitedLine[j]) , int(splitedLine[j])+int(splitedLine[j+1] ) ) ])
#         break
# print(contents)


nextKey=''
for i in _data:
    if "seeds:" in i:
        contents["seeds"]=[]
        splitedLine=i.split(":")[1].strip().replace("  "," ").split(" ")
        for j in range(0,len(splitedLine),2):
            print(splitedLine[j])
            contents["seeds"].extend( [ k for k in range ( int(splitedLine[j]) , int(splitedLine[j])+int(splitedLine[j+1] ) ) ])
    
    print(i,i.strip()=="")
    
    if i.strip()=="":
        continue    
    
    if "seed-to-soil map:" in i:
        nextKey="seed-to-soil"
        contents[nextKey]=[]
        continue
    
    if "soil-to-fertilizer map:" in i:
        nextKey="soil-to-fertilizer"
        contents[nextKey]=[]
        continue    

    if "fertilizer-to-water map:" in i:
        nextKey="fertilizer-to-water map"
        contents[nextKey]=[]
        continue    

    if "water-to-light map:" in i:
        nextKey="water-to-light map"
        contents[nextKey]=[]
        continue    

    if "light-to-temperature map:" in i:
        nextKey="light-to-temperature map"
        contents[nextKey]=[]
        continue    

    if "temperature-to-humidity map:" in i:
        nextKey="temperature-to-humidity map"
        contents[nextKey]=[]
        continue    

    if "humidity-to-location map:" in i:
        nextKey="humidity-to-location map"
        contents[nextKey]=[]
        continue    
    
    contents[nextKey].append({"destination":int(i.strip().replace("  "," ").split(" ")[0]),"source":int(i.strip().replace("  "," ").split(" ")[1]),"range":int(i.strip().replace("  "," ").split(" ")[2])})




def findDest(source,dest,_range,input):
    diff=(source+(_range-1))-input
    return dest+(_range-1)-diff

connection={}

# find all soil
def Looper(i,data):
    for j in data:
        if i>=j["source"] and i<=(j["source"]+j["range"]-1):
            return findDest(j["source"],j["destination"],j["range"],i)
    return i

for i in contents["seeds"]:
   data =Looper(i,contents["seed-to-soil"])
   if data !=None:
        connection[i]={}
        connection[i]["soil"]=data

for key,value in connection.items():
    data=Looper(value["soil"],contents["soil-to-fertilizer"])
    if data!=None:
        connection[key]["ferti"]=data

   
for key,value in connection.items():
    data=Looper(value["ferti"],contents["fertilizer-to-water map"])
    if data!=None:
        connection[key]["water"]=data

for key,value in connection.items():
    data=Looper(value["water"],contents["water-to-light map"])
    if data!=None:
        connection[key]["light"]=data

for key,value in connection.items():
    data=Looper(value["light"],contents["light-to-temperature map"])
    if data!=None:
        connection[key]["temperature"]=data

for key,value in connection.items():
    data=Looper(value["temperature"],contents["temperature-to-humidity map"])
    if data!=None:
        connection[key]["humidity"]=data

for key,value in connection.items():
    data=Looper(value["humidity"],contents["humidity-to-location map"])
    if data!=None:
        connection[key]["location"]=data



    
print(min([val["location"] for key,val in connection.items()]))
