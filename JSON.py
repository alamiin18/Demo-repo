import json

with open('store.json', 'r') as store:
    stores = json.load(store)

search = input('search for product: ').strip()
for x in stores['products']:
    if  search in x.lower()  and len(search) >= 3:
        print(search, 'found')
        break
else:
    print('Not found')



with open('product.json', 'r') as file:
    products = json.load(file)
    print(products)


available = '''
{
    "store": {
        "products": ["Kube cap", "Veil", "Shadda", "Goggles"]
    }
}
'''
stores = json.loads(available)
print(f'Available products: {len(stores['store']['products'])}')


emails = '''
{
    "user": {
        "id": "U01",
        "profile": {
            "name": "Sadiq",
            "email": "sadiq@gmail.com"
        }
    }
}
'''
email = json.loads(emails)
print(f'email: {email['user']['profile']['email']}')


data = '''
[
    {
        "product": "Kube cap", 
        "price": 2500
    },
    {
        "product": "Veil", 
        "price": 3000
    },
    {
        "product": "Shadda", 
        "price": 8000
    }
]
'''


items = json.loads(data)
for item in items:
    print(item["product"], "-", item['price'])

print(items[1]['product'])





personal_data = '''

{
        "name": "Amina",
        "Age": 29,
        "City": "Kano"
        
}

'''
personal_info = json.loads(personal_data)
print(personal_info)
print(personal_info["name"], personal_info['City'])


data = '''
[
     {
        "id": "001",
        "name": "Quincy"
     },
    {
        "id": "009",
        "name": "Mrgesh"
    }
]
'''
info = json.loads(data)
print(info[1])
