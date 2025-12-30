#1. Basic Setup 
#1-1) inventory start as a {}
inventory = {}

#3-1) category list/ product ids in use
categories = ["Electronics", "Home", "Office"]
product_ids = set()

#1-2) Sample item data (quantity/name/price + brand/category 추가!)
sample_item_1 = {
    "name": "Laptop",
    "brand": ("Dell",),  #3 add brand tuple 
    "category": "Electronics",
    "quantity": 5,
    "price": 799.99
}

sample_item_2 = {
    "name": "Chair",
    "brand": ("IKEA",),  #3-2
    "category": "Home",
    "quantity": 10,
    "price": 49.50
}

#1-3) Sample item in inventory / Add Id
inventory[101] = sample_item_1
product_ids.add(101)
inventory[102] = sample_item_2
product_ids.add(102)

print("Initial inventory:", inventory)
print("Used IDs:", product_ids)

#2. User Input and Data Processing (중복 제거!)

print("\n=== Add New Item ===")
name = input("Enter product name: ")

#3-2) category list 사용
print("Select category:")
for idx, cat in enumerate(categories, start=1):
    print(f"{idx}. {cat}")

category_choice = int(input("Enter category number: "))

# -1 list index starts from 0, user chooose from 1 
category = categories[category_choice - 1]

brand_name = input("Enter brand name: ")
brand = (brand_name,) 

quantity_str = input("Enter quantity: ")
price_str = input("Enter price: ")

quantity = int(quantity_str)  
price = float(price_str)     

# add id +1 use set(x reapeat)
new_id = max(product_ids) + 1 if product_ids else 101
product_ids.add(new_id)

new_item = {
    "name": name,
    "brand": brand,
    "category": category,
    "quantity": quantity,
    "price": price
}

inventory[new_id] = new_item

print("\nItem added successfully!\n")
print("Current Inventory:")
print("----------------------------")
for item_id, item in inventory.items():
    print(f"ID: {item_id} | Name: {item['name']} | Brand: {item['brand'][0]} | Category: {item['category']}")
    print(f"Price: ${item['price']:.2f} | Quantity: {item['quantity']}")
    print()
