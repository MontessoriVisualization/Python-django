// JavaScript Basics - Notes with Examples

// 1) Variables: var, let, const
// var   -> function scoped (older style)
// let   -> block scoped, can be reassigned
// const -> block scoped, cannot be reassigned

let city = "Kathmandu";
console.log(city)
city="porkhara"
const country = "Nepal";
var year = 2026;

console.log("Variables:");
console.log("city =", city);
console.log("country =", country);
console.log("year =", year);

city = "Pokhara"; // let can change
year = 2027;       // var can change
console.log("updated city =", city);
console.log("updated year =", year);

// 2 Primitive data types
// string, number, boolean, null, undefined, (bigint, symbol)not included here

const userName = "Sauga";
const age = 20;
const isStudent = true;
const emptyValue = null;
let notAssigned;

console.log("\nData Types:");
console.log("typeof userName =", typeof userName);
console.log("typeof age =", typeof age);
console.log("typeof isStudent =", typeof isStudent);
console.log("typeof emptyValue =", typeof emptyValue); // object (JS quirk)
console.log("typeof notAssigned =", typeof notAssigned);

// 3) Type conversion
// Number(), String(), Boolean()

const n1 = "11";
const n2 = "22";

console.log("\nType Conversion:");
console.log("Number('11') + Number('22') =", Number(n1) + Number(n2)); // 33
console.log("String(123) =", String(123));
console.log("Boolean(1) =", Boolean(1)); // true
console.log("Boolean(0) =", Boolean(0)); // false
console.log("Boolean('') =", Boolean("")); // false
console.log("Boolean(null) =", Boolean(null)); // false
console.log("Boolean(undefined) =", Boolean(undefined)); // false
console.log("Boolean('hello') =", Boolean("hello")); // true

       

// 4) if/else condition

let accessResult;
if (age >= 18) {
    accessResult = "adult";
} else {
    accessResult = "minor";
}

console.log("\n If/Else:"); //\n for new line
console.log("age check:", accessResult);

