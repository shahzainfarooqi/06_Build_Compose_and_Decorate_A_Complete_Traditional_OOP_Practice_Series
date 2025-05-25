class Product:
    def __init__(self, price):
        self._price = price  

    @property
    def price(self):
        """Getter for price"""
        return self._price

    @price.setter
    def price(self, value):
        """Setter for price"""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter for price"""
        print("Deleting price...")
        del self._price


p = Product(150)
print(p.price)     
p.price = 250      
print(p.price)     
del p.price       
