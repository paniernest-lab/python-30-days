products = []
prices = []
num_products = int(input("how many prodcuts?"))

for i in range(num_products):
    product = input("product name: ")
    price = float(input("price: "))
    products.append(product)
    prices.append(price)

print("\nyour shopping list:")

total = 0
for i in range (len(products)):
    print(products[i], "-", prices [i])
    total = total + prices[i]

print("total:", round(total, 2))