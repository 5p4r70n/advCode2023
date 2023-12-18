file=open("data.txt","r").readlines()
dataMain=[i.strip() for i in file]

red = "12"
green= "13"
blue ="14"


workingGames=0


def algo(data :str):
    # print (data)
    structure = {"Game":0,
             "blue":0,
             "green":0,
             "red":0} 

    structure["Game"]=data.split(":")[0].split(" ")[1].strip()
    
    for time in data.split(":")[1].split(";"):
        kk=time.split(",")
        for jj in kk:
            nos=jj.strip().split(" ")[0]
            colour=jj.strip().split(" ")[1]
            
            if int(structure[colour]) < int(nos):
                structure[colour]=nos

    return int(structure["blue"])*int(structure["green"])*int(structure["red"])

for i in dataMain:
    workingGames+=algo(i)

print(workingGames)
    

assert algo("Game 6: 4 blue, 8 green, 5 red; 9 green, 10 blue, 7 red; 11 blue, 10 red, 7 green; 8 red, 6 blue, 9 green") == 990