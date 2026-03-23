// 1. Setup the Store
const walletBalance = 5000;
let cartItems = [500, 1200, 350];
console.log("Initial Cart:", cartItems);

// 2. Manage the Cart
cartItems.push(2000);
cartItems.pop();        
console.log("Updated Cart:", cartItems);

let recommendedItems = [100, 200];
console.log("Recommended Items:", recommendedItems);
let finalCart = [...cartItems, ...recommendedItems];
console.log("Final Cart:", finalCart);

// 3. Calculate Totals
let totalPrice = finalCart[0] + finalCart[1] + finalCart[2] + finalCart[3] + finalCart[4];
totalPrice = totalPrice + (totalPrice * 0.10);
totalPrice = Number(totalPrice.toFixed(2));
console.log("Total Price (with tax):", totalPrice);

// 4. Coupon Code Handling
let couponCode = "   DisCOunT10   ";
couponCode = couponCode.trim().toUpperCase();
if (couponCode === "DISCOUNT10") {
  totalPrice = totalPrice - 500;
  console.log("Coupon applied! New Total:", totalPrice);
}

// 5. Final Decision
if (totalPrice <= walletBalance) {
  let remaining = walletBalance - totalPrice;
  console.log("Purchase Successful! New Balance: " + remaining);
} else {
  let missing = totalPrice - walletBalance;
  console.log("Insufficient Funds! You need " + missing + " more.");
}

// 6. Receipt Generation
let orderId = Math.floor(Math.random() * 100) + 1;
console.log(`Order ${orderId} confirmed. Thank you for shopping!`);