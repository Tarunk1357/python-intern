#multilevel inheritance
# Parent Class
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)


# Child Class
class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand, warranty):
        super().__init__(product_name, price)
        self.brand = brand
        self.warranty = warranty

    def display_electronic_product(self):
        self.display_product()
        print("Brand:", self.brand)
        print("Warranty:", self.warranty, "years")


# Grandchild Classu
class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        super().__init__(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        self.display_electronic_product()
        print("RAM:", self.ram, "GB")
        print("Storage:", self.storage, "GB")

mobile = MobilePhone(
    product_name="Smartphone",
    price=25000,
    brand="Samsung",
    warranty=2,
    ram=8,
    storage=128
)

mobile.display_mobile_details()
