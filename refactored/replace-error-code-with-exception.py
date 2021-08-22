def withdraw(self, amount):
    if amount > self.balance:
        raise ValueError("Balance can't be negative")

    self.balance -= amount