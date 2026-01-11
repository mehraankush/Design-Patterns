from abc import ABC, abstractmethod


class PaymentBehavior(ABC):
    """
    This is the interface that all concrete payment types must implement.
    """
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Behaviors (The algorithms family) statergies
class CreditCardPayment(PaymentBehavior):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card."
    

class PayPalPayment(PaymentBehavior):
    def pay(self, amount):
        return f"Paid {amount} using PayPal."

class BitcoinPayment(PaymentBehavior):
    def pay(self, amount):
        return f"Paid {amount} using Bitcoin."


# The Context (Favor composition)
class PaymentService:
    def __init__(self):
        self.payment_behavior:PaymentBehavior = None
    
    def set_payment_behavior(self,pb:PaymentBehavior):
        self.payment_behavior = pb

    def process_payment(self, amount):
        """
            Delegate to the behavior class.
            Equivalent to 'performFly()' or 'performQuack()'.
        """
        if self.payment_behavior:
            self.payment_behavior.pay(amount)
        else:
            print("No payment method selected!")
    
    

if __name__ == "__main__":
    # 1. Create the context
    my_service = PaymentService()

    # 2. Set behavior dynamically (Composition)
    print("Customer selects Credit Card:")
    my_service.set_payment_behavior(CreditCardPayment())
    my_service.process_payment(100.00)

    # 3. Change behavior at runtime (The power of Strategy)
    print("Customer changes mind to PayPal:")
    my_service.set_payment_behavior(PayPalPayment())
    my_service.process_payment(100.00)
