## Scope of methods
# Task 1 (Service charge)


class BankAccount:
    def __init__(self, name, number: str, balance: float):
        self.name = name
        self.number = number
        self._balance = balance

    def deposit(self, amount: float):
        k = self._balance + amount
        service = self._service_charge(k)
        self._balance = self._balance + amount - service

    def withdraw(self, amount: float):
        k = self._balance - amount
        service = self._service_charge(k)
        self._balance = self._balance - amount - service

    @property
    def balance(self):
        return self._balance

    def _service_charge(self, amount):
        return amount * 0.01


account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)
account.deposit(100)
print(account.balance)
