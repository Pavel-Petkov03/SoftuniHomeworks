class Account:
    def __init__(self, id_, balance, pin):
        self.__pin = pin
        self.balance = balance
        self.__id = id_

    def __validate_pin(self, pin):
        return self.__pin == pin

    def get_id(self, pin):
        if self.__validate_pin(pin):
            return self.__id
        return 'Wrong pin'

    def change_pin(self, old_pin, new_pin):
        if self.__validate_pin(old_pin):
            self.__pin = new_pin
            return 'Pin changed'
        return "Wrong pin"


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
