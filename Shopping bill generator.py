products = [
    ("SmartPhone", "iPhone-16pro", 70000, "Apple"),
    ("SmartPhone", "S26-Ultra", 120000, "Samsung"),
    ("HeadPhone", "Rockerz411", 2000, "boAt"),
    ("Mouse", "M612-RGB", 1000, "REDRAGON"),
]

# show products
print(f"{'Sr':<5}|{'Category':<14}|{'Name':<16}|{'Price':<10}|{'Brand'}")
print("-"*60)

for i, (category, name, price, brand) in enumerate(products, start=1):
    print(f"{i:<5}|{category:<14}|{name:<16}|₹{price:<10}|{brand}")

cart = {}

# input loop
while True:
    choose = input("Enter Item Sr No. or type 'na': ")

    if choose == "na":
        break

    choose = int(choose)
    qty = int(input("Enter Quantity: "))

    product = products[choose - 1]

    if product[1] in cart:
        cart[product[1]] += qty
    else:
        cart[product[1]] = qty


# bill function
def generate_bill(cart):
    total = 0

    print("\n------ BILL ------")

    for item_name, qty in cart.items():

        for category, name, price, brand in products:
            if name == item_name:

                amount = price * qty
                print(f"{name} x {qty} = ₹{amount}")

                total += amount

    print("------------------")
    print("Total = ₹", total)

 
generate_bill(cart)