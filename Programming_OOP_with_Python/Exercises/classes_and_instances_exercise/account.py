class Account:
    def __init__(self, id_, name,*balance):
        self.id = id_
        self.name = name
        self.balance = 0
        if balance:
            self.balance += balance[0]

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"



