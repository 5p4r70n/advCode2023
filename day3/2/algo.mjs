import fs from 'fs'

const data = fs.readFileSync("data.txt",'utf8')
const lines = data.split("\n")
const splChars=['&', '+', '-', '#','@', '$', '*', '/', '%','=']

let matrix =[]


for (let line of lines) {
    let temp=[]
    for (let j = 0; j < 140; j++) {
        let char=line[j]
        temp.push(char)
    }
    matrix.push(temp)
}


var aroundPos=(line,pos)=>{
    line=Number(line)
    pos=Number(pos)

    let aboveLine=(()=>{if (line != 0){return true}else{return false}})();
    let belowLine=(()=>{if (line !=139 ){return true}else{return false}})(); //139 is the max lines aka 1-140, so 0-139
    let leftVal=(()=>{if (pos !=0 ){return true}else{return false}})(); 
    let rightVal=(()=>{if (pos !=139 ){return true}else{return false}})(); 

    let circle={"top":[],"bottom":[],"left":[],"right":[]}

    let checkLeftRight =function(){
        if (leftVal){
            circle["left"].push(pos-1)
        }
        if (rightVal){
            circle["right"].push(pos+1)
        }
    }

    let checkUpDown = function(){
        if (aboveLine){
            if (leftVal){circle["top"].push(pos-1)}
            circle["top"].push(pos)
            if (rightVal){circle["top"].push(pos+1)}
        }
        
        if (belowLine){
            circle["bottom"]=[]
            if (leftVal){circle["bottom"].push(pos-1)}
            circle["bottom"].push(pos)
            if (rightVal){circle["bottom"].push(pos+1)}
        }
    }

    checkLeftRight();checkUpDown(); // finding the around values
    
return circle

}



function findNumber(lineNO,pos){

    
    
    let circleValues={ "left":0,
                    "right":0,
                    "top":0,
                    "bottom":0}

    if (pos["left"] != []){
        let no=''
        for (let i = pos["left"][0];i>=0;i--){
            if(splChars.includes(lines[lineNO][i]) || lines[lineNO][i]==="." ){
                break
            }
            no=lines[lineNO][i]+no
        } 
        circleValues["left"]=Number(no)       
    }

    if (pos["right"]!=[]){
        let no=''
        for (let i = pos["right"][0];i<140;i++){
            if(splChars.includes(lines[lineNO][i]) || lines[lineNO][i]==="." ){
                break
            }
            no=no+lines[lineNO][i]
        }  
        circleValues["right"]=Number(no) 
    }

    if (pos["top"] !=[]){

        let no =''

        let leftVal=pos["top"][0]
        let midval=pos["top"][1]
        let rightVal=pos["top"][2]

        let topLine=lineNO-1

        for (let i = rightVal;i<140;i++){
            if(splChars.includes(lines[topLine][i]) || lines[topLine][i]==="." ){
                break
            }
            no=no+lines[topLine][i]
        } 

        if ( !isNaN(lines[topLine][midval])){
            no=lines[topLine][midval]+no
        }else{
            circleValues["topRight"]=Number(no)
            no=''
        }

        for (let i = leftVal;i>=0;i--){
            if(splChars.includes(lines[topLine][i]) || lines[topLine][i]==="." ){
                break
            }
            no=lines[topLine][i]+no
        } 

        circleValues["top"]=Number(no)
    }

    if (pos["bottom"] !=[]){

        let no =''

        let leftVal=pos["bottom"][0]
        let midval=pos["bottom"][1]
        let rightVal=pos["bottom"][2]

        let topLine=lineNO+1
        
        for (let i = rightVal;i<140;i++){
            if(splChars.includes(lines[topLine][i]) || lines[topLine][i]==="." ){
                break
            }
            no=no+lines[topLine][i]
        } 

        if ( !isNaN(lines[topLine][midval])){
            no=lines[topLine][midval]+no
        }else{
            circleValues["botRight"]=Number(no)
            no=''
        }

        for (let i = leftVal;i>=0;i--){
            if(splChars.includes(lines[topLine][i]) || lines[topLine][i]==="." ){
                break
            }
            no=lines[topLine][i]+no
        } 

        circleValues["bottom"]=Number(no)


    }

    return circleValues

}





let out = []
for (let i = 0; i < 140; i++) {
    let row=lines[i]
    for (let j = 0; j < 140; j++) {
        let char = row[j]
        if (char==="*"){
                out.push(findNumber(i,aroundPos(i,j)))
            }
    }
}
let totSum=0
for (let i of out){
   let elements=Object.values(i).filter(x=> x!=0)
    if (elements.length >1){
        totSum+=elements[0]*elements[1]
    }
}

console.log(totSum)
