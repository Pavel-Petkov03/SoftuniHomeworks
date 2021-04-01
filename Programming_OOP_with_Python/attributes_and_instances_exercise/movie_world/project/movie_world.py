class MovieWorld:
    STATIC_CAPACITY_FOR_DVD = 15
    STATIC_CAPACITY_FOR_CUSTOMER = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += str(f'{customer}\n')
        for dvd in self.dvds:
            result += str(f'{dvd}\n')
        return result

    @staticmethod
    def dvd_capacity():
        return MovieWorld.STATIC_CAPACITY_FOR_DVD

    @staticmethod
    def customer_capacity():
        return MovieWorld.STATIC_CAPACITY_FOR_CUSTOMER

    @staticmethod
    def get_customer(customer_list, customer_id):
        return [customer for customer in customer_list if customer.id == customer_id][0]

    @staticmethod
    def get_dvd(dvd_list, dvd_id):
        return [dvd for dvd in dvd_list if dvd.id == dvd_id][0]

    @staticmethod
    def return_position_of_customer_in_list(customer_list, obj):
        return customer_list.index(obj)

    @staticmethod
    def return_position_of_dvd_in_list(dvd_list, obj):
        return dvd_list.index(obj)

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        actual_customer = self.get_customer(self.customers, customer_id)
        actual_dvd = self.get_dvd(self.dvds, dvd_id)
        if actual_dvd in actual_customer.rented_dvds:
            return f"{actual_customer.name} has already rented {actual_dvd.name}"
        elif actual_dvd.is_rented:
            return "DVD is already rented"
        elif actual_customer.age < actual_dvd.age_restriction:
            return f"{actual_customer.name} should be at least {actual_dvd.age_restriction} to rent this movie"
        else:
            place_for_dvd_in_list = self.return_position_of_dvd_in_list(self.dvds, actual_dvd)
            place_for_customer_in_list = self.return_position_of_customer_in_list(self.customers, actual_customer)
            self.dvds[place_for_dvd_in_list].is_rented = True
            self.customers[place_for_customer_in_list].rented_dvds.append(actual_dvd)

            return f"{actual_customer.name} has successfully rented {actual_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        actual_customer = self.get_customer(self.customers, customer_id)
        actual_dvd = self.get_dvd(self.dvds, dvd_id)
        if actual_dvd in actual_customer.rented_dvds:
            place_for_dvd_in_list = self.return_position_of_dvd_in_list(self.dvds, actual_dvd)
            place_for_customer_in_list = self.return_position_of_customer_in_list(self.customers, actual_customer)
            self.customers[place_for_customer_in_list].rented_dvds.remove(actual_dvd)
            self.dvds[place_for_dvd_in_list].is_rented = False
            return f"{actual_customer.name} has successfully returned {actual_dvd.name}"
        return f"{actual_customer.name} does not have that DVD"
