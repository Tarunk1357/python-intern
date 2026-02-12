class ShoppingCart:
    def __init__(self, items):
        self.items = items 

    # access item using cart[index]
    def __getitem__(self, index):
        return self.items[index]

    # update item using cart[index] = value
    def __setitem__(self, index, value):
        self.items[index] = value

# Creating object 
cart = ShoppingCart(["Apple", "Banana", "Milk"])
print(cart[0])   
cart[1] = "Orange"   
print(cart.items)
