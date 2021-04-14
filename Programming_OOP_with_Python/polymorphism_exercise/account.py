class Account:
    def __init__(self, *args):
        self.owner = args[0]
        self.amount = args[1] if len(args) == 2 else 0
        self._transactions = []

    def __repr__(self):
        return f'{self.__class__.__name__}({self.owner}, {self.amount})'

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other):
        current = Account(f'{self.owner}&{other.owner}', self.amount + other.amount)
        current._transactions = self._transactions + other._transactions
        return current

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        return self._transactions.append(amount)

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.amount + amount_to_add < 0:
            raise ValueError('sorry cannot go in debt!')
        account.add_transaction(amount_to_add)
        return f"New balance: {account.balance}"
