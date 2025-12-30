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

#5. Functions
def add_item():
    print("\n=== Add New Item ===")
    name = input("Enter product name: ")
    
    print("Select category:")
    for idx, cat in enumerate(categories, start=1):
        print(f"{idx}. {cat}")
    category_choice = int(input("Enter category number: "))
    category = categories[category_choice - 1]
    
    brand_name = input("Enter brand name: ")
    brand = (brand_name,)
    
    quantity_str = input("Enter quantity: ")
    price_str = input("Enter price: ")
    quantity = int(quantity_str)
    price = float(price_str)
    
    new_id = max(product_ids) + 1 if product_ids else 101
    product_ids.add(new_id)
    
    new_item = {
        "name": name, "brand": brand, "category": category,
        "quantity": quantity, "price": price
    }
    inventory[new_id] = new_item
    print("Item added successfully!\n")

def view_inventory():
    print("\nCurrent Inventory:")
    print("----------------------------")
    if not inventory:
        print("Inventory is empty!")
    else:
        for item_id, item in inventory.items():
            print(f"ID: {item_id} | Name: {item['name']} | Brand: {item['brand'][0]} | Category: {item['category']}")
            print(f"Price: ${item['price']:.2f} | Quantity: {item['quantity']}")
            print()

def remove_item():
    print("\n=== Remove Item ===")
    item_id_str = input("Enter ID to remove: ")
    item_id = int(item_id_str)
    
    if item_id in inventory:
        del inventory[item_id]
        product_ids.discard(item_id)
        print("Item removed successfully!")
    else:
        print("Item not found!")


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

#4. Conditional Statements & Loops
    # select option
    # 1=add 2=current 5=break
    # go back
while True:
    print("\nWelcome to the Inventory Management System!")
    print("===========================================")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")
    print("===========================================")
    
    choice = input("Select an option: ") #selected by user
    #change code to easy way
    
    if choice == "1":
        add_item()

    elif choice == "2":
        view_inventory()

    elif choice == "4":
        remove_item() 

    elif choice == "5":
        print("Saving inventory to file...")
        print("Exiting system. Goodbye!")
        break
    
    else:
        print("Invalid option! Please select 1-5.")
