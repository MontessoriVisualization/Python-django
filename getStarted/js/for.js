
// for (let index = 0; index < 9; index++) {
// console.log(index)    
// }

// let  arrr = 0;
// for(let i=0 ; i<10; i++){
//     arrr+=i
    
// }

// console.log(arrr)


// ----- a loop that dosen't run--------------------------
// let arr = []

// for(let i=0; i>10;i++){
//     arr+=i
// }
// console.log(arr)


// let arr = []


// ------- infinite loop--------------------
// for(let i=0; i<10;i--){
// console.log("a")
// }
// console.log(arr)

//log 10 to 1
// for(let i=10;i>=0;i--){
//     console.log(i);
// }



// for(let i=0; i<10;++i){

//     console.log(i)
// }


// loging indvisual Array

// const arr =[1,2,3,4,5,6,7,8]
// for(let i=0; i<=arr.length; i++ ){
// console.log(arr[i])
// }


// const arr =["superman","batman","wonderwomen","flash","greenlanton","spiderman"]
// for(let i=arr.length-1; i>=0;i--){
//     console.log(arr[i])
// }

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
for(let i=0; i<letslearnUsersArray.length;i++){

    if(letslearnUsersArray[i].name=="subin"){
        continue;
    }
console.log(letslearnUsersArray[i])

}


for(let i=0;i<letslearnUsersArray.length;i++){
    if(!letslearnUsersArray[i].isLogin){
        console.log(!true)
        continue;
    }   
    console.log(letslearnUsersArray[i].name);







}


