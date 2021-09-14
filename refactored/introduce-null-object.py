class NullCustomer(Customer):
    def is_none(self):
        return True

    def get_plan(self):
        self.get_null_plan()
    
    def get_null_plan(self) -> str:
        return "Plan"

customer = order.customer or NullCustomer()
customer.get_plan()

