# seeds= [3136945476,509728956,1904897211,495273540,1186343315,66026055,1381149926,11379441,4060485949,190301545,444541979,351779229,1076140984,104902451,264807001,60556152,3676523418,44140882,3895155702,111080695]


# seedsToSoil=[{"source":int(i.replace("  "," ").split(" ")[1].strip()),"destination":int(i.replace("  "," ").split(" ")[0].strip()),"range":int(i.replace("  "," ").split(" ")[2].strip())} for i in [i.strip() for i in open("seso.txt","r").readlines()]]
# soilToFert=[{"source":int(i.replace("  "," ").split(" ")[1].strip()),"destination":int(i.replace("  "," ").split(" ")[0].strip()),"range":int(i.replace("  "," ").split(" ")[2].strip())} for i in [i.strip() for i in open("soFe.txt","r").readlines()]]
# fertTowat=[{"source":int(i.replace("  "," ").split(" ")[1].strip()),"destination":int(i.replace("  "," ").split(" ")[0].strip()),"range":int(i.replace("  "," ").split(" ")[2].strip())} for i in [i.strip() for i in open("feWa.txt","r").readlines()]]
# watToLight=[{"source":int(i.replace("  "," ").split(" ")[1].strip()),"destination":int(i.replace("  "," ").split(" ")[0].strip()),"range":int(i.replace("  "," ").split(" ")[2].strip())} for i in [i.strip() for i in open("waLi.txt","r").readlines()]]
# lightToTemp=[{"source":int(i.replace("  "," ").split(" ")[1].strip()),"destination":int(i.replace("  "," ").split(" ")[0].strip()),"range":int(i.replace("  "," ").split(" ")[2].strip())} for i in [i.strip() for i in open("litemp.txt","r").readlines()]]
# tempHumid=[{"source":int(i.replace("  "," ").split(" ")[1].strip()),"destination":int(i.replace("  "," ").split(" ")[0].strip()),"range":int(i.replace("  "," ").split(" ")[2].strip())} for i in [i.strip() for i in open("temphum.txt","r").readlines()]]
# humidToLoca=[{"source":int(i.replace("  "," ").split(" ")[1].strip()),"destination":int(i.replace("  "," ").split(" ")[0].strip()),"range":int(i.replace("  "," ").split(" ")[2].strip())} for i in [i.strip() for i in open("humidLoca.txt","r").readlines()]]

# def findDest(source,dest,_range,input):
#     diff=(source+(_range-1))-input
#     return dest+(_range-1)-diff
# connection={}

# # find all soil
# def Looper(i,data):
#     for j in seedsToSoil:
#         if i>=j["source"] and i<=(j["source"]+j["range"]-1):
#             return findDest(j["source"],j["destination"],j["range"],i)
#     return i

# for i in seeds:
#    data =Looper(i,seedsToSoil)
#    if data !=None:
#         connection[i]={}
#         connection[i]["soil"]=data

# for key,value in connection.items():
#     data=Looper(value["soil"],soilToFert)
#     if data!=None:
#         connection[key]["ferti"]=data

   
# for key,value in connection.items():
#     data=Looper(value["ferti"],fertTowat)
#     if data!=None:
#         connection[key]["water"]=data

# for key,value in connection.items():
#     data=Looper(value["water"],watToLight)
#     if data!=None:
#         connection[key]["light"]=data

# for key,value in connection.items():
#     data=Looper(value["light"],lightToTemp)
#     if data!=None:
#         connection[key]["temperature"]=data

# for key,value in connection.items():
#     data=Looper(value["temperature"],tempHumid)
#     if data!=None:
#         connection[key]["humidity"]=data

# for key,value in connection.items():
#     data=Looper(value["humidity"],humidToLoca)
#     if data!=None:
#         connection[key]["location"]=data



# for key,value in connection.items():
#     print(value["location"])
   
   
   
   
   
# print(connection)

# found=[]
# for i in seeds:
#     for j in seedsToSoil:
#         if i>=j["source"] and i<=(j["source"]+j["range"]-1):
#             if i in found:
#                 print("double found")
#                 break
#             found.append(i)
#         elif (i not in found):
#             print(i)
            
# print(found)


_data=open("test.txt","r").readlines()

contents={}

nextKey=''
for i in _data:
    if "seeds:" in i:
        contents["seeds"]=[int(seed) for seed in i.split(":")[1].strip().replace("  "," ").split(" ")]
        continue
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



# for key,value in connection.items():
#     print(value["location"])
    
print(min([val["location"] for key,val in connection.items()]))

# print(connection)