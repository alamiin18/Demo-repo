

store_inventory = {
    "Ankara": {"price": 5000, "stock": 20, "sizes": ["S", "M", "L"]},
    "Kube cap": {"price": 2000, "stock": 10, "colors": ["Red", "Blue"]},
    "Veil": {"price": 1500, "stock": 15, "materials": ["Silk", "Cotton"]},
    "Shadda": {"price": 3000, "stock": 5, "patterns": ["Plain", "Striped"]}
}
for product, info in store_inventory.items():
    print('product', product, ', price', info['price'], ', stock', info['stock'])


inventory = {
    "Kube cap": 10,
    "Veil": 15,
    "Shadda": 5,
    "Goggles": 8
}
print(inventory.keys())
print(inventory.values())
for product, quantity in inventory.items():
    print('Product:', product,', Quantity:', quantity)


product = input('Product name: ')
for item in inventory:
    if item.lower() == product.lower():
        print( f"{product} quantity:", inventory[item])
        break
else:
    print('Not found')


product = {
    "name": "Ankara",
    "price": 5000,
    "stock": 20
}
print(product.keys())
print(product.values())
print('stock quantity: ', product['stock'])
product['price'] = 5500
print(product)

product["category"] =  "Textile"
product["size"] =  "M"
print(product)
del product['size']
print(product)



counts = dict()
longest = ''

with open('chapter.txt') as f:
    for line in f:
        words = line.split()
        for word in words:
            clean = word.strip()
            counts[clean] = counts.get(clean, 0) + 1
            if len(clean) > len(longest):
                longest = clean
#y = re.findall()
for word, count in counts.items():
    print(word, count)

print('The longest word is:', longest)

print("Done!")
print(len(counts))

big_count = None
big_word = None

for word, count in counts.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count
print('The word that appear most:', big_word, big_count)


jjj = {'chuck': 1, 'book': 23, 'bag': 18, 'jane': 7}
print(jjj.keys())
print(jjj.values())
print(jjj.items())

for aaa, bbb in jjj.items():
    print(aaa, bbb)


count = {'quincy': 1, 'mrugesh': 42, 'beau': 100, '0': 10}
print(count.get('kris', 0))





