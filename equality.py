class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # Compare mobiles  b and m
    def __eq__(self, other):
        if isinstance(other, Mobile):
            return self.brand == other.brand and self.model == other.model
        return False

# creating objects
mobile1 = Mobile("Samsung", "S23", 75000)
mobile2 = Mobile("Samsung", "S23", 72000)
mobile3 = Mobile("Apple", "iPhone 14", 180000)

# Comparee objects
print(mobile1 == mobile2)  # True same b and m
print(mobile1 == mobile3)  # False different b and m
print(mobile2 == mobile3)  # False
