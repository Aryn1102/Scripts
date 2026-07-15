inventory={}

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Search Item")
        print("5. Update Item")
        print("6. Delete Item")
        print("7. Statistics")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            reduce_item()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            search_item()
        elif choice == '5':
            update_item()
        elif choice == '6':
            del_item()
        elif choice == '7':
            statistics()
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_item():
    product_id = input("Enter product ID: ")
    if product_id in inventory:
        print(f"Item with ID {product_id} already exists in inventory.")
        return
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    inventory[product_id] = {"name": name, "price": price, "quantity": quantity}

def reduce_item():
    product_id = input("Enter product ID to reduce: ")
    quantity = int(input("Enter quantity to reduce: "))
    if product_id in inventory:
        if inventory[product_id]["quantity"] >= quantity:
            inventory[product_id]["quantity"] -= quantity
            if inventory[product_id]["quantity"] == 0:
                del inventory[product_id]
            print(f"Item with ID {product_id} updated in inventory.")
        else:
            print(f"Insufficient quantity for item with ID {product_id}.")
    else:
        print(f"Item with ID {product_id} not found in inventory.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for product_id, item in inventory.items():
            print(f"ID: {product_id}, Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}")

def search_item():
    product_id = input("Enter product ID or name to search: ")
    found = False
    for id, item in inventory.items():
        if id == product_id or item['name'] == product_id:
            print(f"Item found - ID: {id}, Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}")
            found = True
            break
    if not found:
        print(f"Item with ID or name {product_id} not found in inventory.")

def update_item():
    product_id = input("Enter product ID to update: ")
    if product_id in inventory:
        update_choice = input("What would you like to update? ").lower()
        if update_choice == "name":
            name = input("Enter new item name: ")
            inventory[product_id]["name"] = name
        elif update_choice == "price":
            price = float(input("Enter new item price: "))
            inventory[product_id]["price"] = price
        elif update_choice == "quantity":
            quantity = int(input("Enter new item quantity: "))
            inventory[product_id]["quantity"] = quantity
        print(f"Item with ID {product_id} updated in inventory.")
    else:
        print(f"Item with ID {product_id} not found in inventory.")

def del_item():
    product_id = input("Enter product ID to delete: ")
    if product_id in inventory:
        if inventory[product_id]["quantity"] > 0:
            print(f"Cannot delete item with ID {product_id} as the  product is out of stock.")
            return
        del inventory[product_id]
        print(f"Item with ID {product_id} deleted from inventory.")
    else:
        print(f"Item with ID {product_id} not found in inventory.")

def statistics():
    total_items = sum(item['quantity'] for item in inventory.values())
    unique_items = len(inventory)
    total_value = sum(item['price'] * item['quantity'] for item in inventory.values())
    print(f"Total items in inventory: {total_items}")
    print(f"Unique items in inventory: {unique_items}")
    print(f"Total value of inventory: ${total_value:.2f}")