import os #operating system

def read_file(filename):
    products = [] #放在最外面(產生空清單)，不管有沒有找到檔案都要做這行。 #讓使用者輸入那邊會需要用到
    with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if 'PRODUCTS,PRICE' in line:
                    continue #繼續(跳過此迴)
                name, price = line.strip().split(',')
                products.append([name, price])
    return products

# 讓使用者輸入
def user_input(products):
    while True:
        name = input('Please type in the product name:')
        if name == 'q':
            break
        price = input('Please type in the product price:')
        products.append([name, price])
    print(products)
    return products

#印出所有商品
def print_products(products):
    for p in products:
        print(p[0], "'s price is", p[1])

#寫入檔案
def write_file(filename, products):
    with open (filename, 'w', encoding='utf-8') as f:
        f.write('PRODUCTS,PRICE\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

#開始執行程式，通常統稱為main function，為程式的進入點!
def main():
    filename = 'products.csv'
    if os.path.isfile(filename): #檢查檔案在不在
        print('I found the file')
        products = read_file(filename)
    else:
        print('I cannot find the file')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)


main() #如果這一行變成註解，整份程式就甚麼都不會做!