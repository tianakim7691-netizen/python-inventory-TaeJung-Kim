1. Project title + short description
    Simple inventory program. Can add/view/remove items. Learned class and file save too.

2. How to run the program (commands)
    1. terminal에서 python3 TaeJung_coursework1.py run
    2. menu 1-5 choose
        1. Add Item (add new product)
        2. View Inventory (see stock)
        3. Update Item (not done yet)
        4. Remove Item (delete product)
        5. Exit (save file and quit)

3. Features implemented (brief checklist)
    1. Basic Setup - inventory dict + sample data (str/int/float)
    2. User Input - input() name/quantity/price + f-string print
    3. List/Tuple/Set - categories list, brand tuple, product_ids set
    4. Loop/If - while True menu + if/elif
    5. Function - add_item(), view_inventory(), remove_item()
    6. OOP - Product class + PerishableProduct inherit, display method
    7. File - save/load inventory.txt
    8. Bonus - try/except error handle

4. Any limitations / known issues
    1. 3-Update Item not implement yet
    2. PerishableProduct only sample, cannot add in menu
    3. File save no expiration date (only basic Product)
    4. Wrong input (like letter for quantity) crash program
    5. ID start 101 and increase (no duplicate)