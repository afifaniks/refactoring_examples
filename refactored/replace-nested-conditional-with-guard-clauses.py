def get_pay_amount(self):
    if self.is_dead:
        return dead_amount()
    if self.is_separated:
        return separated_amount()
    if self.is_retired:
        return retired_amount()
    return normal_amount()