// Recommended Task: "The E-Commerce Inventory Manager"
// Objective:
// Build a system to manage products in a store using functions to automate tasks and objects to store complex data.


// Create an empty array called inventory.
let inventory=[]

// Create a function called createProduct(name, price, quantity).
// This function should return an object with those three properties.
// Call this function three times to create these items and add them to your inventory array:
// "Laptop", 1200, 10
// "Mouse", 25, 50
// "Keyboard", 100, 20
function createProduct(name, price, quantity){
    let products= {
        "name":name,
        "price":price,
        "quantity":quantity
    };
    return products

}

let p1=createProduct("Laptop",1200,10)
let p2=createProduct("Mouse",25,50)
let p3=createProduct("Keyboard",100,20)

// inventory=[{...p1,...p2,...p3}]//all data was overridden by `p3
inventory=[
    {name:"Laptop",
        price:1200,
        quantity:10
    },
    {name:"Mouse",
        price:25,
        quantity:50
    },
    {name:"Keyboard",
        price:100,
        quantity:20
    }

]
console.log(inventory)
// Updating Data (Accessing Constraints):

// Oh no! The "Mouse" price was wrong. Access the second item in your inventory array and update its price to 30.
// Access the "Laptop" (first item) and add a new property category with the value "Electronics".
inventory[1].price=30
console.log("After increasing mouse price",inventory)

// Access the "Laptop" (first item) and add a new property category with the value "Electronics".
// Merging Product Details (Spread Operator):
inventory[0].category="Electronics"
console.log("After adding the category on p1",inventory)
// Create an object called extraDetails with { warranty: "2 years", color: "Silver" }.
// Create a new variable updatedLaptop by merging the first item in your inventory with extraDetails using the spread operator (...).
// Console log updatedLaptop to see the combined result.

const extraDetails={
    warranty:"2 years",
    color:"Silver"
}

let updatedLaptop=[{...inventory[0],...extraDetails}]
console.log(updatedLaptop)

// The Sale Function (Arrow Functions):

// Write an Arrow Function called calculateTotalValue.
// It should accept two parameters: price and quantity.
// It should return the total value (price * quantity).
// Use this function to calculate the total value of the "Keyboard" stock (from your inventory) and log it.

const calculateTotalValue=(price,quantity)=>{
    return (price*quantity)
}
const totalValOfKeyboard=calculateTotalValue(inventory[2].price,inventory[2].quantity)
console.log("The total value of Keyboard is",totalValOfKeyboard)

// Nested Data Challenge:

// Create a user object called adminUser with:
// name: "Manager"
// permissions: A nested object { canEdit: true, canDelete: false }
// Write an if statement: If adminUser.permissions.canEdit is true, console log "Access Granted: Inventory updated."
// Why this works:
// Functions: They practice passing arguments (name, price) effectively.
// Objects: They learn to store grouped data instead of just single variables.
// Spread: Real-world use case (adding extra specs to a product).
// Nested Access: Reviewing how to dig into data (user.permissions.canEdit).

 const adminUser={
    name:"Manger",
    permissions:{
        canEdit:true,
        canDelete:false
    }
 }

 if (adminUser.permissions.canEdit ===true){
    console.log("Access Granted: Inventory updated!!!!")

 }