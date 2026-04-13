products = {1001: {"name": "Face Wash", "price": 99.99},
            1002: {"name": "Moisturizer", "price": 149.99},
            1003: {"name": "Serum", "price": 199.99},
            1004: {"name": "Sunscreen", "price": 299.99}}

cart = {}

def view_products():
  print("\nPRODUCTS")
  print("=========")
  i = 1
  for id, product in products.items():
    print(f"{i}. ID: {id}")
    for key, value in product.items():
      print(key.capitalize(), ": ", value)
    print()
    i+=1

def view_cart():
  if (cart== {}):
    print("Cart is empty!\n")
  else:
    print("\nPRODUCTS IN CART")
    print("=================")
  i = 1
  for id, product in cart.items():
    print(f"{i}. ID: {id}")
    for key, value in product.items():
      print(f"{key}: {value}")
    print()
    i+=1

def add_to_cart():

  while True:
    try:
      id = int(input(("Enter the ID of the product you want to add to cart: ")))
      break
    except ValueError:
      print("Please enter a valid ID")

  while True:
    try:
      quantity = int(input("Enter the quantity: "))
      if (quantity<=0):
        print("Please enter a number greater than zero")
      else:
        break
    except ValueError:
      print("Please enter a valid number")

  if (id in products.keys()):
    cart[id] = products[id].copy()
    cart[id]["quantity"] = quantity
    print("Item added successfully!\n")
  else:
    print("Item not found")

def remove_from_cart():

  while True:
    try:
      id = int(input("Enter the ID of the product you want to remove from the cart: "))
      break
    except ValueError:
      print("Please enter a valid ID")

  if (id in cart.keys()):
    del cart[id]
    print("Item removed successfully!")
  else:
    print("Item not found in the cart")

def clear_cart():
  if (cart == {}):
    print("Cart is already empty!")
  else:
    cart.clear()
    print("Cart cleared!")

def checkout():
  if (cart=={}):
    print("Cart is empty! Please add something to checkout")
  else:
    total_price = 0
    for product in cart.values():
      print(f"Product: {product["name"]}\t"
            f"Price: {product["price"]}\t"
            f"Quantity: {product["quantity"]}")

      total_price+=(product["price"]*product["quantity"])
    print(f"Total price: {total_price} rupee")

def main():

  print("MENU")
  print("=====")
  print("1. View Products\n"
        "2. View Cart\n"
        "3. Add to Cart\n"
        "4. Remove from Cart\n"
        "5. Clear Cart\n"
        "6. Checkout\n"
        "7. Exit\n")

  while True:
    try:
      ch = int(input("\nEnter your choice: "))

    except ValueError:
      print("Please enter an integer")

    else:
      if (ch==1):
        view_products()
      elif (ch==2):
        view_cart()
      elif (ch==3):
        add_to_cart()
      elif (ch==4):
        remove_from_cart()
      elif (ch==5):
        clear_cart()
      elif (ch==6):
        checkout()
      elif (ch==7):
        print("Exiting...")
        break
      else:
        print("Please enter a valid choice")

main()

