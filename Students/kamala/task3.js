
const num1 = 5;
const num2 = new Number(5);
console.log(num1,num2);
console.log(num1+num2);

const num3 = 123.456789;
console.log(typeof num1);
console.log(num3.toPrecision(6)); // will give 6 significant digits meaning 123.456789 will become 123.457
console.log(num3.toFixed(3)); // will give 3 digits after decimal point meaning 123.456789 will become 123.46
// console.log(num3.valueOf()); // will give the primitive value of the number object meaning 123.456789 will become 123.456789
console.log(Math.min(1,2,4,5))
console.log(Math.max(1,2,4,5))
console.log(Math.abs(-4))
console.log(Math.round(4.5))//ans will be 5 because .5 and above round u
console.log(Math.ceil(4.01)) // ans will be 5 because ceil means round up
console.log(Math.floor(4.99999999)) // ans will be 4 because floor means round down
console.log(Math.round(Math.random()*10)) //random number between 0 to 1 but not including 1
// 0-1
// 0.13453*10=1.3453
// 0.99999*10=9.9999
// round  1.5 => 2
// round 9.9999 => 10
// floor 9.9999 => 9


