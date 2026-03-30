const array = [1, "two", true, 4, 5];
            //    0,   1   , 2   , 3, 4
const newArray = new Array(1, "two", true, 4, 5);

console.log(array);
console.log(newArray);
console.log(array[4]);

const fruits = ["apple", "banana", ["mango", "grape"], "orange"]; 
console.log(fruits[2][0])

let marbalHeros=["ironman","spiderman","captain america","ant man"]
const DcHeroes =["superman","banman","flash","woder women"]

console.log(marbalHeros.push("black panthor"))
console.log(marbalHeros.pop())
console.log(marbalHeros.push(DcHeroes))

console.log(marbalHeros)

marbalHeros=marbalHeros.concat(DcHeroes)
console.log(marbalHeros)


const allHeroes = [...marbalHeros,...DcHeroes,...array]
console.log(allHeroes)



// [a,b,c,d,[1,2,3,4]]
// [
// a ,b,c, d,
// 1,2,3,4]


// a,b,c,d,1,2,3,4


const nextedarrayval=[1,2,3,4,5,["a","b",["I","II","III" ,"IV"]]];
console.log(nextedarrayval.flat(Infinity))