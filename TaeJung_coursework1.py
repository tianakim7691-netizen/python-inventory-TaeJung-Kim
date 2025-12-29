
#1. Basic Setup 
#1-1) inventory start as a 0
inventory = {}

#1-2) Sample item data quantity/ name/ price
sample_item_1 = {
    "name": "Laptop",
    "quantity": 5,
    "price": 799.99
}

sample_item_2 = {
    "name": "Chair",
    "quantity": 10,
    "price": 49.50
}

#1-3) Sample item in inventory / Add Id
inventory[101] = sample_item_1
inventory[102] = sample_item_2

# Categories and id set
categories = ["Electronics", "Home", "Office"]
product_ids = {101, 102}

print(inventory)


#2. User Input and Data Processing
inventory = {}
categories = ["Electronics", "Home", "Office"]
product_ids = set()

# Allow the user to add items using input(), storing details in a dictionary

print("=== Add New Item ===")
name = input("Enter product name: ")

# quantity, price ->num
quantity_str = input("Enter quantity: ")
price_str = input("Enter price: ")

quantity = int(quantity_str)  
price = float(price_str)     

# Add id +1 / later change to set
new_id = max(product_ids) + 1 if product_ids else 101
product_ids.add(new_id)

new_item = {
    "name": name,
    "quantity": quantity,
    "price": price
}

inventory[new_id] = new_item

print("\nItem added successfully!\n")
print("Current Inventory:")
print("--------------------") #make pretty 
for item_id, item in inventory.items():
    print(f"ID: {item_id} | Name: {item['name']}")
    print(f"Price: ${item['price']:.2f} | Quantity: {item['quantity']}")
    print()
