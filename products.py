products = []
while True:
    name = input('Please type in the product name:')
    if name == 'q':
        break
    price = input('Please type in the product price:')
    products.append([name, price])
print(products)

for p in products:
    print(p)