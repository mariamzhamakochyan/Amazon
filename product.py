from user import User

class Products:
    def __init__(self):
        self.products = []
        self.descriptions = []

    def add(self, name):
        if User.user.role == 1:
            self.products.append(self.name):
        else:
            print("You are currently a buyer, so you cannot add a product.")

    def detail(self, name, price, features, description):
        prods = []
        if User.user.role == 1:
            if self.name in self.product:
                prods.append({self.price})
                prods.append(self.features)
                prods.append(self.description)           
                self.products.append(prods)
            else:
                print("There are no matching products.")
        print("You are currently a buyer, so you cannot add a product.")

    def remove(self, name):
        idx = self.products.index(self.name)
        if User.user.role == 1:
            if self.name in self.product:
                self.product.remove(self.name)
                del self.description[idx]
            else:
                print("You do not have a similar product.")
        else:
            print("You are currently a buyer, so you cannot add a product.")





            

        






        


        