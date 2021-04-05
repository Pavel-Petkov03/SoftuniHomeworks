class Customer:
    def __init__(self,name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id =1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        pass
