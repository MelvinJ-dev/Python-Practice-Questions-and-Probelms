class atm_machine:
    def __init__(self, name=None, amount=None, balance=None):
        if name is None or amount is None or balance is None:
            print("Welcome! This class needs 3 arguments and has 3 functions:")
            print("   Required arguments → name, amount, balance")
            print("   Functions → display_balance(), deposit_amount(), withdrawal()")
            print("Example: atm_machine('Melvin', 3000, 20000)")
            return

        self.name = name
        self.amount = amount
        self.balance = balance

    def display_balance(self):
        return f'Current balance: {self.balance}'

    def deposit_amount(self, amount):
        self.balance += amount
        return f'Amount of Rupees {amount} deposited. New balance: {self.balance}'

    def withdrawal(self, amount):
        if amount > self.balance:
            return f'Insufficient funds! Current balance: {self.balance}'
        self.balance -= amount
        return f'Amount {amount} has been withdrawn. New balance: {self.balance}'


melvin = atm_machine()