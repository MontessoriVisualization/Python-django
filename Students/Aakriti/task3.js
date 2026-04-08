// Create a system that processes student data, calculates grades, filters results, and generates reports. It should handle real-world logic like grade calculations, filtering by criteria, and data transformations.

// What to Build:
// An array of student objects, where each student has: name, marks (array of subject scores), attendance percentage
// Functions that:
// Calculate average marks and assign grades (A/B/C/D based on ranges)
// Filter students by criteria (e.g., "show only students with > 75 average")
// Find top performer and lowest scorer
// Check eligibility (average > 40 AND attendance > 75%)
// Loops to iterate through data and transform it
// Conditionals to apply grading rules (use switch for grade assignment or if/else for eligibility)
// Generate a summary report showing: total students, pass count, fail count, average class score
// How to Approach It:
// Start with data structure — Create realistic student objects with nested arrays (marks per subject)
// Build utility functions — Each function should do ONE thing (calculate average, assign grade, filter students)
// Use loops strategically — .map() mindset (though not required): transform data from one form to another
// Apply game logic — Use conditionals creatively (e.g., bonus points if attendance > 90%)
// Combine everything — Chain functions and loops to build the final report
// Challenge Twist (Optional):
// Add a pass/fail rule: If marks < 40, fail regardless of attendance
// Add a merit scholarship checker: Show students eligible for scholarship (average > 80 AND attendance 100)
// Export data to a formatted string report using template literals
// This project forces them to design with objects, organize logic with functions, and process data with loops — all core pillars.

let students=[
    {name:"Aakriti",marks:[90,60,70,30],attendance:69},
    {name:"Monika",marks:[20,40,20,47],attendance:29},
    {name:"Hangma",marks:[20,60,90,47],attendance:89},
    {name:"Hari",marks:[80,69,97,90],attendance:30},
    {name:"Gita",marks:[80,39,17,90],attendance:70},
    {name:"Subash",marks:[80,99,97,90],attendance:100},
    {name:"Sita",marks:[20,60,20,47],attendance:85},
    {name:"Shree",marks:[90,70,90,89],attendance:25}

]
console.log(students)

function calcAvg(stu){

    let totalMarks=0;
    for(j=0; j<stu.marks.length;j++){
        totalMarks+=stu.marks[j]
    }
    return totalMarks/stu.marks.length;
}

let avgmarks=[];
for(let i=0; i<students.length;i++){
    avgmarks.push(calcAvg(students[i]))
}
console.log("The average marks of each student",avgmarks)

let grade=[];
for(let i=0; i<avgmarks.length;i++){
    
    if (avgmarks[i]>=80 && avgmarks[i]<=100){
        grade.push("A")
    }
    else if(avgmarks[i]<=80 && avgmarks[i]>=60){
        grade.push("B")
    }
    else if(avgmarks[i]<=60 && avgmarks[i]>=40){
        grade.push("C")
    }
    else{
        grade.push("F")
    }
}
console.log("The grade of each student",grade)



//updating students profile
for(let i=0; i<students.length;i++){
    students[i].Average_Marks=avgmarks[i]
    students[i].Grade=grade[i]
    
}
console.log("Updated Students Profile with grade and avgmarks:",students)

//students with > 75 average
for (let i=0; i<students.length;i++){
    if(students[i].Average_Marks>75){
        console.log(students[i].name)//with meassage
    }
}
//top performer
let topPerformer=avgmarks[0]
for (let i=0; i<avgmarks.length;i++){
    if(avgmarks[i]>topPerformer){
        topPerformer=avgmarks[i]
        
    }

}
// console.log(`${students[i].name} is a top performer with average marks: ${students[i].Average_Marks}`)
console.log(`The top performer is :  ${topPerformer}`)

//low scorer
let lowScorer=avgmarks[0]
for(let i=0; i<avgmarks.length;i++){
    if(avgmarks[i]<lowScorer){
        lowScorer=avgmarks[i]
    }
}
console.log(`The loe Scorer is :  ${lowScorer}`)

// Check eligibility (average > 40 AND attendance > 75%)
let eligibility=[]
for(let i=0; i<avgmarks.length;i++){
    if(students[i].Average_Marks>40 && students[i].attendance >75){
        eligibility.push("PASS")
    }
    else{
        eligibility.push("FAIL")
    }
}
console.log("The pass/fail eligibilty of each student; ",eligibility)

//again updating with results
for(let i=0; i<students.length;i++){
    students[i].Result=eligibility[i]
    
}
console.log("Updated Students Profile with grade and avgmarks:",students)


//pass count
let pcount=0;
for(let i=0;i<eligibility.length;i++){

    if(eligibility[i]==="PASS"){
        pcount+=1
    }
}
console.log("The pass count in letslearn is: ",pcount)

//fail count
let fcount=0;
for(let i=0;i<eligibility.length;i++){

    if(eligibility[i]==="PASS"){
        continue;
    }
    else{
        fcount+=1
    }
}
console.log("The fail count in letslearn is: ",fcount)
//average class score
function classScore(){
let avgClassScore=0;
for(let i=0; i<avgmarks.length;i++){
    avgClassScore+=avgmarks[i]
}
 return avgClassScore/students.length
}

console.log("The average score of class is : ",classScore(avgmarks))

// summary report showing: total students, pass count, fail count, average class score
console.log("==============CLASS REPORT OF LETSLEARN=============")
console.log(`\nThe total students in Letslearn is : ${students.length}\nPass count of lets learn : ${pcount} \nFail count of letslearn : ${fcount}\nAverage class score of letslearn is : ${classScore(avgmarks)}`)
console.log("====================================================")

// Add a merit scholarship checker: Show students eligible for scholarship (average > 80 AND attendance 100)
// function merit(){
//     for(let i=0; i<students.length;i++){
//         if(students[i].attendance===100 && students[i].avgmarks>80){
            
//         }
//         return students[i].name
//     }
// }
// console.log(merit())