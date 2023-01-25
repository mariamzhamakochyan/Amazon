from user import User

class Products:
    def __init__(self, name, price, features, description):
        global role
        self.name = name
        self.price = price
        self.features = features
        self.description = description
        self.products = []
        self.descriptions = []

    def add(self, name):
        if role == "S":
            self.products.append(self.name)
        else:
            print("You are currently a buyer, so you cannot add a product.")

    def detail(self, name, price, features, description):
        prods = []
        if role == "S":
            if self.name in self.products:
                prods.append({self.price})
                prods.append(self.features)
                prods.append(self.description)
                self.products.append(prods)
            else:
                print("There are no matching products.")
        else:
            print("You are currently a buyer, so you cannot add a product.")

    def remove(self, name):
        idx = self.products.index(self.name)
        if role == "S":
            if self.name in self.products:
                self.product.remove(self.name)
                del self.description[idx]
            else:
                print("You do not have a similar product.")
        else:
            print("You are currently a buyer, so you cannot add a product.")