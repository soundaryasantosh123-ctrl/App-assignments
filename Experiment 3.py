class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")


class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Bitcoin.")


class PaymentProcessor:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def set_payment_method(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def make_payment(self, amount):
        self.payment_strategy.pay(amount)


print("===== Payment Processing System =====")

processor = PaymentProcessor(CreditCardPayment())

while True:
    print("\nSelect Payment Method:")
    print("1. Credit Card")
    print("2. PayPal")
    print("3. Bitcoin")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Thank you for using the Payment System!")
        break

    amount = float(input("Enter payment amount: ₹"))

    if choice == "1":
        processor.set_payment_method(CreditCardPayment())

    elif choice == "2":
        processor.set_payment_method(PayPalPayment())

    elif choice == "3":
        processor.set_payment_method(BitcoinPayment())

    else:
        print("Invalid choice!")
        continue

    processor.make_payment(amount)
