#method overriding.
# Parent class
class Payment:
    def pay(self):
        print("Making a payment")

# Child class GooglePay
class GooglePay(Payment):
    def pay(self):
        print("Payment done using Google Pay")

# Child class PhonePe
class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe")

# Child class CreditCard
class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card")

# Creating objects 
p1 = Payment()
p2 = GooglePay()
p3 = PhonePe()
p4 = CreditCard()

p1.pay()
p2.pay()
p3.pay()
p4.pay()
