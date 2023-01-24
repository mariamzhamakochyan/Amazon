from user import User
from shopping_cart import ShoppingCart
from product import Products

print("     ...Welcom to Amazon...")
role = input("Are you a Seller or a Buyer? (Wriete 'S' or 'B'): ")
username = input("Please entern your name: ")
mail = input("Plese entern your mail: ")
us = User(role, username, mail)
us.add(role,username,mail)
pr = Products()
