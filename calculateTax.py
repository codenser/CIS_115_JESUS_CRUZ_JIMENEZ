#this program will calculate the tax and total of an item base on the price and rate of tax
itemPrice = 75.34
taxRate = 7.25 / 100

tax = itemPrice * taxRate
total = itemPrice + tax

print(f'Item price: {itemPrice}')
print(f'Tax rate: {taxRate}%')
print(f'The price with tax is: {total}')