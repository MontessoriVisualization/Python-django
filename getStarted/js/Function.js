//function declaration
function add(a=3, b=2) {// a and b are parameters
    console.log(a+b)
}
add(5, 10) // 5 and 10 are arguments
add()

function greet(name) {
    return `Hello, ${name}! Welcome to JavaScript functions.`;
}
const message1 = greet("Saugat");
const message2 = greet("Aakriti");
console.log(message1);
console.log(message2);

//arrow function
const addArrow = (a, b) => {
    console.log(a + b);
};
addArrow(5, 10);

//immedeatly invoked function expression (IIFE) features it runs as soon as it is defined and only once
(function(a,b) {

    console.log(a*b)
})(5,10);

const globalVariable ="I am a global variable.";

function outerFunction() {
    console.log(globalVariable); 
    const outerVariable = "I am from the outer function.";

    function innerFunction() {
        console.log("this is a inner funcion"); // Accessing variable from outer function
        console.log(outerVariable); // Accessing variable from outer function
    }
    console.log("This is the outer function.");
        innerFunction(); // Calling the inner function
}
// console.log(outerVariable); // This will cause an error because outerVariable is not accessible here
outerFunction();

useCall();

function useCall() {
    console.log("This is a function using call method.");
}


// unecalls()
const unecalls = function() {// This is a function expression assigned to a variable
    console.log("This is a function using call method.");
}
unecalls();

const unecallsArrow = (a) => ++a ;  // This is an arrow function that takes one parameter 'a' and returns 'a' incremented by 1

console.log(unecallsArrow(19))

