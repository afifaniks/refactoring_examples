class Order:
    def price(self):
        return Calculator(self).calculate()


class Calculator:
    def __init__(self, order: Order):
        self.primary_base_price = 0
        self.secondary_base_price = 0
        self.tertiary_base_price = 0

    def calculate(self):
        pass