/* Recommended Task: "The E-Commerce Inventory Manager" 
Objective: Build a system to manage products in a store using functions to automate tasks and objects to store complex data.
 Instructions for Students: Setup the Inventory (Array of Objects): Create an empty array called inventory.
  Create a function called createProduct(name, price, quantity). 
  This function should return an object with those three properties. 
  Call this function three times to create these items and add them to your inventory array:
   "Laptop", 1200, 10 "Mouse", 25, 50 "Keyboard", 100, 20 Updating Data (Accessing Constraints): Oh no! The "Mouse" price was wrong.
    Access the second item in your inventory array and update its price to 30. Access the "Laptop" (first item) and add a new property category with the value "Electronics". 
    Merging Product Details (Spread Operator): Create an object called extraDetails with { warranty: "2 years", color: "Silver" }. 
    Create a new variable updatedLaptop by merging the first item in your inventory with extraDetails using the spread operator (...).
     Console log updatedLaptop to see the combined result. The Sale Function (Arrow Functions): Write an Arrow Function called calculateTotalValue.
      It should accept two parameters: price and quantity. It should return the total value (price * quantity).
       Use this function to calculate the total value of the "Keyboard" stock (from your inventory) and log it.
        Nested Data Challenge: Create a user object called adminUser with: name: "Manager" permissions: A nested object
         { canEdit: true, canDelete: false } Write an if statement: If adminUser.permissions.canEdit is true, console log "Access Granted: Inventory updated." Why this works: Functions: They practice passing arguments (name, price) effectively. 
          Objects: They learn to store grouped data instead of just single variables. Spread: Real-world use case (adding extra specs to a product). Nested Access: Reviewing how to dig into data (user.permissions.canEdit).*/

// Setup the Inventory (Array of Objects)
let inventory = [];

function createProduct(name, price, quantity) {
    return {
        name: name,
        price: price,
        quantity: quantity
    };
}       
// Create products and add to inventory
inventory.push(createProduct("Laptop", 1200, 10));
inventory.push(createProduct("Mouse", 25, 50));
inventory.push(createProduct("Keyboard", 100, 20));

// Updating Data (Accessing Constraints)
inventory[1].price = 30; // Update Mouse price
inventory[0].category = "Electronics"; // Add category to Laptop

// Merging Product Details (Spread Operator)
const extraDetails = { warranty: "2 years", color: "Silver" };
const updatedLaptop = { ...inventory[0], ...extraDetails };
console.log(updatedLaptop);

// The Sale Function (Arrow Functions)
const calculateTotalValue = (price, quantity) => price * quantity;
const keyboardStockValue = calculateTotalValue(inventory[2].price, inventory[2].quantity);
console.log(`Total value of Keyboard stock: $${keyboardStockValue}`);

// Nested Data Challenge
const adminUser = {
    name: "Manager",
    permissions: {
        canEdit: true,
        canDelete: false
    }
};

if (adminUser.permissions.canEdit) {
    console.log("Access Granted: Inventory updated.");
}
