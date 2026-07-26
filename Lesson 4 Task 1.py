## Scope of methods
# Task 1 (Service charge)


class BankAccount:
    def __init__(self,name,number:str,balance:float):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self,amount:float):
        k = self.balance + amount
        service = self._service_charge(k)
        self.balance = self.balance + amount - service

    def withdraw(self,amount:float):
        k = self.balance - amount
        service = self._service_charge(k)
        self.balance = self.balance - amount - service
        

    def balance(self):
        return self.balance

    def _service_charge(self,amount):
        return amount * 0.01


account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)
account.deposit(100)
print(account.balance)
