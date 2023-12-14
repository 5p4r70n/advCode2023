import re


keyDic={"one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9",
        "1":"1",
        "2":"2",
        "3":"3",
        "4":"4",
        "5":"5",
        "6":"6",
        "7":"7",
        "8":"8",
        "9":"9",
}

file = open("list.txt","r").readlines()
file = [i.replace("\n","") for i in file ] #for removing \n

# def removeAlfaNos(data:str) -> str:
#     print(data)
#     searchValfront=re.findall("(one|two|three|four|five|six|seven|eight|nine)",data)
#     searchValRev=re.findall("(one|two|three|four|five|six|seven|eight|nine)$",data)
    
#     if (searchValfront!=[] and searchValRev!=[]) and  ( len(searchValfront[0]) + len(searchValRev[0]) > len(data)):
#         return keyDic[searchValfront[0]]+keyDic[searchValRev[0]]
    
#     if searchValfront!=[]:
#         data= data.replace(searchValfront[0],keyDic[searchValfront[0]])
   
#     if searchValRev!=[]:
#         data= data.replace(searchValRev[0],keyDic[searchValRev[0]])
    
#     print(data)
#     return data

# def calc(data:str)-> int:
#     searchVal=re.findall("\d",data)
#     return int(searchVal[0]+searchVal[-1])


# finalData=[removeAlfaNos(i) for i in file] #converting leading and trailing string nos to int  

    
# outValue=0
# for i in finalData:
#     outValue+=calc(i)
# print(outValue)


        
        
    

# assert removeAlfaNos("fdgvdfoneight15")=="fdgvdf1ight15"
# assert removeAlfaNos("fdgvdfoneight15two")=="fdgvdf1ight152"
# assert removeAlfaNos("fdgvdfonight15")=="fdgvdfonight15"
# assert removeAlfaNos("fdgonevdfonight15two")=="fdg1vdfonight152"
# assert removeAlfaNos("oneight")=="18"
# assert removeAlfaNos("one1eight")=="118"
# assert removeAlfaNos("1qeighthfzzsvsvtph")=="1q8hfzzsvsvtph"
# assert removeAlfaNos("4two66nineeightzjrzhgnxr")=="4266nine8zjrzhgnxr"



# assert calc("118")==18
# assert calc("1dsgdfg1sdgdfgdf8")==18
# assert calc("dsgdfg1dsgdfg1sdgdfgdf8sdfdsfg")==18
# assert calc("1q8hfzzsvsvtph")==18


def getValue(data:str)->int:
    # print(data)
    searchValfront=re.findall("(one|two|three|four|five|six|seven|eight|nine|\d)",data)
    searchValBack=re.findall("(?:(?!.+(?:zero|one|two|three|four|five|six|seven|eight|nine|\d)))(?:zero|one|two|three|four|five|six|seven|eight|nine|\d)",data)
    # print(searchValBack)
    # print(keyDic[searchValfront[0]]+keyDic[searchValBack[0]])
    
    return int(keyDic[searchValfront[0]]+keyDic[searchValBack[0]])



finalData=[getValue(i) for i in file] #converting leading and trailing string nos to int  

    
outValue=0
for i in finalData:
   outValue+=i
print(outValue)


assert getValue("fdgvdfoneight15")==15
assert getValue("fdgvdfoneight15two")==12
assert getValue("fdgvdfonight15")==15
assert getValue("fdgonevdfonight15two")==12
assert getValue("oneight")==18
assert getValue("one1eight")==18
assert getValue("1qeighthfzzsvsvtph")==18
assert getValue("4two66nineeightzjrzhgnxr")==48

