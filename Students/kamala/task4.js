const letslearnUsersArray = [
{
    name:"saugat Bagale",
    age:23,
    isLogin:true
},
{
    name:"Nishant",
    age:24,
    isLogin:false
},
{
    name:"Aakriti",
    age:22,
    isLogin:true
},
{
    name:"subin",
    age:19,
    isLogin:false
},
{
    name:"kamala",
    age:19,
    isLogin:true
},
{
    name:"suman",
    age:19,
    isLogin:false
}
];

let result = [];

for (let i = 0; i < letslearnUsersArray.length; i++) {
    if (letslearnUsersArray[i].isLogin === true) {
        result.push(letslearnUsersArray[i].name);
    }
}

console.log(result);