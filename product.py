class product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    
    def show(self):
        print(f'    Product name: {self.name}')
        print(f'    Price: {self.price}$')
        print(f'    Description: {self.description}')
        
d = product("Aho", 1322, "book" )
d.show()
        



        


        