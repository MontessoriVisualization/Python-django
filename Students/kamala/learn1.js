const learn={
    name: "Sita",
    age: 20,
    cources : ["python","ML","Django"],"present days":['sun','mon','tue']
};
//update cources
learn.cources=["UI/UX",'Development']
//add new property
learn.grade="class2"

const info={
    name:"Ram",
    grade:"class4"
}
console.log({...learn, ...info});

// console.log(learn);