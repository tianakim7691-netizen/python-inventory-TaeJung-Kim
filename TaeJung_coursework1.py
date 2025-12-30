#1. Basic Setup 
#1-1) inventory start as a {}
inventory = {}

#3-1) category list/ product ids in use
categories = ["Electronics", "Home", "Office"]
product_ids = set()

#6. Object-Oriented Programming 
class Product:
    #basic 
    def __init__(self, name, brand, category, quantity, price): #init=initialize
        self.name = name
        self.brand = brand
        self.category = category
        self.quantity = quantity
        self.price = price
    
    def display(self, item_id):  # +item_id 
        #pd info
        print(f"ID: {item_id} | Name: {self.name} | Brand: {self.brand[0]} | Category: {self.category}")
        print(f"Price: ${self.price:.2f} | Quantity: {self.quantity}")
        print()
    
    def update_quantity(self, new_quantity):
        #update quantity
        self.quantity = new_quantity

class PerishableProduct(Product):
    #deadline pd
    def __init__(self, name, brand, category, quantity, price, expiration_date):
        super().__init__(name, brand, category, quantity, price)  # call parents class
        self.expiration_date = expiration_date
    
    def display(self, item_id):  # +item_id 
        #parents class method overwrite
        super().display(item_id)  # call parents display
        print(f"Expires: {self.expiration_date}")

# sample 
sample_item_1 = Product("Laptop", ("Dell",), "Electronics", 5, 799.99)
sample_item_2 = PerishableProduct("Milk", ("Organic",), "Home", 10, 3.99, "2025-12-31")
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
    
    #6 create new pd
    new_product = Product(name, brand, category, quantity, price)
    
    new_id = max(product_ids) + 1 if product_ids else 101
    product_ids.add(new_id)
    inventory[new_id] = new_product
    print("Item added successfully!\n")

def view_inventory():
    print("\nCurrent Inventory:")
    print("----------------------------")
    if not inventory:
        print("Inventory is empty!")
    else:
        for item_id, item in inventory.items():
            item.display(item_id) 

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

#4. Conditional Statements & Loops 
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
