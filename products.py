products = []
while True:
    name = input('Please type in the product name:')
    if name == 'q':
        break
    price = input('Please type in the product price:')
   
    # p = []
    # p.append(name)
    # p.append(price)
    p = [name, price]
   
    products.append(p)
    #products.append([name, price])
print(products)

print(products[0][0])