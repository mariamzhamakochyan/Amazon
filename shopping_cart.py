from user import User
from product import Products

class ShoppingCart:
    def __init__(self, name):
        self.name = name
        self.shopcart = {}

    def add(self, name, count):
        if User.self.role == "S":
            if self.name in Products.self.products:
                self.shopcart.update(self.name = self.self.count)                
            else:
                print("There is no such product.")
        else:
            print("You have no shopping cart cuz you are not a buyer.")    

    def remove(self, name, count):
        if User.self.role == "S":
            if self.name in self.shopcart:
                del self.shopcart[self.name]
            else:
                print("No such product")
        else:
            print("You have no shopping cart cuz you are not a buyer.")

    def show(self):
        print(self.shopcart)
        
       
        
    
