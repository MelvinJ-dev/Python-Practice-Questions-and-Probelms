# Sample of a atm machine and pratice of class and objects

class atm_machine:
            
        def display_balance(self):
            print(f'Balance : {self.balance}')
        def deposit_amount(self,amount):
            self.balance+=amount
            print(f'Amount of Rupees {self.balance} is deposited')
            print(f'Balance : {self.balance}')
        def withdrawal(self,amount):
            self.balance-=amount
            print(f'Amount {self.amount} has been withdraw')
            print(f'Balance : {self.balance}')
        def run(self):
            while True:

                option = input("The Program has 3 funtions\n1.dipaly_balance\n2.deposit_amount\n3.withdrawal\n4.Exit\n")
                if option=='1':
                    self.display_balance()
                elif option=='2':
                    amount = int(input("Enter the amount to deposit : "))
                    self.deposit_amount(amount)
                elif option=='3':
                    amount = int(input("Enter the amount to withdraw : "))
                    self.withdrawal(amount)
                else:
                    break
        def __init__(self,name=None,amount=None):
                    if name is None or amount is None:
                        print("The following arguments are required to run the program")
                        print("Name = Melvin","Amount = 3000")
                        print("eg : Melvin,3000")
                    
                    self.name = name
                    self.amount = amount
                    self.balance = 20000
                    self.run()

melvin = atm_machine("melvin",3000)
