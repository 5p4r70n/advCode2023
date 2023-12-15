import fs from 'fs'

const data = fs.readFileSync("data.txt",'utf8')
const lines = data.split("\r\n")
const splChars=['&', '+', '-', '#','@', '$', '*', '/', '%','=']
var splCharsPos={}
let matrix =[]

for (let i = 0; i < 140; i++) {
    let temp=[]
    let row=lines[i]
    for (let j = 0; j < 140; j++) {
        temp.push(row[j])
    }
    matrix.push(temp)
}



// loading special Chars
for (var i=0;i<lines.length;i++){
    var row=lines[i]
    splCharsPos[i]=[]
    for (var j=0;j<row.length;j++){
        var char=row[j]
        if (splChars.includes(char)){
            splCharsPos[i].push(j)
        }
    }
}


var aroundPos=(line,pos)=>{
    line=Number(line)
    pos=Number(pos)
    function hasCommonElement(array1, array2) {
        // console.log(array1,array2)
        return array1.some(value => array2.includes(value));
      }

    let aboveLine=(()=>{if (line != 0){return true}else{return false}})();
    let belowLine=(()=>{if (line !=139 ){return true}else{return false}})(); //139 is the max lines aka 1-140, so 0-139
    let leftVal=(()=>{if (pos !=0 ){return true}else{return false}})(); 
    let rightVal=(()=>{if (pos !=139 ){return true}else{return false}})(); 

    let circle={}

    let checkLeftRight =function(){
        circle[line]=[]
        if (leftVal){
            circle[line].push(pos-1)
        }
        if (rightVal){
            circle[line].push(pos+1)
        }
    }

    let checkUpDown = function(){
        if (aboveLine){
            circle[line-1]=[]
            if (leftVal){circle[line-1].push(pos-1)}
            circle[line-1].push(pos)
            if (rightVal){circle[line-1].push(pos+1)}
        }
        
        if (belowLine){
            circle[line+1]=[]
            if (leftVal){circle[line+1].push(pos-1)}
            circle[line+1].push(pos)
            if (rightVal){circle[line+1].push(pos+1)}
        }
    }

    checkLeftRight();checkUpDown(); // finding the around values
    // console.log(circle)

    let isAdjecentToSplChar = function(){  
        let returnVal=false  
        Object.entries(circle).forEach(([key, value]) => {
            // console.log(key, value);
            if (hasCommonElement(value,splCharsPos[key])){returnVal=true}
          });

        return returnVal
    }

    // console.log(circle)
    
return isAdjecentToSplChar()

}


let validList=[]

let totSum=0
for (let i = 0; i < 140; i++) {
    let row = lines[i]
    let validFound=false
    let numberFound=false
    let number=''
    for (let j = 0; j < 140; j++) {
        let char = row[j]
        
        if (!isNaN(char)){
            numberFound=true
            number+=char
            console.log(i,j,validFound,numberFound,char)
        }
        
        if (!isNaN(char) && aroundPos(i,j)){
            validFound=true
        }
        
        if (splChars.includes(char) || char==="."){

            if (validFound){
                totSum+=Number(number)
                validList.push(i +":" +j+":" +number)
            }

            number=''
            numberFound=false
            validFound=false
        }
    }
    if (validFound){
        totSum+=Number(number)
        validList.push(i +":" +j+":" +number)
    }
}
console.log(validList)
console.log(totSum)

fs.writeFile(
    './my.json',
    JSON.stringify(validList),
    function (err) {
        if (err) {
            console.error('Crap happens');
        }
    }
);
