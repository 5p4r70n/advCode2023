import fs from 'fs'

const data = fs.readFileSync("data.txt",'utf8')
const lines = data.split("\r\n")

let cards ={}

for (let i of lines){
    let cardNo=Number(i.split(":")[0].split(" ")[-1])
    console.log(cardNo)
    let winKeys=i.split(":")[1].split("|")[0].split(" ").filter(x=>x!='').map(Number)
    let ourKeys=i.split(":")[1].split("|")[1].split(" ").filter(x=>x!='').map(Number)
    cards[cardNo]={"winKeys":winKeys,"ourKeys":ourKeys}
}


// function totPoint(cardNo){
//     let value= cards[cardNo]
//     let totPoint=0
//     let count=0



//     for (let entries of value["ourKeys"]){
//         if (value["winKeys"].includes(entries)){
//             count+=1}}

//     if (count !=0){
//         console.log(count)
//         totPoint+=(2**(count-1))
//     }

//     return totPoint

// }




// Object.values(cards).forEach((value)=>{
//     let count=0
//     for (let entries of value["ourKeys"]){
//         if (value["winKeys"].includes(entries)){
//             count+=1
//         }
//     }
//     if (count !=0){
//         // console.log(count , (2**(count-1)))
//         totPoint+=(2**(count-1))
//     }
// })



Object.keys(cards).forEach(key => {
    console.log((key))
});