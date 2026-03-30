//Create a JavaScript program that simulates a simple shopping cart checkout process.

const walletBalance=5000
console.log(walletBalance)
let cartItems=[500,1200,350]
cartItems.push(2000)//added
cartItems.pop()//deleted
let recommendedItems=[100,200]
const finalCart=[...cartItems,...recommendedItems]//deconstructed and again formed a new list
console.log(finalCart)
let totalPrice=finalCart[0]+finalCart[1]+finalCart[2]+finalCart[3]+finalCart[4]//did addition using indexing
console.log(totalPrice)//before discount
totalPrice-=(totalPrice*(10/100))
console.log(totalPrice)//total price after 10% discount
console.log(totalPrice.toFixed(2))

let cuponCode="                        disCOunt10    "
cuponCode=cuponCode.trim().toUpperCase()
console.log(cuponCode)

const user_cuponCode="DISCOUNT10"
if (cuponCode==user_cuponCode){
    totalPrice-=500
}
console.log(totalPrice)

if (totalPrice<=walletBalance){

    let remBalance=walletBalance-totalPrice
    console.log(`Purchase Sucessful!!!! Remaning Balance:${remBalance}`)
}
else{
    let needBalance=walletBalance-totalPrice
    needBalance=Math.abs(needBalance)
    console.log(`Insufficient Balance!!! You need ${needBalance} more`)
}


let orderId=(Math.random()*100)+1
orderId=Math.floor(orderId)
console.log(`OrderID ${orderId} confrimed. Thankyou for shopping!!`)