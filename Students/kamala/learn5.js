// const studentScores =[
//     10,85,92,78,88,95,80
// ];
// const total=studentScores.reduce(function(total,current){
//     console.log("value:",total,current)
//     return total+ current
// },0);
// console.log("Total Marks Sum :",total)

// for in use 
const array={
    name:"Adhikari", age:20,email:"adhikari@gmail.com"
}
for (const key in array){
    console.log(array[key])
}
// for of use 

const array2={
    name:"Adhikari", age:20,email:"adhikari@gmail.com"
}
for (const [key, value] of Object.entries(array2)) {
    console.log(key, value)
}
