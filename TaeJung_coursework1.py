
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
