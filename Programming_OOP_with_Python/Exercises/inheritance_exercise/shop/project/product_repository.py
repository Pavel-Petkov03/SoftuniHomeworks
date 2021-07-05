class ProductRepository:
    products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        return self.find_product_by_name(product_name)[0]

    def remove(self, product_name):
        obj = self.find_product_by_name(product_name)
        if obj:
            self.products.remove(obj[0])

    def find_product_by_name(self, product_name):
        return [p for p in self.products if p.name == product_name]

    def __str__(self):
        return '\n'.join([f'{p.name}: {p.quantity}' for p in self.products])
