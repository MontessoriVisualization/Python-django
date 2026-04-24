// forin give only name of the key
const letslearnUsersArray=[{
    name:"saugat Bagale",
    age:23,
    isLogin:true
},{
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
},

]
//forin give only name of the key
for(let key in letslearnUsersArray){
    console.log(letslearnUsersArray[key].name)
}
//for of give only name
for(let key of letslearnUsersArray){
    console.log(key.name)
}


