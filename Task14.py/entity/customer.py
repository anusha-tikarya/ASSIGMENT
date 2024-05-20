class Customer:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address

    def __str__(self):
        return f"Customer[ID={self.customer_id}, Name={self.name}, Address={self.address}]"