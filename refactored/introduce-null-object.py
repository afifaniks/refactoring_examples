class NullCustomer(Customer):
    def is_none(self):
        return True

    def get_plan(self):
        pass

customer = order.customer or NullCustomer()
customer.get_plan()

