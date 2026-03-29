//check whether a person is elligible to vote or not
//should be 18 plus and should havea citizenship to cast vote

const age=24
const citizenshipNum=23456
if (age>=18){
    if(Boolean(citizenshipNum)){
        console.log("You are elligible to cast vote...")
    }
}
else{
    console.log("you are not allowed to vote!!!")
}