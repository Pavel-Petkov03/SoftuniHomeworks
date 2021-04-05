class Customer:
    id_ = 1
    def __init__(self,name, address, email):
        self.name = name
        self.address = address
        self.email = email

    def __repr__(self):
        return f"Customer <{Customer.id_}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.id_ + 1
