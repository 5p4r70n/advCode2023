import fs from 'fs'

const data = fs.readFileSync("data.txt",'utf8')
const lines = data.split("\n")

let matrix =[]


for (let line of lines) {
    let temp=[]
    for (let j = 0; j < 140; j++) {
        let char=line[j]
        
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



findNumber(lineNO,pos){



}




for (let i = 0; i < 140; i++) {
    let row=lines[i]
    for (let j = 0; j < 140; j++) {
        let char = row[j]
        if (char==="*"){
                console.log(aroundPos(i,j))
            }
    }
    // console.log(row)
}