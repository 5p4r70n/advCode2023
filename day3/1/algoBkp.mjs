import fs from 'fs'

const data = fs.readFileSync("data.txt",'utf8')
const lines = data.split("\r\n")
const splChars=['&', '+', '-', '#','@', '$', '*', '/', '%','=']
var splCharsPos={}
var numericPos={}

var aroundPos=(line,pos)=>{

    function hasCommonElement(array1, array2) {
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
            circle[line-1].push(pos-1)
            circle[line-1].push(pos)
            circle[line-1].push(pos+1)
        }
        
        if (belowLine){
            circle[line+1]=[]
            circle[line+1].push(pos-1)
            circle[line+1].push(pos)
            circle[line+1].push(pos+1)
        }
    }

    checkLeftRight();checkUpDown(); // finding the around values

    let isAdjecentToSplChar = function(){  
        let returnVal=false  

        Object.entries(circle).forEach(([key, value]) => {
            if (hasCommonElement(value,splCharsPos[key])){returnVal=true}
          });

        return returnVal
    }

    // console.log(circle)
    
return isAdjecentToSplChar()

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

//loading numerics
for (var i=0;i<lines.length;i++){
    var row=lines[i]
    numericPos[i]={}
    for (var j=0;j<row.length;j++){
        var char=row[j]
        if (!isNaN(char)){
            numericPos[i][j]=char
        }
    }
}

//find the full no

// Object.entries(numericPos).forEach(([lineNO,lineValue])=>{

//     Object.entries(lineValue).forEach(([charPos,char])=>{
//         if (aroundPos(Number(lineNO),Number(charPos))){

//             console.log(lineNO,charPos,char)

//         }
//     })
// })

let totSum=0

for (var i=0;i<lines.length;i++){
    var row=lines[i]
    let numberFound=false
    let validFound=false
    let theChar=""

    for (var j=0;j<row.length;j++){
        var char=row[j]

        console.log(j)

        if (char==="." && !numberFound){
            theChar=''
            console.log( ". check")
            continue
        }
        
        if(char==="." && validFound){
            totSum+=Number(theChar)
            theChar=''
            validFound=false
            numberFound=false
            console.log( "Valid found")
            continue
        }

        if (!isNaN(char)){
            numberFound=true
            if (aroundPos(i,j)){
                validFound=true
            }
            theChar+=char
            console.log( "number found")
            console.log(theChar)
            continue
        }    
    }
}

console.log(totSum)







