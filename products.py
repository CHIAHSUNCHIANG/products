#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if 'PRODUCTS,PRICE' in line:
            continue #繼續
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)

# 讓使用者輸入
while True:
    name = input('Please type in the product name:')
    if name == 'q':
        break
    price = input('Please type in the product price:')
    products.append([name, price])
print(products)

#印出所有商品
for p in products:
    print(p[0], "'s price is", p[1])

with open ('products.csv', 'w', encoding='utf-8') as f:
    f.write('PRODUCTS,PRICE\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')