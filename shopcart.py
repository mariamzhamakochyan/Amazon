import product
class ShoppingCart:
    def __init__(self):
        self.name = name
        self.shopcart = {}

    def add(self, name, count):
        self.name = input("Enter product name: ")
        self.count = int(input("Enter how many of those products you want:"))
        if self.name in product:
            self.shopcart.update(self.name:self.count)

    def remove(self, name, count):
        self.name = input("Enter product name you want to remove: ")
        self.count = int(input("Enter how many of those products you want to remove:"))
        if self.name in self.shopcart:
            if self.count <= self.shopcart[self.name]:
                del self.shopcart[self.name]
            else:
                print("Wrong quantity:")
        else:
            print("No product with that name:")
        
    


