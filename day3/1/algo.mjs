import fs from 'fs'

const data = fs.readFileSync("data.txt",'utf8')
const lines = data.split("\r\n")
const splChars=['&', '+', '-', '#','@', '$', '*', '/', '%','=']
var splCharsPos={}
var numericPos={}

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

// //loading numerics
// for (var i=0;i<lines.length;i++){
//     var row=lines[i]
//     numericPos[i]={}
//     for (var j=0;j<row.length;j++){
//         var char=row[j]
//         if (!isNaN(char)){
//             numericPos[i][j]=char
//         }
//     }
// }

//find the full no

// Object.entries(numericPos).forEach(([lineNO,lineValue])=>{
//     console.log(lineNO)

//     Object.entries(lineValue).forEach(([positionValue,value])=>{
//         // console.log(lineNO,positionValue)
//         // console.log(aroundPos(lineNO,positionValue))

//         if (aroundPos(lineNO,positionValue)){
//             console.log(lineNO,positionValue,value)
//         }

//     })
    
// })

// console.log(aroundPos(0,9))


let totSum=0

for (var i=0;i<lines.length;i++){
    var row=lines[i]
    let numberFound=false
    let validFound=false
    let theChar=""
    //..708.220.184.
    for (var j=0;j<row.length;j++){
        let char=row[j]

        console.log(i,j,numberFound,validFound)

        if ((char==="." || splChars.includes(char))  && !numberFound){
            theChar=""
            // console.log( ". check ")
            continue
        }
        
        if ((char==="." || splChars.includes(char)) && numberFound && !validFound){
            theChar=""
            // console.log( ". check ")
            continue
        }
        

        if((char==="." || splChars.includes(char)) && validFound){
            totSum+=Number(theChar)
            console.log( "Valid found ",theChar)
            theChar=''
            validFound=false
            numberFound=false
            continue
        }

        if (!isNaN(char)){
            numberFound=true
            if (aroundPos(i,j)){
                validFound=true
            }
            theChar+=char
            // console.log( "number found")
            console.log(theChar)
            continue
        }    
    }
   
}

console.log(totSum)

