// Smart checkout system 
const walletBalance = 500;
let cartItems = [500, 1200, 350];
cartItems.push(2000);
cartItems.pop();
let recommendedItems = [100,200];
let finalCart= [...cartItems , ...recommendedItems];
let totalPrice = finalCart[0]+ finalCart[1]+finalCart[2]+finalCart[3]+ finalCart[4];
totalPrice=totalPrice-(totalPrice* 0.10);
totalprice = totalPrice.toFixed(2);

let couponCode = "   DisCOunT10   ";
couponCode = couponCode.trim().toUpperCase();

if (couponCode === "DISCOUNT10") {
  totalPrice = totalPrice - 500;
}

if (totalPrice <= walletBalance) {
  let remaining = walletBalance - totalPrice;
  console.log(`Purchase Successful! New Balance: ${remaining}`);
} else {
  let missing = totalPrice - walletBalance;
  console.log(`Insufficient Funds! You need ${missing} more.`);
}

let orderId = Math.floor(Math.random() * 100) + 1;

console.log(`Order ${orderId} confirmed.Thank you for shopping!`);