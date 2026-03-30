//check whether a person is elligible to vote or not
const age = 20;
const citizenshipNum = 12345;

if (age >= 18) {
    if (citizenshipNum) {
        console.log("You are eligible to vote");
    } else {
        console.log("You don't have citizenship");
    }
} else {
    console.log("You are under 18, not eligible");
}