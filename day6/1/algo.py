dataInit ={
    1:{
        "time":59,
        "distance":597
    },
    2:{
        "time":79,
        "distance":1234
    },
    3:{
        "time":65,
        "distance":1032
    },
    4:{
        "time":75,
        "distance":1328
    },
}

# dataInit ={
#     1:{
#         "time":7,
#         "distance":9
#     },
#     2:{
#         "time":15,
#         "distance":40
#     },
#     3:{
#         "time":30,
#         "distance":200
#     }
# }


def calAlgo(data):
    count=0
    for i in range(1,data["time"]+1):
        if i*(data["time"]-i)>data["distance"]:
            count+=1
    return count
        

op=1

for i in dataInit:
    op=op*calAlgo(dataInit[i])

print(op)

    

