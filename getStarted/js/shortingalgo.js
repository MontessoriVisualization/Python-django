/* Create a system that processes student data, calculates grades, filters results, and generates reports. It should handle real-world logic like grade calculations, filtering by criteria, and data transformations.

What to Build:
An array of student objects, where each student has: name, marks (array of subject scores), attendance percentage
Functions that:
Calculate average marks and assign grades (A/B/C/D based on ranges)
Filter students by criteria (e.g., "show only students with > 75 average")
Find top performer and lowest scorer
Check eligibility (average > 40 AND attendance > 75%)
Loops to iterate through data and transform it
Conditionals to apply grading rules (use switch for grade assignment or if/else for eligibility)
Generate a summary report showing: total students, pass count, fail count, average class score
How to Approach It:
Start with data structure — Create realistic student objects with nested arrays (marks per subject)
Build utility functions — Each function should do ONE thing (calculate average, assign grade, filter students)
Use loops strategically — .map() mindset (though not required): transform data from one form to another
Apply game logic — Use conditionals creatively (e.g., bonus points if attendance > 90%)
Combine everything — Chain functions and loops to build the final report
Challenge Twist (Optional):
Add a pass/fail rule: If marks < 40, fail regardless of attendance
Add a merit scholarship checker: Show students eligible for scholarship (average > 80 AND attendance 100)
Export data to a formatted string report using template literals
This project forces them to design with objects, organize logic with functions, and process data with loops — all core pillars.
 */
// Sample student data
const students = [
    { name: "Ram", marks: [85, 90, 78], attendance: 92 },  
    { name: "Shyam", marks: [70, 75, 80], attendance: 85 },
    { name: "Hari", marks: [60, 65, 58], attendance: 80 },
    { name: "Gita", marks: [30, 35, 28], attendance: 70 },
    { name: "Sita", marks: [95, 98, 92], attendance: 100 }
];

function avg(student){
     let totalMark=0
     for (let index = 0; index < student.marks.length; index++) {
        totalMark+=student.marks[index]        
     }
     return totalMark / student.marks.length;
}

const avgmarks =[]
for(let i=0;i<students.length;i++){
    avgmarks.push(avg(students[i]))

}
console.log(avgmarks)
// let highestMark = avgmarks[0]
// for(let i=0;i<avgmarks.length;i++){
//     if(avgmarks[i]>highestMark){
//         highestMark = avgmarks[i]
//     }
// }
// console.log("Highest Mark:", highestMark)
//     let lowestMark = avgmarks[0]

// for(let i=0;i<avgmarks.length;i++){
//     if(avgmarks[i]<lowestMark){
//         lowestMark = avgmarks[i]
//     }
// }
// console.log("Lowest Mark:", lowestMark)

//  const accArray=[]
// for (let index = 0; index < avgmarks.length; index++) {
//     let highestMark = avgmarks[0]
//     for(let j=0;j<avgmarks.length;j++){
//     if(avgmarks[j]>highestMark){
//         highestMark = avgmarks[j]
//     }

// }

//     accArray.push(highestMark)
//     const index = avgmarks.indexOf(highestMark)
//     avgmarks[index] = -1
// console.log(avgmarks)


    
// }
// console.log("Sorted Marks:", accArray)


