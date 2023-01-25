from user import User
from shopping_cart import ShoppingCart
from product import Products

print("     ...Welcom to Amazon...")

role = input("Are you a Seller or a Buyer? (Wriete 'S' or 'B'): ")
username = input("Please entern your name: ")
mail = input("Please entern your mail: ")
us = User(role, username, mail)
us.add(role,username,mail)

if role == "S":
    choice = input("Do you want to add or remove a product? (Enter A or R)")
    if choice == "A":
        name = input("Entern product name: ")
        price = input("Entern price: ")
        features = input("Entern features: ")
        description = input("Entern Description: ")
        pr = Products(name, price, features, description)
        pr.add(name)
        pr.detail(name, price, features, description)
    else:
        name = input("Entern product name you want to remove: ")
        pr.remove(name)
else:
    print("cur no")