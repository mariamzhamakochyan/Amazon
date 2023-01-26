from user import User
from shopping_cart import ShoppingCart
from product import Products

print("     ...Welcom to Amazon...")

role = input("Are you a Seller or a Buyer? (Wriete 'S' or 'B'): ")
username = input("Please enter your name: ")
mail = input("Please enter your mail: ")
us = User(role, username, mail)
us.add(role,username,mail)

if role == "S":
    choice = input("Do you want to add or remove a product? (Enter A or R)")
    if choice == "A":
        name = input("Enter product name: ")
        price = input("Enter price: ")
        features = input("Enter features: ")
        description = input("Enter Description: ")
        pr = Products(name, price, features, description)
        pr.add(name)
        pr.detail(name, price, features, description)
    else:
        name = input("Enter product name you want to remove: ")
        pr.remove(name)
else:
    print("cur no")
