const studentScores = [
   10, 85, 92, 78, 8, 5, 80, 95, 88, 76
];
// const totalMarkSum = studentScores.reduce(function(total,curren),0)
    const totalMarkSum = studentScores.reduce(function(total,current){
        console.log("valv:",total,current)
        return total + current
    }, 0);
console.log("Total Marks Sum:", totalMarkSum);  
//if we used for each for the same scenario
let total = 0;
studentScores.forEach(function(score){
    total += score;
})
console.log("Total Marks Sum using forEach:", total);

//fiter
const passingScores = studentScores.filter(function(score){
    return score>=75
})
console.log(passingScores)
const filtered=[];

for (const element of studentScores) {
    if(element>=75){
        filtered.push(element)

    }
    
}
console.log(filtered)


const letslearnUsersObject= [
    {name:"saugat Bagale",age:23,email:"saugat@example.com"},
    {name:"John Doe",age:30,email:"john@example.com"},
    {name:"Jane Smith",age:25,email:"jane@example.com"}

]
const userNames = letslearnUsersObject.filter(function(user){
    return user.age >= 25
}).map(function(user){
    return user.age
}).reduce(function(acc,user){
    return acc + user
},0)






console.log(userNames)
// const userNamesFor = [];
// function getUserNames(users){

//     for (const element of letslearnUsersObject) {
//         userNamesFor.push(element.name)
//     }
//     return userNamesFor;
// }

