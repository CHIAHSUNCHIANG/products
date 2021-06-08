products = []
while True:
    name = input('Please type in the product name:')
    if name == 'q':
        break
    price = input('Please type in the product price:')
    products.append([name, price])
print(products)

for p in products:
    print(p[0], "'s price is", p[1])

with open ('products.csv', 'w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')